from abc import ABC, abstractmethod

import numpy as np
from joblib import Parallel, delayed, cpu_count

from .information_theory import get_info_length


def _logdomain_diff(x, y):
    #Copied from http://polarcodes.com Matlab package
    return x + np.log1p(-np.exp(y-x))


class Encoder(ABC):
    """Abstract encoder class"""
    def __init__(self, code_length, info_length, base=2, parallel=True, **kwargs):
        self.code_length = code_length
        self.info_length = info_length
        self.base = base
        self.parallel = parallel

    @abstractmethod
    def encode_messages(self, messages): pass


class IdentityEncoder(Encoder):
    @staticmethod
    def encode_messages(messages):
        return messages


class RepetitionEncoder(Encoder):
    def __init__(self, code_length, **kwargs):
        super().__init__(code_length, info_length=1)

    def encode_messages(self, messages):
        messages = np.reshape(messages, (-1, 1))
        messages = np.repeat(messages, self.code_length, axis=1)
        return messages


class LinearEncoder(Encoder):
    """Linear block encoder.

    Parameters
    ----------
    code_matrix : array
        Code generation matrix. Dimension is (info_bits, code_length).

    base : int, optional
        Base of the field. Default is binary (2).
    """
    def __init__(self, code_matrix, base=2, **kwargs):
        self.code_matrix = code_matrix
        info_length, code_length = np.shape(code_matrix)
        super().__init__(code_length, info_length, base=base)

    def encode_messages(self, messages):
        codewords = np.matmul(messages, self.code_matrix)
        return np.mod(codewords, self.base)


class PolarEncoder(Encoder):
    """Polar code encoder.

    The implementation is copied from the Matlab implementation from
    http://www.polarcodes.com

    Parameters
    ----------
    code_length : int
        Length of the codewords.

    info_length : int
        Number of information bits.

    design_channel : str or Channel object
        Design channel name or channel object. Supported are: `AWGN`, `BEC` and
        `BSC`.

    design_channelstate: float (optional)
        State of the design channel. AWGN: SNR, BEC: epsilon, BSC: p.

    frozenbits : array (optional)
        Array of frozen bits. If not given, all zeros will be used.

    parallel : bool (optional)
        Use parallel encoding of the codewords. This might not be supported on 
        all machines.
    """
    def __init__(self, code_length, info_length, design_channel,
                 design_channelstate=0., frozenbits=None, parallel=True, **kwargs):
        self.design_channel = design_channel
        self.design_channelstate = design_channelstate
        self.frozenbits = frozenbits
        self.pos_lookup = self.construct_polar_code(
            code_length, info_length, design_channel, design_channelstate,
            frozenbits)
        super().__init__(code_length, info_length, parallel=parallel)

    @staticmethod
    def construct_polar_code(code_length, info_length, design_channel,
                             design_channelstate, frozenbits=None):
        design_channel = design_channel.upper()
        z0 = np.zeros(code_length)
        if design_channel == "BAWGN":
            param = 10**(design_channelstate/10.)
            z0[0] = -param*(info_length/code_length)
        elif design_channel == "BSC":
            z0[0] = (np.log(2) + .5*np.log(design_channelstate) +
                     .5*np.log(1-design_channelstate))
        elif design_channel == "BEC":
            z0[0] = np.log(design_channelstate)
        for j in range(1, int(np.log2(code_length))+1):
            u = 2**j
            for t in range(int(u/2)):
                T = z0[t]
                z0[t] = _logdomain_diff(np.log(2)+T, 2*T)
                z0[int(u/2)+t] = 2*T
        idx = np.argsort(z0)
        idx_good = np.sort(idx[:info_length])
        idx_bad = np.sort(idx[info_length:])

        A = np.zeros(code_length, dtype=int)
        A[idx_good] = -1  # information bits
        if frozenbits is None:
            frozenbits = np.zeros(code_length-info_length)
        A[idx_bad] = frozenbits
        return A


    def encode_messages(self, messages):
        code_words = np.zeros((len(messages), self.code_length))
        _pos_lookup = np.tile(self.pos_lookup, (len(messages), 1))
        if self.parallel:
            num_cores = cpu_count()
            code_words = Parallel(n_jobs=num_cores)(
                delayed(self._encode_single_message)(
                     k, _pos_lookup[idx]) for idx, k in enumerate(messages))
            code_words = np.array(code_words)
        else:
            for idx, message in enumerate(messages):
                code_words[idx] = self._encode_single_message(
                    message, _pos_lookup[idx])
        return code_words

    # The following methods are copied from pencode.m file (polarcodes.com)
    def _encode_single_message(self, message, pos_lookup):
        code_word = self._fill_single_codeword(message, pos_lookup)
        code_word = self._transform_single_codeword(code_word)
        return code_word

    @staticmethod
    def _fill_single_codeword(message, pos_lookup):
        code_length = len(pos_lookup)
        code_word = np.array(pos_lookup)
        code_word[code_word == -1] = message
        return code_word

    @staticmethod
    def _transform_single_codeword(code_word):
        code_length = len(code_word)
        n = int(np.ceil(np.log2(code_length)))
        for i in range(n):
            B = 2**(n-i)
            nB = 2**(i)
            for j in range(nB):
                base = j*B
                for l in range(int(B/2)):
                    code_word[base+l] = np.mod(
                        code_word[base+l] + code_word[int(base+B/2+l)], 2)
        return code_word


class PolarWiretapEncoder(PolarEncoder):
    """Encoder for polar wiretap codes.

    It uses [1] for the construction of the codes.

    [1] H. Mahdavifar and A. Vardy, "Achieving the Secrecy Capacity of Wiretap
    Channels Using Polar Codes" IEEE Trans. Inf. Theory, vol. 57, no. 10,
    pp. 6428–6443, Oct. 2011.

    Parameters
    ----------
    code_length : int
        Length of the code

    design_channel_bob : str or Channel object
        Name of the design channel to Bob (main channel)

    design_channel_eve : str or Channel object
        Name of the design channel to Eve (wiretap channel)

    design_channelstate_bob : float, optional
        Design channelstate of the main channel. It is ignored if the
        `design_channel_bob` argument is a Channel like object.

    design_channelstate_eve : float, optional
        Design chanelstate of the wiretap channel. It is ignored if the
        `design_channel_eve` argument is a Channel like object.

    frozenbits : array, optional
        Array of frozen bits. If not given, all zeros will be used.
        
    """
    def __init__(self, code_length, design_channel_bob, design_channel_eve,
        design_channelstate_bob=0, design_channelstate_eve=0, frozenbits=None,
        parallel=True, **kwargs):
        self.pos_lookup = self.construct_polar_wiretap_code(code_length,
            design_channel_bob, design_channel_eve, design_channelstate_bob,
            design_channelstate_eve, frozenbits)
        info_length = np.count_nonzero(self.pos_lookup == -1)
        #self.info_length_bob = np.count_nonzero(self.pos_lookup == -2) + info_length
        self.info_length_bob = np.count_nonzero(self.pos_lookup < 0)
        Encoder.__init__(self, code_length, info_length, parallel=parallel)


    @staticmethod
    def construct_polar_wiretap_code(code_length, design_channel_bob,
        design_channel_eve, design_channelstate_bob, design_channelstate_eve,
        frozenbits=None):
        info_length_bob = get_info_length(code_length, design_channel_bob,
                                          design_channelstate_bob)
        info_length_eve = get_info_length(code_length, design_channel_eve,
                                          design_channelstate_eve)
        good_bob = PolarEncoder.construct_polar_code(code_length,
            info_length_bob, design_channel_bob, design_channelstate_bob, frozenbits)
        good_eve = PolarEncoder.construct_polar_code(code_length,
            info_length_eve, design_channel_eve, design_channelstate_eve, frozenbits)
        good_bob = np.where(good_bob == -1)
        good_eve = np.where(good_eve == -1)
        sec_bits = np.setdiff1d(good_bob, good_eve)
        pos_lookup = np.zeros(code_length)
        pos_lookup[good_eve] = -2  # random bits
        pos_lookup[sec_bits] = -1  # secure bits
        return pos_lookup

    @staticmethod
    def _fill_single_codeword(message, pos_lookup):
        code_word = PolarEncoder._fill_single_codeword(message, pos_lookup)
        _num_random = np.count_nonzero(code_word == -2)
        code_word[code_word == -2] = np.random.randint(0, 2, size=_num_random)
        return code_word

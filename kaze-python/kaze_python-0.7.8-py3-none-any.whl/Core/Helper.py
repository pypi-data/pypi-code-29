from base58 import b58decode
from logzero import logger
import binascii
from kaze.Blockchain import GetBlockchain, GetStateReader
from kazecore.Cryptography.Crypto import Crypto
from kazecore.IO.BinaryWriter import BinaryWriter
from kazecore.UInt160 import UInt160
from kaze.IO.MemoryStream import StreamManager
from kaze.VM.ScriptBuilder import ScriptBuilder
from kaze.SmartContract.ApplicationEngine import ApplicationEngine
from kazecore.Fixed8 import Fixed8
from kaze.SmartContract import TriggerType
from kaze.Settings import settings
from kaze.EventHub import events


class Helper:

    @staticmethod
    def WeightedFilter(list):
        raise NotImplementedError()

    @staticmethod
    def WeightedAverage(list):
        raise NotImplementedError()

    @staticmethod
    def GetHashData(hashable):
        """
        Get the data used for hashing.

        Args:
            hashable (kaze.IO.Mixins.SerializableMixin): object extending SerializableMixin

        Returns:
            bytes:
        """
        ms = StreamManager.GetStream()
        writer = BinaryWriter(ms)
        hashable.SerializeUnsigned(writer)
        ms.flush()
        retVal = ms.ToArray()
        StreamManager.ReleaseStream(ms)
        return retVal

    @staticmethod
    def Sign(verifiable, keypair):
        """
        Sign the `verifiable` object with the private key from `keypair`.

        Args:
            verifiable:
            keypair (kazecore.KeyPair):

        Returns:
            bool: True if successfully signed. False otherwise.
        """
        prikey = bytes(keypair.PrivateKey)
        hashdata = verifiable.GetHashData()
        res = Crypto.Default().Sign(hashdata, prikey)
        return res

    @staticmethod
    def ToArray(value):
        """
        Serialize the given `value` to a an array of bytes.

        Args:
            value (kaze.IO.Mixins.SerializableMixin): object extending SerializableMixin.

        Returns:
            bytes:
        """
        ms = StreamManager.GetStream()
        writer = BinaryWriter(ms)

        value.Serialize(writer)

        retVal = ms.ToArray()
        StreamManager.ReleaseStream(ms)

        return retVal

    @staticmethod
    def AddrStrToScriptHash(address):
        """
        Convert a public address to a script hash.

        Args:
            address (str): base 58 check encoded public address.

        Raises:
            ValueError: if the address length of address version is incorrect.
            Exception: if the address checksum fails.

        Returns:
            UInt160:
        """
        data = b58decode(address)
        if len(data) != 25:
            raise ValueError('Not correct Address, wrong length.')
        if data[0] != settings.ADDRESS_VERSION:
            raise ValueError('Not correct Coin Version')

        checksum = Crypto.Default().Hash256(data[:21])[:4]
        if checksum != data[21:]:
            raise Exception('Address format error')
        return UInt160(data=data[1:21])

    @staticmethod
    def ToScriptHash(scripts):
        """
        Get a hash of the provided message using the ripemd160 algorithm.

        Args:
            scripts (str): message to hash.

        Returns:
            str: hash as a double digit hex string.
        """
        return Crypto.Hash160(scripts)

    @staticmethod
    def RawBytesToScriptHash(raw):
        """
        Get a hash of the provided raw bytes using the ripemd160 algorithm.

        Args:
            raw (bytes): byte array of raw bytes. i.e. b'\xAA\xBB\xCC'

        Returns:
            UInt160:
        """
        rawh = binascii.unhexlify(raw)
        rawhashstr = binascii.unhexlify(bytes(Crypto.Hash160(rawh), encoding='utf-8'))
        return UInt160(data=rawhashstr)

    @staticmethod
    def VerifyScripts(verifiable):
        """
        Verify the scripts of the provided `verifiable` object.

        Args:
            verifiable (kaze.IO.Mixins.VerifiableMixin):

        Returns:
            bool: True if verification is successful. False otherwise.
        """
        try:
            hashes = verifiable.GetScriptHashesForVerifying()
        except Exception as e:
            logger.error("couldn't get script hashes %s " % e)
            return False

        if len(hashes) != len(verifiable.Scripts):
            return False

        blockchain = GetBlockchain()

        for i in range(0, len(hashes)):
            verification = verifiable.Scripts[i].VerificationScript

            if len(verification) == 0:
                sb = ScriptBuilder()
                sb.EmitAppCall(hashes[i].Data)
                verification = sb.ToArray()

            else:
                verification_hash = Crypto.ToScriptHash(verification, unhex=False)
                if hashes[i] != verification_hash:
                    return False

            state_reader = GetStateReader()
            engine = ApplicationEngine(TriggerType.Verification, verifiable, blockchain, state_reader, Fixed8.Zero())
            engine.LoadScript(verification, False)
            invoction = verifiable.Scripts[i].InvocationScript
            engine.LoadScript(invoction, True)

            try:
                success = engine.Execute()
                state_reader.ExecutionCompleted(engine, success)
            except Exception as e:
                state_reader.ExecutionCompleted(engine, False, e)

            if engine.EvaluationStack.Count != 1 or not engine.EvaluationStack.Pop().GetBoolean():
                Helper.EmitServiceEvents(state_reader)
                return False

            Helper.EmitServiceEvents(state_reader)

        return True

    @staticmethod
    def IToBA(value):
        return [1 if digit == '1' else 0 for digit in bin(value)[2:]]

    @staticmethod
    def EmitServiceEvents(state_reader):
        for event in state_reader.events_to_dispatch:
            events.emit(event.event_type, event)

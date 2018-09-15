'''
Created on Aug 11,  2017

This is a conversion of Uwe Reichel's matlab script into python.

@author: Tim Mahrt
'''

import io
import os
from os.path import join
import wave
import math

def detectSyllableNuclei(wavFN, outputFN):
    #   Bootstrap script for Uwe Reichels nucleus detection.
    #function[]  =  detect_syllable_nuclei(path_to_files,  output_path)
    
    files = dir(fullfile(path_to_files, ' * .wav'))
    for file in files:
        [tossPath, name, tossExt] = fileparts(file.name)
        
        y, fs =     (inputFN)
        opt.fs = fs
        opt.verbose = 0
        sn = fu_sylncl(y, opt)
        
        sn = sn / float(fs)  # Get the timestamps in seconds
        
        output_fn = fullfile(output_path, name + '.txt')
        fd = fopen(output_fn, 'w')
        fprintf(fd, '#f\n', sn)
        fclose(fd)
    
    return


def fu_sylncl(s, opt):
    '''
    #function [sn sb]  =  fu_sylncl(s, opt)
    
    # sn  =  fu_sylncl(s, opt)
    # [sn sb]  =  fu_sylncl(s, opt)
    # opt.do = 'apply':
    #  default case.
    #  returns vector sn of syllable nucleus samples in speech signal s
    #  given opt structure with fields as specified in training output below.
    #  Optionally,  sb,  a vector of syllable boundary samples is returned
    #  (simply the sample minimum energy between two adjacent nuclei)
    # opt.do = 'train':
    #   .ref: sample reference
    #   .fs: sample frequency
    #   .errtype:  < 'f' > |'io'|'mae'
    #       error type: 1 - fscore (best choice)
    #                   n_ins + n_omis (used in diss)
    #                   1 - MAE (after alignment)
    #  returns structure SN to be used as OPT in 'apply' case
    #   .f_thresh: energy threshold factor
    #   .bf: lower and upper boundary frequencies for band pass filtering
    #   .do: 'apply'
    #   .fs: sample frequency of input signal
    #   .e_min: minimum needed proportion of max energy
    #   .length: length of energy window in s
    #   .rlength: length of reference energy window ( > length) in s
    #   .md: min distance between subsequent nuclei in s (set to 0 if to be
    #       neglected)
    #   .nouse_int:  < [] >  n x 2 matrix [on off] of intervals not to be used
    #        (e.g. pause intervals). In samples! E.g. output of
    #        fu_pause_detector (with opt.ret = 'smpl'). Additionally,
    #        0 - output of fu_voicing (to be transformed for compatibility) can
    #        be used. Both can also be called inline setting .do_nouse > 0
    #   .do_nouse:  < 0 > |1|2|3: create or enlarge .nouse_int matrix by
    #       finding pauses and / or voiceless utterance parts
    #             < 0 >   -  do nothing
    #            1  -  detect pauses and voiceless utterance parts
    #            2  -  pause only
    #            3  -  voiceless utterance parts only
    #   .verbose: plot signal and nuclei
    #
    #  -  -  exclude pause and voiceless intervals from analysis?
    # opt.pau.do =  < 'apply' > |'skip': prceeding
    #        . *  see matlab_lib / fu_pause_detector.m
    # opt.voi.do =  < 'apply' > |'skip': preceeding voicing detection
    #        . * : see fu_voicing.m
    #
    # minimal application example:
    # [y fs]  =  wavread('myaudio.wav')
    # opt.fs  =  fs
    # opt.verbose  =  1
    # [sn sb]  =  fu_sylncl(y, opt)
    '''
    
    # WHAT?
    #global s_glob
    #global opt_glob
    #close all
    
    if nargin == 1:
        opt = struct
    opt = fu_optstruct_init(opt,
                            ('do', 'nouse_int', 'do_nouse', 'errtype'),
                            ('apply', [], 2, 'f'))
    ofld = ('do', 'bf', 'f_thresh', 'length', 'rlength', 'md', 'e_min', 'fs',
            'verbose', 'pau', 'unv')
    
    # preprocessing -> defining intervals not usable for syllable nuclei
    # matrix,  rows: on- and offset in samples
    # opt.nouse_int = fu_sylncl_no_use_intervals(s, opt)
    opt.nouse_int = []
    
    if opt.do == 'apply':       ###### apply #########
        # fscore optimised on si1000p reference data
        odef = ('apply', [212.5509, 3967.1], 1.0681, 0.0776, 0.1491, 0.1,
                0.1571, 16000, 0, struct, struct)
        opt = fu_optstruct_init(opt, ofld, odef)
        opt.pau = fu_optstruct_init(opt.pau, ('fs', 'ret'), (opt.fs, 'smpl'))
        opt.unv = fu_optstruct_init(opt.unv, ('sts'), (1))
        sn = fu_sylncl_sub(s, opt)
        # add syl boundaries
        if nargout > 1:
            sb = fu_sylbnd(s, sn, opt)
        
    else:                            ###### train #########
        s_glob = s
        opt_glob = opt
        # o_opt = optimset(@fminunc)
        o_opt = optimset(fminsearch)
        o_opt = optimset('LargeScale', 'on')
        # [f_lowbnd / 100 f_upbndf / 1000 threshold_factor ncl_length ref_length
        #  minimum_rms]
        w0 = [2.3, 2.9, 1.06, 0.08, 0.14, 0.16]
        
        # [w fval ef o] = fminunc(@fu_sylncl_err, w0, o_opt)
        [w, fval, ef, o] = fminsearch(fu_sylncl_err, w0, o_opt)
        odef = ('apply', [w(1) * 100, w(2) * 1000], w(3), w(4), w(5),
                w(6), opt.fs, 1)
        opt = fu_optstruct_init(opt, ofld, odef)
        sn = fu_sylncl_sub(s, opt)
    
    '''
    if opt.verbose == 1:
        # [sn [sb NaN]]
        # t = [1:length(s)]. / opt.fs
        t = range(len(s))
        plot(t, s)
        #hold on
        # if isfield(opt, 'ref')
        #    for i = opt.ref plot([i i], [ - 1 1], ' - g')
        #
        for i = sn plot([i i], [-1 1], '-r')
        if nargout > 1:
            for i = sb plot([i i], [-1 1], '-g')
    '''
    if opt.do == 'train':
        opt.do = 'apply'
        opt.error = fval
        sn = opt
        sn_opt = opt
        save('sn_opt', 'sn_opt')
        
    return [sn, sb]


def fu_optstruct_init(opt, optfields, optdefaults):
    '''
    function opt  =  fu_optstruct_init(opt, optfields, optdefaults)
    
    #opt  =  fu_optstruct_init(opt, optfields, optdefaults)
    #initialisation of option structure OPT
    #assigns each field given in cell array OPTFIELDS with corresponding
    #default value given in cell array OPTDEFAULTS,  whenever field is not
    #yet specified
    #if OPTDEFAULTS[i] is 'oblig' then optfields[i] had already to be set
    #by the user. If not,  an error is given.
    '''
    for n in range(len(optfields)):
        if not isfield(opt, optfields[n]):
            if ((not isnumeric(optdefaults[n])) and optdefaults[n] == 'oblig'):
                error(sprintf('opt field "#s" has to be defined by the user!',
                              optfields[n]))
            
            opt = setfield(opt, optfields[n], optdefaults[n])
    
    return opt


def fu_sylncl_sub(s, opt):
    '''
    function t = fu_sylncl_sub(s, opt)
    
    # returns samples of syllable nuclei given signal S and processing
    # options OPT (see fu_sylncl for details)
    # called by fu_sylncl
    
    # recall higher before 2. nucl splitting. why???
    '''
    # settings ################################################
    # reference window span
    rws = math.floor(opt.rlength * opt.fs)
    # signal length
    ls = len(s)
    # window length for energy calculation in samples
    ml = math.floor(opt.length * opt.fs)
    # minimum distance between subsequent nuclei in samples
    md = math.floor(opt.md * opt.fs)
    # stepsize
    sts = max(1, math.floor(0.03 * opt.fs))
    stsh = math.floor(sts / float(2))  # for centering of reference window
    
    # no use intervals (pause,  voiceless) ####################
    #  -  >  vector of all samples not to be used
    t_nou_init = []
    t_nou_pau = []
    voi = []
    t_nou = []
    if isfield(opt, 'nouse_int'):
        t_nou_init = opt.nouse_int
    
    if opt.do_nouse > 0:
        if opt.do_nouse < 3:
            t_nou_pau = fu_pause_detector(s, opt.pau)
       
        if (opt.do_nouse == 1 or opt.do_nouse == 3):
            [voi, zrr] = fu_voicing(s, opt.fs, opt.unv)
        
    for i in range(size(t_nou_init, 1)):
        t_nou = [t_nou, range(t_nou_init(i, 1), t_nou_init(i, 2))]
    
    for i in range(size(t_nou_pau, 1)):
        t_nou = [t_nou, range(t_nou_pau(i, 1), t_nou_pau(i, 2))]
    
    t_nou = unique([t_nou, transpose(find(voi == 0))])
    
    # filtering ###########################################
    ft = 'low' if len(opt.bf) == 1 else 'band'
    
    # filter order,  the higher the steeper,  but incapable to filter narrow
    # bands
    ord = 5
    s = fu_filter(s, ft, opt.bf, opt.fs, ord)
    
    # settings 2 ##########################################
    # minimum energy as portion of maximum energy found
    e_y = []
    # for i = 1:sts:ls
    for i in range(1, ls, sts):
        # window #############################
        yi = range(i, min(ls, i + ml - 1))
        y = s(yi)
        e_y = [e_y, fu_rmse(y)]
    
    e_min = opt.e_min * max(e_y)
    mey = max(e_y)
    
    # output vector collecting nucleus sample indices
    t = []
    
    all_i = []
    all_e = []
    all_r = []
    
    # for i = 1:sts:ls
    for i in range(1, ls, sts):
        yi = fu_i_window(i, ml, ls)
        y = s(yi)
        e_y = fu_rmse(y)
        rwi = fu_i_window(i, rws, ls)
        rw = s(rwi)
        e_rw = fu_rmse(rw)
        all_i = [all_i i]
        all_e = [all_e e_y]
        all_r = [all_r e_rw]
    
    lmopt = struct
    
    lmopt.peak.mpd = math.floor(opt.fs * opt.md / float(sts))
    [pks, idx] = fu_locmax(all_e, lmopt)
    t = []
    for i = idx:
        if (all_e(i) >= all_r(i) * opt.f_thresh and all_e(i) > e_min):
            if length(find(t_nou == all_i(i))) == 0:
                t = [t all_i(i)]

    return t


def fu_sylbnd(s, sn, opt):
    '''
    function sb  =  fu_sylbnd(s, sn, opt)
    
    #sb  =  fu_sylbnd(s, sn, opt)
    #called in fu_sylncl
    #s: signal vector
    #sn: vector with detected nucleus samples (by fu_sylncl_sub)
    #opt: as provided for fu_sylncl
    '''
    
    # window length for energy calculation in samples
    ml = math.floor(opt.length * opt.fs)
    # stepsize
    sts = max(1, math.floor(0.03 * opt.fs))
    
    sb = []
    # for i = 1:length(sn) - 1  # for all adjacent syl ncl
    for i in range(len(sn) - 1):
        on = sn(i)
        off = sn(i + 1)
        sw = s(on:off)
        ls = len(sw)
        all_i = []
        all_e = []
#         for j = 1:sts:length(sw)  # for all windows within ncl pair
        for j in range(0, len(sw), sts):  # for all windows within ncl pair
            yi = fu_i_window(j, ml, ls)
            y = sw(yi)
            e_y = fu_rmse(y)
            all_i = [all_i j]
            all_e = [all_e e_y]
        
        [ymin, ymini] = min(all_e)
        sb = [sb on + all_i(ymini(1))]
    
    return sb


def fu_pause_detector(s, opt):
    '''
    function t  =  fu_pause_detector(s, opt)
    
    # t  =  fu_pause_detector(s, opt)
    # looks for pauses in signal according to criterias
    # specified in opt
    # input: s  -  signal vector
    #        opt  -  structure with fields
    #           .length: minimum length of pause in s
    #           .rlength: length of reference window in s
    #           .f_thresh: threshold factor ( * rmse(reference_window))
    #           .fs: sample rate
    #           .ret:  < 's' > |'smpl' return values in seconds or samples
    #       default (optimised on IMS radio news corpus,  read speech,
    #             by fminunc()):
    #           opt.length  =  0.1524
    #           opt.f_thresh  =  0.0767
    #           opt.rlength  =  5
    #           opt.fs  =  16000
    # output: t  -  matrix of pause time on -  and offsets (in s)
    # algorithm:
    #  -  preprocessing: removing DC,  low pass filtering (10kHz)
    #  -  window y with opt.length sec is moved over signal with stepsize
    #   0.05 s
    #  -  reference window rw with opt.rlength sec centered on y midpoint
    #   is moved in parallel
    #  -  if rmse(rw)  <  rmse(global_signal) * opt.f_thresh
    #       rw is set to global_signal (long pause assumed)
    #  -  if rmse(y)  <  rmse(rw) * opt.f_thresh
    #       y is considered as a pause
    # Uwe Reichel,  IPS (2009)
    '''
    
    # defaults ##########################################
    if nargin == 1:
        opt = struct
    ofld = ['f_thresh', 'length', 'rlength', 'fs', 'ret']
    odef = [0.0767, 0.1524, 5, 16000, 's']
    opt = fu_optstruct_init(opt, ofld, odef)
    
    # preprocessing #####################################
    # stereo -  > mono,  mean 0
    s = s(:, 1) - mean(s(:, 1))
    # low pass filtering (just carried out if fs  >  20kHz)
    s = fu_filter(s, 'low', 10000, opt.fs)
    
    # settings ##########################################
    # reference window span
    rws = math.floor(opt.rlength * opt.fs)
    # signal length
    ls = len(s)
    # min pause length in samples
    ml = math.floor(opt.length * opt.fs)
    # global rmse and pause threshold
    e_glob = fu_rmse(s)
    t_glob = opt.f_thresh * e_glob
    # stepsize
    # sts = floor(ml / 4)
    sts = max(1, math.floor(0.05 * opt.fs))
    stsh = math.floor(sts / 2)  # for centering of reference window
    
    # pause detection ###################################
    # output array collecting pause sample indices
    t = []
    j = 1
    
    # for x in range(1:sts:ls):
    for i in range(0, sts, ls):
        # window #############################
        yi = range(i, min(ls, i + ml - 1))
        # tt = [yi(1) yi()]
        y = s(yi)
        e_y = fu_rmse(y)
        # reference window ###################
        rw = s(fu_i_window(min(i + stsh, ls), rws, ls))
        e_rw = fu_rmse(rw)
        if (e_rw <= t_glob):
            e_rw = e_glob
        # if rmse in window below threshold ##
        if e_y <= (e_rw * opt.f_thresh):
            if size(t, 1) == j:
                # values belong to already detected pause
                if yi(1) < t(j, 2):
                    t(j, 2) = yi()
                else:                          # new pause
                    j = j + 1
                    t(j, :) = [yi(1), yi()]
                
            else:                              # new pause
                t(j, :) = [yi(1), yi()]
    
    # conversion of sample indices into ##############
    # time on -  and offset values (sec) ###############
    
    if opt.ret == 's':
        t = t / float(opt.fs)
    
    return t


def fu_filter(s, t, gf, fs, o):
    '''
    function sflt = fu_filter(s, t, gf, fs, o)
    
    #sflt = fu_filter(s, t, gf, fs)
    #s: signal vector
    #t: type 'high'|'low'|'stop'|'band'
    #gf: grenzfrequenzen (1 Wert-->  Hoch - ,  Tiefpass,  2 Werte-->  Bandpass)
    #fs: sample frequency
    #o: order,  default 10
    #applies butter filter
    #operates only if gf  <  fs / 2
    '''
    fn = gf / float(fs / 2)
    
    if fn > = 1:
        sflt = s
        return
    
    if nargin < 5:
        o = 5
    
    if strcmp(t, 'band'):
        [b a] = butter(o, fn)
    else:
        [b a] = butter(o, fn, t)
    
    sflt = filtfilt(b, a, s)
    
    if length(find(isnan(sflt))) > 0:
        disp('filtering not possible,  returning original signal')
        sflt = s
    
    '''
    #freqz(b, a, 128, fs)
    #subplot(2, 1, 1)
    #x = 32000:32000 + fs
    #plot(x, s(x), ' - b')
    #subplot(2, 1, 2)
    #plot(x, sflt(x), ' - b')
    #a = 300000
    #fhpt_play(sflt * a)
    '''
    return sflt


def fu_i_window(i, wl, l):
    '''
    #function wi  =  fu_i_window(i, wl, l)
    
    # wi  =  fu_i_window(i, wl, l)
    # i: index in vector
    # wl: window length
    # l: vector length
    # wi: indices in window around i
    #  -  returns indices of window around index i in vector of length l
    #  -  if distance from i to  or beginning of vector is less than wl / 2,
    #   the window is shifted accordingly
    '''
    hwl = math.floor(wl / float(2))
    wi = range(max(i - hwl, 1), min(i + hwl, l))
    
    # if window too short: trying to lengthen window to wanted size
    d = wl - len(wi)
    if d > 0:
        if wi(1) > 1:
            o = max(wi(1) - d, 1)
            wi = range(o, wi())
            d = wl - len(wi)
        
        if d > 0:
            if wi() < l:
                o = min(wi() + d, l)
                wi = range(wi(1), o)

    return wi


def fu_rmse(x, y):
    '''
    function e  =  fu_rmse(x,  y)
    
    #e  =  fu_rmse(x)
    #e  =  fu_rmse(x, y)
    #returns root mean squared error E between vector X and 0 - line
    #or root mean squared error E between vectors X and Y
    '''
    
    if nargin < 2:
        e = math.sqrt(sum(x**2) / float(len(x)))
    else:
        e = math.sqrt(sum((x - y)**2) / float(len(x)))
    
    return e


def fu_voicing(y, sr, opt):
    '''
    function [voi zrr] = fu_voicing(y,sr,opt)

    # voi = fu_voicing(y,sr <,opt>)
    # [voi zr] = fu_voicing(y,sr <,opt>)
    # Y: signal
    # SR: sample rate
    # VOI: vector with 1 element per window
    #   1: voiced
    #   0: voiceless/pause
    # ZR: do=='apply': vector of zero crossing rates, one value per window
    #         'train': opt struct with optimised .th and .zr_th and .err error
    # OPT:
    #   .do: <apply>|train
    #   .wl: window length <0.03> (<1: in s, >=1: in samples)
    #   .th: <0.002> relative amplitude threshold, y<max*.th is ignored
    #   .sts: step size <0.01> (<1: in s, >=1: in samples)
    #   .zr_th: <2000> (below & >0: voiced use higher value for increased
    #           recall, lower value for increased precision)
    #   .min_nf: <3> (min number of frames in a row to be constantly
    #                 (un)voiced. Interpolation over shorter sequences
    #   .ret: <'w'>|'smpl'
    #            'w': one value per window
    #            'smpl': one value per signal sample
    #  IF .do equal 'train'
    #   .errfun <@fu_voicing_err>
    #   .ref: reference matrix or vector (see e.g. voi_ref.dat)
    #   --> optimisation of .th and .zr_th
    #   integrated training call by FU_VOI_OPTIM_BRACKET
    #
    # voicing detection by zero crossing rate
    # BEWARE: Default parameters are optimised on si1000p reference and
    # sts=0.01. If step size is changed, than $sts in sncl_ref.pl has to
    # be changed the same way!!!
    # param values are informally optimised on SI1000P reference data:
    #   hamming: 0.1180
    # precision: 0.8898
    #    recall: 0.9045
    '''
    if nargin < 3:
        opt=struct
    
    optt = ('wl', 'th', 'sts', 'zr_th', 'do', 'min_nf', 'ret')
    optf = (0.03, 0.002, 0.01, 2000, 'apply', 3, 'w')
    opt = fu_optstruct_init(opt, optt, optf)
    opt.sr = sr
    
    if opt.do == 'apply':  # application
        [voi, zr] = fu_voicing_sub(y, opt)
        if nargout == 2:
            zrr = zr
    else:  # training
        # o_opt=optimset(@fminunc)
        o_opt = optimset(fminsearch)
        o_opt = optimset('LargeScale','on')
        w0 = [0.004, 1000]
        #[w fval ef o]=fminunc(opt.errfun,w0,o_opt)
        [w, fval, ef, o] = fminsearch(opt.errfun, w0, o_opt)
        opt.th = w(1)
        opt.zr_th = w(2)
        [voiv, zr] = fu_voicing_sub(y, opt)
        # error
        voiv = fu_trim_vec(voiv, opt.ref, 0)
        e = pdist([voivopt.ref], 'hamming')
        voi = opt
        voi.err = e
        if nargout == 2:
            zrr = e  # to avoid crash
    
    return [voi, zrr]


def fu_voicing_sub(y, opt):
    '''
    function [voi zrr] = fu_voicing_sub(y,opt)
    
    # returns binary vector (1=voiced frame) for signal vector Y
    # and specs given in OPT
    # called by fu_voicing
    '''
    
    zr = fu_zero_crossing_rate(y, opt.sr, opt)
    voi = zeros(len(zr), 1)
    voi(find(zr < opt.zr_th and zr > 0)) = 1
    
    if opt.min_nf > 1:
        voi = fu_smooth_binvec(voi, opt.min_nf)
    
    if nargout == 2:
        zrr = zr

    return [voi, zrr]


def fu_locmax(y, opt):
    '''
    function [pks idx] = fu_locmax(y,opt)
    
    #[pks idx] = fu_locmax(y,opt)
    #wrapper around 'findpeaks'
    #y: data vector
    #opt:
    #   .smooth.win <1> smoothing options, see fu_smooth
    #          .mtd <'none'>
    #          .order <1>
    #   .peak.mph: <-Inf>  min peak height
    #          .th: <0>  threshold min difference of local peak to neighbors
    #          .mpd: <1> min peak distance
    #   .verbose.plot: <0>|1
    #           .bw: <0>|1
    #pks: peak values
    #idx: their positions [sample]
    '''

    # init
    if nargin < 2:
        opt = struct
    
    opt = fu_optstruct_init(opt, ('smooth', 'peak'), (struct, struct))
    opt.smooth = fu_optstruct_init(opt.smooth, ('win', 'mtd', 'order'),
                                   (1, 'none', 1))
    opt.peak = fu_optstruct_init(opt.peak, ('mph','th','mpd'), (-Inf, 0, 1))
    
    # locmax
    opt.peak.mpd = min(opt.peak.mpd, len(y) - 1)
    
    [pks, idx] = findpeaks(fu_smooth(y,opt.smooth), 'MINPEAKDISTANCE',
                           opt.peak.mpd, 'MINPEAKHEIGHT', opt.peak.mph,
                           'THRESHOLD', opt.peak.th)
    
    # fallback
    if len(pks)==0
        [pks idx] = findpeaks(y)
    
    
    # transpose to column vector since in 7.10.0 findpeaks() always returns
    # row vector!
    if size(y,2) == 1
        pks = fu_r2c(pks)
        idx = fu_r2c(idx)

    
    return [pks, idx]


def fu_smooth(y, opt):
    '''
    function ys=fu_smooth(y,opt)
    
    #ys=fu_smooth(y,opt)
    #bracket for smoothing
    #faster but less flexible than fu_smoothing
    #y: vector
    # opt.mtd    # as in fun smooth (+ 'none')
    #    .wl     # window length
    #    .order  # polynomial order for sgolay
    '''
    
    if nargin < 1:
        opt=struct
    
    opt=fu_optstruct_init(opt, ('mtd', 'wl', 'order'), ('mova', 5, 3))
    
    if opt.mtd == 'none':
        ys = y
    elif not opt.mtd == 'sgolay':
        ys = smooth(y, opt.wl, opt.mtd)
    else:
        ys = smooth(y, opt.wl, opt.mtd, opt.order)
    
    return ys


def fu_zero_crossing_rate(y, sr, opt):
    '''
    function zr = fu_zero_crossing_rate(y,sr,opt)
    
    #zr = fu_zero_crossing_rate(y,sr [,opt])
    #y: signal vector
    #sr: sample rate (<16000>)
    #opt
    #   .wl: <0.01> window length (<1: in s, >=1: in samples)
    #   .th: <0.004> min abs extreme point amplitude (vs. noise in <p:>)
    #        used as a factor: .th * max(abs(y)) !
    #   .sts: step size <1> (<1: in s, >=1: in samples)
    #zr: zero crossing rate in crossing/sec (same length as Y)
    # set all data points below .th to NaN
    # 
    # center window of length .wl on each data point in Y
    # 
    '''
    
    if nargin < 2:
        sr = 16000
    if nargin < 3:
        opt = struct
    opt = fu_optstruct_init(opt, ('wl', 'th', 'sts'), (0.01, 0.004, 1))
    
    # sec -> samples
    if opt.wl < 1 opt.wl = round(opt.wl * sr)
    if opt.sts < 1 opt.sts = round(opt.sts * sr)
    
    # filter values below threshold
    ya = abs(y)
    y(find(ya < opt.th * max(ya))) = NaN
    
    # multiplying subsequent data points: <=0 -> zero crossing
    zcv = [NaN row2columnvec(y(1:-1).*y(2:))]
    
    # -> matrix, one row per window
    zcm = fu_window_vec(zcv, opt)
    
    # zero crossings
    [ri, ci] = find(zcm <= 0)
    
    # how many zero crossings per window?
    zcw = fu_typecount(ri)
    
    # getting rate
    l = size(zcm, 2)
    
    zr = zeros(size(zcm, 1), 1)
    zr(zcw(:,1)) = zcw(:,2) / l * sr
    
    return zr

def fu_window_vec(v, opt):
    '''
    function m = fu_window_vec(v,opt)
    
    # m = fu_window_vec(v,opt)
    # windows vector V according to specs in struct opt
    # V: input vector
    # M: matrix, one window per row
    # OPT:
    #   .sts: <1> int, step size
    #   .wl: <1> int, window length
    
    # opt init
    # idx is needed for fu_window_bnd, not to be specified by user
    #usable for vectorisation of algorithms
    '''
    
    if nargin < 2:
        opt = struct
    opt = fu_optstruct_init(opt, ('sts', 'wl'), (1, 1))
    opt.idx = 1
    wb = fu_window_bnd(opt.wl, length(v), opt)
    
    m = v(wb)

    return m


def fu_window_bnd(wl, ly, opt):
    '''
    function wb = fu_window_bnd(wl,ly,opt)
    
    #wb = fu_window_bnd(wl,ly,opt)
    #returns matrix of window on- and offset indices (one pair per row)
    #windows are centered on each index 1:opt.sts:ly
    # wl: window length
    # ly: length of vector
    # opt:
    #   .sts: int <1> - step size
    #   .idx: <0>|1   - if one not just bounds but also all indices between
    # e.g. wl=2 ly=6 opt.sts=1 opt.idx=0
    # --> wb = [1 2 1 3 2 4 3 5 4 6 5 6]
    #                             opt.idx=0
    # --> wb = [1 1 2 1 2 3 2 3 4 3 4 5 4 5 6 5 6 6]
    #usable for vectorisation of algorithms
    '''
    
    if nargin < 3:
        opt = struct
    opt = fu_optstruct_init(opt,('sts', 'idx'),(1, 0))
    
    x=tranpose([1:opt.sts:ly])
    h=round(wl / float(2))
    
    if opt.idx == 0:
        hh = [-h, h]
    else:
        hh = range(-h, h)
    
    wb = repmat(hh, size(x, 1), 1) + repmat(x, 1, size(hh, 2))
    wb(find(wb < 1)) = 1
    wb(find(wb > ly)) = ly
    
    return wb


def fu_typecount(v):
    '''
    function tc = fu_typecount(v)
    
    #tc = fu_numcount(v)
    #returns counts of each type in vector V in matrix TC
    #TC: each row contains 'type count'-pair, types are sorted
    #usable for vectorisation of algorithms
    '''
    [vs, i, j] = unique(sort(row2columnvec(v)))
    
    d = diff([0i])
    
    tc = [vs, d]
    
    return tc


def fu_r2c(v):
    '''
    function [v t]=fu_r2c(v)
    
    #v=fu_r2c(v)
    #[v t]=fu_r2c(v)
    #if V is a ROW VECTOR, it is transposed and T is set to 1
    #needed for uniform vector/matrix treatment in functions
    #operating on column vectors
    #see also fu_c2r, fu_transpose
    '''
    tb = 0
    # transpose row vector
    if size(v, 1) == 1:
        v = transpose(v)
        tb = 1
    
    if nargout == 2:
        t = tb
    
    return [v, t]

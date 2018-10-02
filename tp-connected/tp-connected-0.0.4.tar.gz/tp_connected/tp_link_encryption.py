__all__ = ['tp_link_encryption']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['enc'])
@Js
def PyJsHoisted_enc_(val, nn, ee, this, arguments, var=var):
    var = Scope({'val':val, 'nn':nn, 'ee':ee, 'this':this, 'arguments':arguments}, var)
    var.registers(['nn', 'ee', 'result', 'val'])
    var.put('result', var.get('jQuery').get('rsa').callprop('encrypt', var.get('val'), var.get('nn'), var.get('ee')))
    return var.get('result')
PyJsHoisted_enc_.func_name = 'enc'
var.put('enc', PyJsHoisted_enc_)
PyJs_Object_0_ = Js({})
var.put('jQuery', PyJs_Object_0_)
PyJs_Object_1_ = Js({})
var.put('$', PyJs_Object_1_)
PyJs_Object_2_ = Js({})
var.put('navigator', PyJs_Object_2_)
@Js
def PyJs_anonymous_4_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n'])
    @Js
    def PyJs_anonymous_5_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('Math').callprop('random')
    PyJs_anonymous_5_._set_name('anonymous')
    return var.get('Array').callprop('apply', var.get(u"null"), var.get('Array')(var.get('n'))).callprop('map', PyJs_anonymous_5_)
PyJs_anonymous_4_._set_name('anonymous')
PyJs_Object_3_ = Js({'crypto':PyJs_anonymous_4_})
var.put('window', PyJs_Object_3_)
pass
@Js
def PyJs_anonymous_6_(PyJsArg_24_, this, arguments, var=var):
    var = Scope({'$':PyJsArg_24_, 'this':this, 'arguments':arguments}, var)
    var.registers(['$'])
    def PyJs_LONG_104_(var=var):
        PyJs_Object_7_ = Js({})
        @Js
        def PyJs_anonymous_8_(val, nn, ee, this, arguments, var=var):
            var = Scope({'val':val, 'nn':nn, 'ee':ee, 'this':this, 'arguments':arguments}, var)
            var.registers(['dbits', 'rng_psize', 'Montgomery', 'Classic', 'rsaObj', 'rng_state', 'nbits', 'nbv', 'ua', 't', 'parseBigInt', 'Arcfour', 'ee', 'rng_seed_int', 'l', 'rr', 'result', 'nbi', 'n', 'vv', 'rng_pptr', 'BigInteger', 'rng_get_byte', 'prng_newstate', 'BI_RC', 'pkcs1pad2', 'SecureRandom', 'RSAKey', 'rng_seed_time', 'i', 'rng_pool', 'int2char', 'z', 'intAt', 'e', 'nn', 'BI_RM', 'val'])
            @Js
            def PyJsHoisted_BigInteger_(a, b, c, this, arguments, var=var):
                var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
                var.registers(['c', 'b', 'a'])
                def PyJs_LONG_9_(var=var):
                    return ((var.get(u"null")!=var.get('a')) and (var.get(u"this").callprop('fromNumber', var.get('a'), var.get('b'), var.get('c')) if (Js('number')==var.get('a',throw=False).typeof()) else (var.get(u"this").callprop('fromString', var.get('a'), Js(256.0)) if ((var.get(u"null")==var.get('b')) and (Js('string')!=var.get('a',throw=False).typeof())) else var.get(u"this").callprop('fromString', var.get('a'), var.get('b')))))
                PyJs_LONG_9_()
            PyJsHoisted_BigInteger_.func_name = 'BigInteger'
            var.put('BigInteger', PyJsHoisted_BigInteger_)
            @Js
            def PyJsHoisted_nbi_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                return var.get('BigInteger').create(var.get(u"null"))
            PyJsHoisted_nbi_.func_name = 'nbi'
            var.put('nbi', PyJsHoisted_nbi_)
            @Js
            def PyJsHoisted_int2char_(n, this, arguments, var=var):
                var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
                var.registers(['n'])
                return var.get('BI_RM').callprop('charAt', var.get('n'))
            PyJsHoisted_int2char_.func_name = 'int2char'
            var.put('int2char', PyJsHoisted_int2char_)
            @Js
            def PyJsHoisted_intAt_(s, i, this, arguments, var=var):
                var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
                var.registers(['c', 'i', 's'])
                var.put('c', var.get('BI_RC').get(var.get('s').callprop('charCodeAt', var.get('i'))))
                return ((-Js(1.0)) if (var.get(u"null")==var.get('c')) else var.get('c'))
            PyJsHoisted_intAt_.func_name = 'intAt'
            var.put('intAt', PyJsHoisted_intAt_)
            @Js
            def PyJsHoisted_nbv_(i, this, arguments, var=var):
                var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 'i'])
                var.put('r', var.get('nbi')())
                return PyJsComma(var.get('r').callprop('fromInt', var.get('i')),var.get('r'))
            PyJsHoisted_nbv_.func_name = 'nbv'
            var.put('nbv', PyJsHoisted_nbv_)
            @Js
            def PyJsHoisted_nbits_(x, this, arguments, var=var):
                var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 'x', 't'])
                var.put('r', Js(1.0))
                def PyJs_LONG_10_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(((Js(0.0)!=var.put('t', PyJsBshift(var.get('x'),Js(16.0)))) and PyJsComma(var.put('x', var.get('t')),var.put('r', Js(16.0), '+'))),((Js(0.0)!=var.put('t', (var.get('x')>>Js(8.0)))) and PyJsComma(var.put('x', var.get('t')),var.put('r', Js(8.0), '+')))),((Js(0.0)!=var.put('t', (var.get('x')>>Js(4.0)))) and PyJsComma(var.put('x', var.get('t')),var.put('r', Js(4.0), '+')))),((Js(0.0)!=var.put('t', (var.get('x')>>Js(2.0)))) and PyJsComma(var.put('x', var.get('t')),var.put('r', Js(2.0), '+')))),((Js(0.0)!=var.put('t', (var.get('x')>>Js(1.0)))) and PyJsComma(var.put('x', var.get('t')),var.put('r', Js(1.0), '+')))),var.get('r'))
                return PyJs_LONG_10_()
            PyJsHoisted_nbits_.func_name = 'nbits'
            var.put('nbits', PyJsHoisted_nbits_)
            @Js
            def PyJsHoisted_Classic_(m, this, arguments, var=var):
                var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
                var.registers(['m'])
                var.get(u"this").put('m', var.get('m'))
            PyJsHoisted_Classic_.func_name = 'Classic'
            var.put('Classic', PyJsHoisted_Classic_)
            @Js
            def PyJsHoisted_Montgomery_(m, this, arguments, var=var):
                var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
                var.registers(['m'])
                def PyJs_LONG_11_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('m', var.get('m')),var.get(u"this").put('mp', var.get('m').callprop('invDigit'))),var.get(u"this").put('mpl', (Js(32767.0)&var.get(u"this").get('mp')))),var.get(u"this").put('mph', (var.get(u"this").get('mp')>>Js(15.0)))),var.get(u"this").put('um', ((Js(1.0)<<(var.get('m').get('DB')-Js(15.0)))-Js(1.0)))),var.get(u"this").put('mt2', (Js(2.0)*var.get('m').get('t'))))
                PyJs_LONG_11_()
            PyJsHoisted_Montgomery_.func_name = 'Montgomery'
            var.put('Montgomery', PyJsHoisted_Montgomery_)
            @Js
            def PyJsHoisted_Arcfour_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                PyJsComma(PyJsComma(var.get(u"this").put('i', Js(0.0)),var.get(u"this").put('j', Js(0.0))),var.get(u"this").put('S', var.get('Array').create()))
            PyJsHoisted_Arcfour_.func_name = 'Arcfour'
            var.put('Arcfour', PyJsHoisted_Arcfour_)
            @Js
            def PyJsHoisted_prng_newstate_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                return var.get('Arcfour').create()
            PyJsHoisted_prng_newstate_.func_name = 'prng_newstate'
            var.put('prng_newstate', PyJsHoisted_prng_newstate_)
            @Js
            def PyJsHoisted_rng_seed_int_(x, this, arguments, var=var):
                var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                var.registers(['x'])
                def PyJs_LONG_12_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (Js(255.0)&var.get('x')), '^'),var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('x')>>Js(8.0))&Js(255.0)), '^')),var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('x')>>Js(16.0))&Js(255.0)), '^')),var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('x')>>Js(24.0))&Js(255.0)), '^')),((var.get('rng_pptr')>=var.get('rng_psize')) and var.put('rng_pptr', var.get('rng_psize'), '-')))
                PyJs_LONG_12_()
            PyJsHoisted_rng_seed_int_.func_name = 'rng_seed_int'
            var.put('rng_seed_int', PyJsHoisted_rng_seed_int_)
            @Js
            def PyJsHoisted_rng_seed_time_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                var.get('rng_seed_int')(var.get('Date').create().callprop('getTime'))
            PyJsHoisted_rng_seed_time_.func_name = 'rng_seed_time'
            var.put('rng_seed_time', PyJsHoisted_rng_seed_time_)
            @Js
            def PyJsHoisted_rng_get_byte_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                if (var.get(u"null")==var.get('rng_state')):
                    #for JS loop
                    PyJsComma(PyJsComma(var.get('rng_seed_time')(),var.put('rng_state', var.get('prng_newstate')()).callprop('init', var.get('rng_pool'))),var.put('rng_pptr', Js(0.0)))
                    while (var.get('rng_pptr')<var.get('rng_pool').get('length')):
                        try:
                            var.get('rng_pool').put(var.get('rng_pptr'), Js(0.0))
                        finally:
                                var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))
                    var.put('rng_pptr', Js(0.0))
                return var.get('rng_state').callprop('next')
            PyJsHoisted_rng_get_byte_.func_name = 'rng_get_byte'
            var.put('rng_get_byte', PyJsHoisted_rng_get_byte_)
            @Js
            def PyJsHoisted_SecureRandom_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                pass
            PyJsHoisted_SecureRandom_.func_name = 'SecureRandom'
            var.put('SecureRandom', PyJsHoisted_SecureRandom_)
            @Js
            def PyJsHoisted_parseBigInt_(str, r, this, arguments, var=var):
                var = Scope({'str':str, 'r':r, 'this':this, 'arguments':arguments}, var)
                var.registers(['str', 'r'])
                return var.get('BigInteger').create(var.get('str'), var.get('r'))
            PyJsHoisted_parseBigInt_.func_name = 'parseBigInt'
            var.put('parseBigInt', PyJsHoisted_parseBigInt_)
            @Js
            def PyJsHoisted_pkcs1pad2_(s, n, this, arguments, var=var):
                var = Scope({'s':s, 'n':n, 'this':this, 'arguments':arguments}, var)
                var.registers(['s', 'ba', 'c', 'x', 'rng', 'n', 'i'])
                if (var.get('n')<(var.get('s').get('length')+Js(11.0))):
                    return var.get(u"null")
                #for JS loop
                var.put('ba', var.get('Array').create())
                var.put('i', (var.get('s').get('length')-Js(1.0)))
                while ((var.get('i')>=Js(0.0)) and (var.get('n')>Js(0.0))):
                    var.put('c', var.get('s').callprop('charCodeAt', (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))))
                    def PyJs_LONG_13_(var=var):
                        return (PyJsComma(var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((Js(63.0)&var.get('c'))|Js(128.0))),var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')>>Js(6.0))|Js(192.0)))) if ((var.get('c')>Js(127.0)) and (var.get('c')<Js(2048.0))) else PyJsComma(PyJsComma(var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((Js(63.0)&var.get('c'))|Js(128.0))),var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), (((var.get('c')>>Js(6.0))&Js(63.0))|Js(128.0)))),var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')>>Js(12.0))|Js(224.0)))))
                    (var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), var.get('c')) if (var.get('c')<Js(128.0)) else PyJs_LONG_13_())
                
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(0.0))
                #for JS loop
                var.put('rng', var.get('SecureRandom').create())
                var.put('x', var.get('Array').create())
                while (var.get('n')>Js(2.0)):
                    #for JS loop
                    var.get('x').put('0', Js(0.0))
                    while (Js(0.0)==var.get('x').get('0')):
                        var.get('rng').callprop('nextBytes', var.get('x'))
                    
                    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), var.get('x').get('0'))
                
                return PyJsComma(PyJsComma(var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(2.0)),var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(0.0))),var.get('BigInteger').create(var.get('ba')))
            PyJsHoisted_pkcs1pad2_.func_name = 'pkcs1pad2'
            var.put('pkcs1pad2', PyJsHoisted_pkcs1pad2_)
            @Js
            def PyJsHoisted_RSAKey_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                def PyJs_LONG_14_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('n', var.get(u"null")),var.get(u"this").put('e', Js(0.0))),var.get(u"this").put('d', var.get(u"null"))),var.get(u"this").put('p', var.get(u"null"))),var.get(u"this").put('q', var.get(u"null"))),var.get(u"this").put('dmp1', var.get(u"null"))),var.get(u"this").put('dmq1', var.get(u"null"))),var.get(u"this").put('coeff', var.get(u"null")))
                PyJs_LONG_14_()
            PyJsHoisted_RSAKey_.func_name = 'RSAKey'
            var.put('RSAKey', PyJsHoisted_RSAKey_)
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            def PyJs_LONG_19_(var=var):
                @Js
                def PyJs_anonymous_15_(i, x, w, j, c, n, this, arguments, var=var):
                    var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
                    var.registers(['h', 'w', 'xl', 'c', 'l', 'm', 'x', 'j', 'xh', 'n', 'i'])
                    #for JS loop
                    var.put('xl', (Js(32767.0)&var.get('x')))
                    var.put('xh', (var.get('x')>>Js(15.0)))
                    while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
                        var.put('l', (Js(32767.0)&var.get(u"this").get(var.get('i'))))
                        var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(15.0)))
                        var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
                        def PyJs_LONG_16_(var=var):
                            return PyJsComma(var.put('c', (((PyJsBshift(var.put('l', ((((var.get('xl')*var.get('l'))+((Js(32767.0)&var.get('m'))<<Js(15.0)))+var.get('w').get(var.get('j')))+(Js(1073741823.0)&var.get('c')))),Js(30.0))+PyJsBshift(var.get('m'),Js(15.0)))+(var.get('xh')*var.get('h')))+PyJsBshift(var.get('c'),Js(30.0)))),var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (Js(1073741823.0)&var.get('l'))))
                        PyJs_LONG_16_()
                    
                    return var.get('c')
                PyJs_anonymous_15_._set_name('anonymous')
                @Js
                def PyJs_anonymous_17_(i, x, w, j, c, n, this, arguments, var=var):
                    var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
                    var.registers(['w', 'c', 'x', 'j', 'n', 'i', 'v'])
                    #for JS loop
                    
                    while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
                        var.put('v', (((var.get('x')*var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))+var.get('w').get(var.get('j')))+var.get('c')))
                        PyJsComma(var.put('c', var.get('Math').callprop('floor', (var.get('v')/Js(67108864.0)))),var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (Js(67108863.0)&var.get('v'))))
                    
                    return var.get('c')
                PyJs_anonymous_17_._set_name('anonymous')
                @Js
                def PyJs_anonymous_18_(i, x, w, j, c, n, this, arguments, var=var):
                    var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
                    var.registers(['h', 'w', 'xl', 'c', 'l', 'm', 'x', 'j', 'xh', 'n', 'i'])
                    #for JS loop
                    var.put('xl', (Js(16383.0)&var.get('x')))
                    var.put('xh', (var.get('x')>>Js(14.0)))
                    while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
                        var.put('l', (Js(16383.0)&var.get(u"this").get(var.get('i'))))
                        var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(14.0)))
                        var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
                        PyJsComma(var.put('c', (((var.put('l', ((((var.get('xl')*var.get('l'))+((Js(16383.0)&var.get('m'))<<Js(14.0)))+var.get('w').get(var.get('j')))+var.get('c')))>>Js(28.0))+(var.get('m')>>Js(14.0)))+(var.get('xh')*var.get('h')))),var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (Js(268435455.0)&var.get('l'))))
                    
                    return var.get('c')
                PyJs_anonymous_18_._set_name('anonymous')
                return (PyJsComma(var.get('BigInteger').get('prototype').put('am', PyJs_anonymous_15_),var.put('dbits', Js(30.0))) if (Js('Microsoft Internet Explorer')==var.get('navigator').get('appName')) else (PyJsComma(var.get('BigInteger').get('prototype').put('am', PyJs_anonymous_17_),var.put('dbits', Js(26.0))) if (Js('Netscape')!=var.get('navigator').get('appName')) else PyJsComma(var.get('BigInteger').get('prototype').put('am', PyJs_anonymous_18_),var.put('dbits', Js(28.0)))))
            PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_19_(),var.get('BigInteger').get('prototype').put('DB', var.get('dbits'))),var.get('BigInteger').get('prototype').put('DM', ((Js(1.0)<<var.get('dbits'))-Js(1.0)))),var.get('BigInteger').get('prototype').put('DV', (Js(1.0)<<var.get('dbits'))))
            PyJsComma(PyJsComma(var.get('BigInteger').get('prototype').put('FV', var.get('Math').callprop('pow', Js(2.0), Js(52.0))),var.get('BigInteger').get('prototype').put('F1', (Js(52.0)-var.get('dbits')))),var.get('BigInteger').get('prototype').put('F2', ((Js(2.0)*var.get('dbits'))-Js(52.0))))
            var.put('BI_RM', Js('0123456789abcdefghijklmnopqrstuvwxyz'))
            var.put('BI_RC', var.get('Array').create())
            #for JS loop
            PyJsComma(var.put('rr', Js('0').callprop('charCodeAt', Js(0.0))),var.put('vv', Js(0.0)))
            while (var.get('vv')<=Js(9.0)):
                try:
                    var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
                finally:
                        var.put('vv',Js(var.get('vv').to_number())+Js(1))
            #for JS loop
            PyJsComma(var.put('rr', Js('a').callprop('charCodeAt', Js(0.0))),var.put('vv', Js(10.0)))
            while (var.get('vv')<Js(36.0)):
                try:
                    var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
                finally:
                        var.put('vv',Js(var.get('vv').to_number())+Js(1))
            #for JS loop
            PyJsComma(var.put('rr', Js('A').callprop('charCodeAt', Js(0.0))),var.put('vv', Js(10.0)))
            while (var.get('vv')<Js(36.0)):
                try:
                    var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
                finally:
                        var.put('vv',Js(var.get('vv').to_number())+Js(1))
            def PyJs_LONG_65_(var=var):
                @Js
                def PyJs_anonymous_20_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['x'])
                    return (var.get('x').callprop('mod', var.get(u"this").get('m')) if ((var.get('x').get('s')<Js(0.0)) or (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0))) else var.get('x'))
                PyJs_anonymous_20_._set_name('anonymous')
                @Js
                def PyJs_anonymous_21_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['x'])
                    return var.get('x')
                PyJs_anonymous_21_._set_name('anonymous')
                @Js
                def PyJs_anonymous_22_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['x'])
                    var.get('x').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('x'))
                PyJs_anonymous_22_._set_name('anonymous')
                @Js
                def PyJs_anonymous_23_(x, y, r, this, arguments, var=var):
                    var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'y', 'x'])
                    PyJsComma(var.get('x').callprop('multiplyTo', var.get('y'), var.get('r')),var.get(u"this").callprop('reduce', var.get('r')))
                PyJs_anonymous_23_._set_name('anonymous')
                @Js
                def PyJs_anonymous_24_(x, r, this, arguments, var=var):
                    var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'x'])
                    PyJsComma(var.get('x').callprop('squareTo', var.get('r')),var.get(u"this").callprop('reduce', var.get('r')))
                PyJs_anonymous_24_._set_name('anonymous')
                @Js
                def PyJs_anonymous_25_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'x'])
                    var.put('r', var.get('nbi')())
                    def PyJs_LONG_26_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(var.get('x').callprop('abs').callprop('dlShiftTo', var.get(u"this").get('m').get('t'), var.get('r')),var.get('r').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('r'))),(((var.get('x').get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))) and var.get(u"this").get('m').callprop('subTo', var.get('r'), var.get('r')))),var.get('r'))
                    return PyJs_LONG_26_()
                PyJs_anonymous_25_._set_name('anonymous')
                @Js
                def PyJs_anonymous_27_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'x'])
                    var.put('r', var.get('nbi')())
                    return PyJsComma(PyJsComma(var.get('x').callprop('copyTo', var.get('r')),var.get(u"this").callprop('reduce', var.get('r'))),var.get('r'))
                PyJs_anonymous_27_._set_name('anonymous')
                @Js
                def PyJs_anonymous_28_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['u0', 'i', 'x', 'j'])
                    #for JS loop
                    
                    while (var.get('x').get('t')<=var.get(u"this").get('mt2')):
                        var.get('x').put((var.get('x').put('t',Js(var.get('x').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
                    
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get(u"this").get('m').get('t')):
                        try:
                            var.put('j', (Js(32767.0)&var.get('x').get(var.get('i'))))
                            var.put('u0', (((var.get('j')*var.get(u"this").get('mpl'))+((((var.get('j')*var.get(u"this").get('mph'))+((var.get('x').get(var.get('i'))>>Js(15.0))*var.get(u"this").get('mpl')))&var.get(u"this").get('um'))<<Js(15.0)))&var.get('x').get('DM')))
                            #for JS loop
                            var.get('x').put(var.put('j', (var.get('i')+var.get(u"this").get('m').get('t'))), var.get(u"this").get('m').callprop('am', Js(0.0), var.get('u0'), var.get('x'), var.get('i'), Js(0.0), var.get(u"this").get('m').get('t')), '+')
                            while (var.get('x').get(var.get('j'))>=var.get('x').get('DV')):
                                PyJsComma(var.get('x').put(var.get('j'), var.get('x').get('DV'), '-'),(var.get('x').put(var.put('j',Js(var.get('j').to_number())+Js(1)),Js(var.get('x').get(var.put('j',Js(var.get('j').to_number())+Js(1))).to_number())+Js(1))-Js(1)))
                            
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    PyJsComma(PyJsComma(var.get('x').callprop('clamp'),var.get('x').callprop('drShiftTo', var.get(u"this").get('m').get('t'), var.get('x'))),((var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)) and var.get('x').callprop('subTo', var.get(u"this").get('m'), var.get('x'))))
                PyJs_anonymous_28_._set_name('anonymous')
                @Js
                def PyJs_anonymous_29_(x, y, r, this, arguments, var=var):
                    var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'y', 'x'])
                    PyJsComma(var.get('x').callprop('multiplyTo', var.get('y'), var.get('r')),var.get(u"this").callprop('reduce', var.get('r')))
                PyJs_anonymous_29_._set_name('anonymous')
                @Js
                def PyJs_anonymous_30_(x, r, this, arguments, var=var):
                    var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'x'])
                    PyJsComma(var.get('x').callprop('squareTo', var.get('r')),var.get(u"this").callprop('reduce', var.get('r')))
                PyJs_anonymous_30_._set_name('anonymous')
                @Js
                def PyJs_anonymous_31_(r, this, arguments, var=var):
                    var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'i'])
                    #for JS loop
                    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.get('r').put(var.get('i'), var.get(u"this").get(var.get('i')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                    PyJsComma(var.get('r').put('t', var.get(u"this").get('t')),var.get('r').put('s', var.get(u"this").get('s')))
                PyJs_anonymous_31_._set_name('anonymous')
                @Js
                def PyJs_anonymous_32_(x, this, arguments, var=var):
                    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                    var.registers(['x'])
                    PyJsComma(PyJsComma(var.get(u"this").put('t', Js(1.0)),var.get(u"this").put('s', ((-Js(1.0)) if (var.get('x')<Js(0.0)) else Js(0.0)))),(var.get(u"this").put('0', var.get('x')) if (var.get('x')>Js(0.0)) else (var.get(u"this").put('0', (var.get('x')+var.get(u"this").get('DV'))) if (var.get('x')<(-Js(1.0))) else var.get(u"this").put('t', Js(0.0)))))
                PyJs_anonymous_32_._set_name('anonymous')
                @Js
                def PyJs_anonymous_33_(s, b, this, arguments, var=var):
                    var = Scope({'s':s, 'b':b, 'this':this, 'arguments':arguments}, var)
                    var.registers(['k', 's', 'b', 'x', 'sh', 'i', 'mi'])
                    pass
                    if (Js(16.0)==var.get('b')):
                        var.put('k', Js(4.0))
                    else:
                        if (Js(8.0)==var.get('b')):
                            var.put('k', Js(3.0))
                        else:
                            if (Js(256.0)==var.get('b')):
                                var.put('k', Js(8.0))
                            else:
                                if (Js(2.0)==var.get('b')):
                                    var.put('k', Js(1.0))
                                else:
                                    if (Js(32.0)==var.get('b')):
                                        var.put('k', Js(5.0))
                                    else:
                                        if (Js(4.0)!=var.get('b')):
                                            return PyJsComma(var.get(u"this").callprop('fromRadix', var.get('s'), var.get('b')), Js(None))
                                        var.put('k', Js(2.0))
                    PyJsComma(var.get(u"this").put('t', Js(0.0)),var.get(u"this").put('s', Js(0.0)))
                    #for JS loop
                    var.put('i', var.get('s').get('length'))
                    var.put('mi', Js(1.0).neg())
                    var.put('sh', Js(0.0))
                    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                        var.put('x', ((Js(255.0)&var.get('s').get(var.get('i'))) if (Js(8.0)==var.get('k')) else var.get('intAt')(var.get('s'), var.get('i'))))
                        def PyJs_LONG_35_(var=var):
                            def PyJs_LONG_34_(var=var):
                                return (PyJsComma(var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), ((var.get('x')&((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0)))<<var.get('sh')), '|'),var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), (var.get('x')>>(var.get(u"this").get('DB')-var.get('sh'))))) if ((var.get('sh')+var.get('k'))>var.get(u"this").get('DB')) else var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (var.get('x')<<var.get('sh')), '|'))
                            return (((Js('-')==var.get('s').callprop('charAt', var.get('i'))) and var.put('mi', Js(0.0).neg())) if (var.get('x')<Js(0.0)) else PyJsComma(PyJsComma(var.put('mi', Js(1.0).neg()),(var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), var.get('x')) if (Js(0.0)==var.get('sh')) else PyJs_LONG_34_())),((var.put('sh', var.get('k'), '+')>=var.get(u"this").get('DB')) and var.put('sh', var.get(u"this").get('DB'), '-'))))
                        PyJs_LONG_35_()
                    
                    def PyJs_LONG_36_(var=var):
                        return PyJsComma(PyJsComma((((Js(8.0)==var.get('k')) and (Js(0.0)!=(Js(128.0)&var.get('s').get('0')))) and PyJsComma(var.get(u"this").put('s', (-Js(1.0))),((var.get('sh')>Js(0.0)) and var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0))<<var.get('sh')), '|')))),var.get(u"this").callprop('clamp')),(var.get('mi') and var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))))
                    PyJs_LONG_36_()
                PyJs_anonymous_33_._set_name('anonymous')
                @Js
                def PyJs_anonymous_37_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['c'])
                    #for JS loop
                    var.put('c', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
                    while ((var.get(u"this").get('t')>Js(0.0)) and (var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))==var.get('c'))):
                        var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())-Js(1))
                    
                PyJs_anonymous_37_._set_name('anonymous')
                @Js
                def PyJs_anonymous_38_(n, r, this, arguments, var=var):
                    var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'n', 'i'])
                    pass
                    #for JS loop
                    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.get('r').put((var.get('i')+var.get('n')), var.get(u"this").get(var.get('i')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                    #for JS loop
                    var.put('i', (var.get('n')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.get('r').put(var.get('i'), Js(0.0))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                    PyJsComma(var.get('r').put('t', (var.get(u"this").get('t')+var.get('n'))),var.get('r').put('s', var.get(u"this").get('s')))
                PyJs_anonymous_38_._set_name('anonymous')
                @Js
                def PyJs_anonymous_39_(n, r, this, arguments, var=var):
                    var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'n', 'i'])
                    #for JS loop
                    var.put('i', var.get('n'))
                    while (var.get('i')<var.get(u"this").get('t')):
                        try:
                            var.get('r').put((var.get('i')-var.get('n')), var.get(u"this").get(var.get('i')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    PyJsComma(var.get('r').put('t', var.get('Math').callprop('max', (var.get(u"this").get('t')-var.get('n')), Js(0.0))),var.get('r').put('s', var.get(u"this").get('s')))
                PyJs_anonymous_39_._set_name('anonymous')
                @Js
                def PyJs_anonymous_40_(n, r, this, arguments, var=var):
                    var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['bs', 'cbs', 'c', 'ds', 'bm', 'r', 'n', 'i'])
                    var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
                    var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
                    var.put('bm', ((Js(1.0)<<var.get('cbs'))-Js(1.0)))
                    var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
                    var.put('c', ((var.get(u"this").get('s')<<var.get('bs'))&var.get(u"this").get('DM')))
                    #for JS loop
                    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            PyJsComma(var.get('r').put(((var.get('i')+var.get('ds'))+Js(1.0)), ((var.get(u"this").get(var.get('i'))>>var.get('cbs'))|var.get('c'))),var.put('c', ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('bs'))))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                    #for JS loop
                    var.put('i', (var.get('ds')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.get('r').put(var.get('i'), Js(0.0))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                    PyJsComma(PyJsComma(PyJsComma(var.get('r').put(var.get('ds'), var.get('c')),var.get('r').put('t', ((var.get(u"this").get('t')+var.get('ds'))+Js(1.0)))),var.get('r').put('s', var.get(u"this").get('s'))),var.get('r').callprop('clamp'))
                PyJs_anonymous_40_._set_name('anonymous')
                @Js
                def PyJs_anonymous_41_(n, r, this, arguments, var=var):
                    var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['bs', 'cbs', 'ds', 'bm', 'r', 'n', 'i'])
                    var.get('r').put('s', var.get(u"this").get('s'))
                    var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
                    if (var.get('ds')>=var.get(u"this").get('t')):
                        var.get('r').put('t', Js(0.0))
                    else:
                        var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
                        var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
                        var.put('bm', ((Js(1.0)<<var.get('bs'))-Js(1.0)))
                        var.get('r').put('0', (var.get(u"this").get(var.get('ds'))>>var.get('bs')))
                        #for JS loop
                        var.put('i', (var.get('ds')+Js(1.0)))
                        while (var.get('i')<var.get(u"this").get('t')):
                            try:
                                PyJsComma(var.get('r').put(((var.get('i')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('cbs')), '|'),var.get('r').put((var.get('i')-var.get('ds')), (var.get(u"this").get(var.get('i'))>>var.get('bs'))))
                            finally:
                                    var.put('i',Js(var.get('i').to_number())+Js(1))
                        PyJsComma(PyJsComma(((var.get('bs')>Js(0.0)) and var.get('r').put(((var.get(u"this").get('t')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get('s')&var.get('bm'))<<var.get('cbs')), '|')),var.get('r').put('t', (var.get(u"this").get('t')-var.get('ds')))),var.get('r').callprop('clamp'))
                PyJs_anonymous_41_._set_name('anonymous')
                @Js
                def PyJs_anonymous_42_(a, r, this, arguments, var=var):
                    var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['c', 'm', 'r', 'i', 'a'])
                    #for JS loop
                    var.put('i', Js(0.0))
                    var.put('c', Js(0.0))
                    var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
                    while (var.get('i')<var.get('m')):
                        PyJsComma(PyJsComma(var.put('c', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))), '+'),var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))),var.put('c', var.get(u"this").get('DB'), '>>'))
                    
                    if (var.get('a').get('t')<var.get(u"this").get('t')):
                        #for JS loop
                        var.put('c', var.get('a').get('s'), '-')
                        while (var.get('i')<var.get(u"this").get('t')):
                            PyJsComma(PyJsComma(var.put('c', var.get(u"this").get(var.get('i')), '+'),var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))),var.put('c', var.get(u"this").get('DB'), '>>'))
                        
                        var.put('c', var.get(u"this").get('s'), '+')
                    else:
                        #for JS loop
                        var.put('c', var.get(u"this").get('s'), '+')
                        while (var.get('i')<var.get('a').get('t')):
                            PyJsComma(PyJsComma(var.put('c', var.get('a').get(var.get('i')), '-'),var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))),var.put('c', var.get(u"this").get('DB'), '>>'))
                        
                        var.put('c', var.get('a').get('s'), '-')
                    def PyJs_LONG_43_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(var.get('r').put('s', ((-Js(1.0)) if (var.get('c')<Js(0.0)) else Js(0.0))),(var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('c'))) if (var.get('c')<(-Js(1.0))) else ((var.get('c')>Js(0.0)) and var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), var.get('c'))))),var.get('r').put('t', var.get('i'))),var.get('r').callprop('clamp'))
                    PyJs_LONG_43_()
                PyJs_anonymous_42_._set_name('anonymous')
                @Js
                def PyJs_anonymous_44_(a, r, this, arguments, var=var):
                    var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['y', 'x', 'r', 'i', 'a'])
                    var.put('x', var.get(u"this").callprop('abs'))
                    var.put('y', var.get('a').callprop('abs'))
                    var.put('i', var.get('x').get('t'))
                    #for JS loop
                    var.get('r').put('t', (var.get('i')+var.get('y').get('t')))
                    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                        var.get('r').put(var.get('i'), Js(0.0))
                    
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('y').get('t')):
                        try:
                            var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', Js(0.0), var.get('y').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), var.get('x').get('t')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    PyJsComma(PyJsComma(var.get('r').put('s', Js(0.0)),var.get('r').callprop('clamp')),((var.get(u"this").get('s')!=var.get('a').get('s')) and var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))))
                PyJs_anonymous_44_._set_name('anonymous')
                @Js
                def PyJs_anonymous_45_(r, this, arguments, var=var):
                    var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'c', 'i', 'x'])
                    #for JS loop
                    var.put('x', var.get(u"this").callprop('abs'))
                    var.put('i', var.get('r').put('t', (Js(2.0)*var.get('x').get('t'))))
                    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                        var.get('r').put(var.get('i'), Js(0.0))
                    
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<(var.get('x').get('t')-Js(1.0))):
                        try:
                            var.put('c', var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)))
                            def PyJs_LONG_46_(var=var):
                                return ((var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', (var.get('i')+Js(1.0)), (Js(2.0)*var.get('x').get(var.get('i'))), var.get('r'), ((Js(2.0)*var.get('i'))+Js(1.0)), var.get('c'), ((var.get('x').get('t')-var.get('i'))-Js(1.0))), '+')>=var.get('x').get('DV')) and PyJsComma(var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').get('DV'), '-'),var.get('r').put(((var.get('i')+var.get('x').get('t'))+Js(1.0)), Js(1.0))))
                            PyJs_LONG_46_()
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    PyJsComma(PyJsComma(((var.get('r').get('t')>Js(0.0)) and var.get('r').put((var.get('r').get('t')-Js(1.0)), var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)), '+')),var.get('r').put('s', Js(0.0))),var.get('r').callprop('clamp'))
                PyJs_anonymous_45_._set_name('anonymous')
                @Js
                def PyJs_anonymous_47_(m, q, r, this, arguments, var=var):
                    var = Scope({'m':m, 'q':q, 'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['ms', 'ys', 'pm', 'm', 'y0', 't', 'd2', 'pt', 'd1', 'y', 'q', 'ts', 'yt', 'r', 'i', 'qd', 'nsh', 'e', 'j'])
                    var.put('pm', var.get('m').callprop('abs'))
                    if (var.get('pm').get('t')<=Js(0.0)).neg():
                        var.put('pt', var.get(u"this").callprop('abs'))
                        if (var.get('pt').get('t')<var.get('pm').get('t')):
                            return PyJsComma(((var.get(u"null")!=var.get('q')) and var.get('q').callprop('fromInt', Js(0.0))),PyJsComma(((var.get(u"null")!=var.get('r')) and var.get(u"this").callprop('copyTo', var.get('r'))), Js(None)))
                        ((var.get(u"null")==var.get('r')) and var.put('r', var.get('nbi')()))
                        var.put('y', var.get('nbi')())
                        var.put('ts', var.get(u"this").get('s'))
                        var.put('ms', var.get('m').get('s'))
                        var.put('nsh', (var.get(u"this").get('DB')-var.get('nbits')(var.get('pm').get((var.get('pm').get('t')-Js(1.0))))))
                        (PyJsComma(var.get('pm').callprop('lShiftTo', var.get('nsh'), var.get('y')),var.get('pt').callprop('lShiftTo', var.get('nsh'), var.get('r'))) if (var.get('nsh')>Js(0.0)) else PyJsComma(var.get('pm').callprop('copyTo', var.get('y')),var.get('pt').callprop('copyTo', var.get('r'))))
                        var.put('ys', var.get('y').get('t'))
                        var.put('y0', var.get('y').get((var.get('ys')-Js(1.0))))
                        if (Js(0.0)!=var.get('y0')):
                            var.put('yt', ((var.get('y0')*(Js(1.0)<<var.get(u"this").get('F1')))+((var.get('y').get((var.get('ys')-Js(2.0)))>>var.get(u"this").get('F2')) if (var.get('ys')>Js(1.0)) else Js(0.0))))
                            var.put('d1', (var.get(u"this").get('FV')/var.get('yt')))
                            var.put('d2', ((Js(1.0)<<var.get(u"this").get('F1'))/var.get('yt')))
                            var.put('e', (Js(1.0)<<var.get(u"this").get('F2')))
                            var.put('i', var.get('r').get('t'))
                            var.put('j', (var.get('i')-var.get('ys')))
                            var.put('t', (var.get('nbi')() if (var.get(u"null")==var.get('q')) else var.get('q')))
                            #for JS loop
                            def PyJs_LONG_48_(var=var):
                                return PyJsComma(PyJsComma(PyJsComma(var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t')),((var.get('r').callprop('compareTo', var.get('t'))>=Js(0.0)) and PyJsComma(var.get('r').put((var.get('r').put('t',Js(var.get('r').get('t').to_number())+Js(1))-Js(1)), Js(1.0)),var.get('r').callprop('subTo', var.get('t'), var.get('r'))))),var.get('BigInteger').get('ONE').callprop('dlShiftTo', var.get('ys'), var.get('t'))),var.get('t').callprop('subTo', var.get('y'), var.get('y')))
                            PyJs_LONG_48_()
                            while (var.get('y').get('t')<var.get('ys')):
                                var.get('y').put((var.get('y').put('t',Js(var.get('y').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
                            
                            #for JS loop
                            
                            while (var.put('j',Js(var.get('j').to_number())-Js(1))>=Js(0.0)):
                                var.put('qd', (var.get(u"this").get('DM') if (var.get('r').get(var.put('i',Js(var.get('i').to_number())-Js(1)))==var.get('y0')) else var.get('Math').callprop('floor', ((var.get('r').get(var.get('i'))*var.get('d1'))+((var.get('r').get((var.get('i')-Js(1.0)))+var.get('e'))*var.get('d2'))))))
                                if (var.get('r').put(var.get('i'), var.get('y').callprop('am', Js(0.0), var.get('qd'), var.get('r'), var.get('j'), Js(0.0), var.get('ys')), '+')<var.get('qd')):
                                    #for JS loop
                                    PyJsComma(var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t')),var.get('r').callprop('subTo', var.get('t'), var.get('r')))
                                    while (var.get('r').get(var.get('i'))<var.put('qd',Js(var.get('qd').to_number())-Js(1))):
                                        var.get('r').callprop('subTo', var.get('t'), var.get('r'))
                                    
                            
                            def PyJs_LONG_49_(var=var):
                                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get(u"null")!=var.get('q')) and PyJsComma(var.get('r').callprop('drShiftTo', var.get('ys'), var.get('q')),((var.get('ts')!=var.get('ms')) and var.get('BigInteger').get('ZERO').callprop('subTo', var.get('q'), var.get('q'))))),var.get('r').put('t', var.get('ys'))),var.get('r').callprop('clamp')),((var.get('nsh')>Js(0.0)) and var.get('r').callprop('rShiftTo', var.get('nsh'), var.get('r')))),((var.get('ts')<Js(0.0)) and var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))))
                            PyJs_LONG_49_()
                PyJs_anonymous_47_._set_name('anonymous')
                @Js
                def PyJs_anonymous_50_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['y', 'x'])
                    if (var.get(u"this").get('t')<Js(1.0)):
                        return Js(0.0)
                    var.put('x', var.get(u"this").get('0'))
                    if (Js(0.0)==(Js(1.0)&var.get('x'))):
                        return Js(0.0)
                    var.put('y', (Js(3.0)&var.get('x')))
                    def PyJs_LONG_51_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(var.put('y', ((var.get('y')*(Js(2.0)-((Js(15.0)&var.get('x'))*var.get('y'))))&Js(15.0))),var.put('y', ((var.get('y')*(Js(2.0)-((Js(255.0)&var.get('x'))*var.get('y'))))&Js(255.0)))),var.put('y', ((var.get('y')*(Js(2.0)-(((Js(65535.0)&var.get('x'))*var.get('y'))&Js(65535.0))))&Js(65535.0)))),((var.get(u"this").get('DV')-var.get('y')) if (var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')*var.get('y'))%var.get(u"this").get('DV'))))%var.get(u"this").get('DV')))>Js(0.0)) else (-var.get('y'))))
                    return PyJs_LONG_51_()
                PyJs_anonymous_50_._set_name('anonymous')
                @Js
                def PyJs_anonymous_52_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return (Js(0.0)==((Js(1.0)&var.get(u"this").get('0')) if (var.get(u"this").get('t')>Js(0.0)) else var.get(u"this").get('s')))
                PyJs_anonymous_52_._set_name('anonymous')
                @Js
                def PyJs_anonymous_53_(e, z, this, arguments, var=var):
                    var = Scope({'e':e, 'z':z, 'this':this, 'arguments':arguments}, var)
                    var.registers(['g', 'r2', 'z', 'e', 'r', 'i', 't'])
                    if ((var.get('e')>Js(4294967295.0)) or (var.get('e')<Js(1.0))):
                        return var.get('BigInteger').get('ONE')
                    var.put('r', var.get('nbi')())
                    var.put('r2', var.get('nbi')())
                    var.put('g', var.get('z').callprop('convert', var.get(u"this")))
                    var.put('i', (var.get('nbits')(var.get('e'))-Js(1.0)))
                    #for JS loop
                    var.get('g').callprop('copyTo', var.get('r'))
                    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                        if PyJsComma(var.get('z').callprop('sqrTo', var.get('r'), var.get('r2')),((var.get('e')&(Js(1.0)<<var.get('i')))>Js(0.0))):
                            var.get('z').callprop('mulTo', var.get('r2'), var.get('g'), var.get('r'))
                        else:
                            var.put('t', var.get('r'))
                            PyJsComma(var.put('r', var.get('r2')),var.put('r2', var.get('t')))
                    
                    return var.get('z').callprop('revert', var.get('r'))
                PyJs_anonymous_53_._set_name('anonymous')
                @Js
                def PyJs_anonymous_54_(b, this, arguments, var=var):
                    var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
                    var.registers(['k', 'km', 'd', 'b', 'm', 'p', 'r', 'i'])
                    if (var.get(u"this").get('s')<Js(0.0)):
                        return (Js('-')+var.get(u"this").callprop('negate').callprop('toString', var.get('b')))
                    pass
                    if (Js(16.0)==var.get('b')):
                        var.put('k', Js(4.0))
                    else:
                        if (Js(8.0)==var.get('b')):
                            var.put('k', Js(3.0))
                        else:
                            if (Js(2.0)==var.get('b')):
                                var.put('k', Js(1.0))
                            else:
                                if (Js(32.0)==var.get('b')):
                                    var.put('k', Js(5.0))
                                else:
                                    if (Js(4.0)!=var.get('b')):
                                        return var.get(u"this").callprop('toRadix', var.get('b'))
                                    var.put('k', Js(2.0))
                    var.put('km', ((Js(1.0)<<var.get('k'))-Js(1.0)))
                    var.put('m', Js(1.0).neg())
                    var.put('r', Js(''))
                    var.put('i', var.get(u"this").get('t'))
                    var.put('p', (var.get(u"this").get('DB')-((var.get('i')*var.get(u"this").get('DB'))%var.get('k'))))
                    if ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                        #for JS loop
                        (((var.get('p')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('i'))>>var.get('p')))>Js(0.0))) and PyJsComma(var.put('m', Js(0.0).neg()),var.put('r', var.get('int2char')(var.get('d')))))
                        while (var.get('i')>=Js(0.0)):
                            def PyJs_LONG_55_(var=var):
                                return (PyJsComma(var.put('d', ((var.get(u"this").get(var.get('i'))&((Js(1.0)<<var.get('p'))-Js(1.0)))<<(var.get('k')-var.get('p')))),var.put('d', (var.get(u"this").get(var.put('i',Js(var.get('i').to_number())-Js(1)))>>var.put('p', (var.get(u"this").get('DB')-var.get('k')), '+')), '|')) if (var.get('p')<var.get('k')) else PyJsComma(var.put('d', ((var.get(u"this").get(var.get('i'))>>var.put('p', var.get('k'), '-'))&var.get('km'))),((var.get('p')<=Js(0.0)) and PyJsComma(var.put('p', var.get(u"this").get('DB'), '+'),var.put('i',Js(var.get('i').to_number())-Js(1))))))
                            PyJsComma(PyJsComma(PyJs_LONG_55_(),((var.get('d')>Js(0.0)) and var.put('m', Js(0.0).neg()))),(var.get('m') and var.put('r', var.get('int2char')(var.get('d')), '+')))
                        
                    return (var.get('r') if var.get('m') else Js('0'))
                PyJs_anonymous_54_._set_name('anonymous')
                @Js
                def PyJs_anonymous_56_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['r'])
                    var.put('r', var.get('nbi')())
                    return PyJsComma(var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get('r')),var.get('r'))
                PyJs_anonymous_56_._set_name('anonymous')
                @Js
                def PyJs_anonymous_57_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this"))
                PyJs_anonymous_57_._set_name('anonymous')
                @Js
                def PyJs_anonymous_58_(a, this, arguments, var=var):
                    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'i', 'a'])
                    var.put('r', (var.get(u"this").get('s')-var.get('a').get('s')))
                    if (Js(0.0)!=var.get('r')):
                        return var.get('r')
                    var.put('i', var.get(u"this").get('t'))
                    if (Js(0.0)!=var.put('r', (var.get('i')-var.get('a').get('t')))):
                        return ((-var.get('r')) if (var.get(u"this").get('s')<Js(0.0)) else var.get('r'))
                    #for JS loop
                    
                    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                        if (Js(0.0)!=var.put('r', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))))):
                            return var.get('r')
                    
                    return Js(0.0)
                PyJs_anonymous_58_._set_name('anonymous')
                @Js
                def PyJs_anonymous_59_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    return (Js(0.0) if (var.get(u"this").get('t')<=Js(0.0)) else ((var.get(u"this").get('DB')*(var.get(u"this").get('t')-Js(1.0)))+var.get('nbits')((var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))^(var.get(u"this").get('s')&var.get(u"this").get('DM'))))))
                PyJs_anonymous_59_._set_name('anonymous')
                @Js
                def PyJs_anonymous_60_(a, this, arguments, var=var):
                    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
                    var.registers(['r', 'a'])
                    var.put('r', var.get('nbi')())
                    return PyJsComma(PyJsComma(var.get(u"this").callprop('abs').callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('r')),(((var.get(u"this").get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))) and var.get('a').callprop('subTo', var.get('r'), var.get('r')))),var.get('r'))
                PyJs_anonymous_60_._set_name('anonymous')
                @Js
                def PyJs_anonymous_61_(e, m, this, arguments, var=var):
                    var = Scope({'e':e, 'm':m, 'this':this, 'arguments':arguments}, var)
                    var.registers(['z', 'm', 'e'])
                    pass
                    return PyJsComma(var.put('z', (var.get('Classic').create(var.get('m')) if ((var.get('e')<Js(256.0)) or var.get('m').callprop('isEven')) else var.get('Montgomery').create(var.get('m')))),var.get(u"this").callprop('exp', var.get('e'), var.get('z')))
                PyJs_anonymous_61_._set_name('anonymous')
                @Js
                def PyJs_anonymous_62_(key, this, arguments, var=var):
                    var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
                    var.registers(['key', 'i', 't', 'j'])
                    pass
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<Js(256.0)):
                        try:
                            var.get(u"this").get('S').put(var.get('i'), var.get('i'))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    #for JS loop
                    PyJsComma(var.put('j', Js(0.0)),var.put('i', Js(0.0)))
                    while (var.get('i')<Js(256.0)):
                        try:
                            PyJsComma(PyJsComma(PyJsComma(var.put('j', (((var.get('j')+var.get(u"this").get('S').get(var.get('i')))+var.get('key').get((var.get('i')%var.get('key').get('length'))))&Js(255.0))),var.put('t', var.get(u"this").get('S').get(var.get('i')))),var.get(u"this").get('S').put(var.get('i'), var.get(u"this").get('S').get(var.get('j')))),var.get(u"this").get('S').put(var.get('j'), var.get('t')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    PyJsComma(var.get(u"this").put('i', Js(0.0)),var.get(u"this").put('j', Js(0.0)))
                PyJs_anonymous_62_._set_name('anonymous')
                @Js
                def PyJs_anonymous_63_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['t'])
                    pass
                    def PyJs_LONG_64_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get(u"this").put('i', ((var.get(u"this").get('i')+Js(1.0))&Js(255.0))),var.get(u"this").put('j', ((var.get(u"this").get('j')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))),var.put('t', var.get(u"this").get('S').get(var.get(u"this").get('i')))),var.get(u"this").get('S').put(var.get(u"this").get('i'), var.get(u"this").get('S').get(var.get(u"this").get('j')))),var.get(u"this").get('S').put(var.get(u"this").get('j'), var.get('t'))),var.get(u"this").get('S').get(((var.get('t')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0))))
                    return PyJs_LONG_64_()
                PyJs_anonymous_63_._set_name('anonymous')
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('Classic').get('prototype').put('convert', PyJs_anonymous_20_),var.get('Classic').get('prototype').put('revert', PyJs_anonymous_21_)),var.get('Classic').get('prototype').put('reduce', PyJs_anonymous_22_)),var.get('Classic').get('prototype').put('mulTo', PyJs_anonymous_23_)),var.get('Classic').get('prototype').put('sqrTo', PyJs_anonymous_24_)),var.get('Montgomery').get('prototype').put('convert', PyJs_anonymous_25_)),var.get('Montgomery').get('prototype').put('revert', PyJs_anonymous_27_)),var.get('Montgomery').get('prototype').put('reduce', PyJs_anonymous_28_)),var.get('Montgomery').get('prototype').put('mulTo', PyJs_anonymous_29_)),var.get('Montgomery').get('prototype').put('sqrTo', PyJs_anonymous_30_)),var.get('BigInteger').get('prototype').put('copyTo', PyJs_anonymous_31_)),var.get('BigInteger').get('prototype').put('fromInt', PyJs_anonymous_32_)),var.get('BigInteger').get('prototype').put('fromString', PyJs_anonymous_33_)),var.get('BigInteger').get('prototype').put('clamp', PyJs_anonymous_37_)),var.get('BigInteger').get('prototype').put('dlShiftTo', PyJs_anonymous_38_)),var.get('BigInteger').get('prototype').put('drShiftTo', PyJs_anonymous_39_)),var.get('BigInteger').get('prototype').put('lShiftTo', PyJs_anonymous_40_)),var.get('BigInteger').get('prototype').put('rShiftTo', PyJs_anonymous_41_)),var.get('BigInteger').get('prototype').put('subTo', PyJs_anonymous_42_)),var.get('BigInteger').get('prototype').put('multiplyTo', PyJs_anonymous_44_)),var.get('BigInteger').get('prototype').put('squareTo', PyJs_anonymous_45_)),var.get('BigInteger').get('prototype').put('divRemTo', PyJs_anonymous_47_)),var.get('BigInteger').get('prototype').put('invDigit', PyJs_anonymous_50_)),var.get('BigInteger').get('prototype').put('isEven', PyJs_anonymous_52_)),var.get('BigInteger').get('prototype').put('exp', PyJs_anonymous_53_)),var.get('BigInteger').get('prototype').put('toString', PyJs_anonymous_54_)),var.get('BigInteger').get('prototype').put('negate', PyJs_anonymous_56_)),var.get('BigInteger').get('prototype').put('abs', PyJs_anonymous_57_)),var.get('BigInteger').get('prototype').put('compareTo', PyJs_anonymous_58_)),var.get('BigInteger').get('prototype').put('bitLength', PyJs_anonymous_59_)),var.get('BigInteger').get('prototype').put('mod', PyJs_anonymous_60_)),var.get('BigInteger').get('prototype').put('modPowInt', PyJs_anonymous_61_)),var.get('BigInteger').put('ZERO', var.get('nbv')(Js(0.0)))),var.get('BigInteger').put('ONE', var.get('nbv')(Js(1.0)))),var.get('Arcfour').get('prototype').put('init', PyJs_anonymous_62_)),var.get('Arcfour').get('prototype').put('next', PyJs_anonymous_63_))
            PyJs_LONG_65_()
            var.put('rng_psize', Js(256.0))
            if (var.get(u"null")==var.get('rng_pool')):
                PyJsComma(var.put('rng_pool', var.get('Array').create()),var.put('rng_pptr', Js(0.0)))
                pass
                if (var.get('window').get('crypto') and var.get('window').get('crypto').get('getRandomValues')):
                    var.put('ua', var.get('Uint8Array').create(Js(32.0)))
                    #for JS loop
                    PyJsComma(var.get('window').get('crypto').callprop('getRandomValues', var.get('ua')),var.put('t', Js(0.0)))
                    while (var.get('t')<Js(32.0)):
                        try:
                            var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), var.get('ua').get(var.get('t')))
                        finally:
                                var.put('t',Js(var.get('t').to_number())+Js(1))
                if (((Js('Netscape')==var.get('navigator').get('appName')) and (var.get('navigator').get('appVersion')<Js('5'))) and var.get('window').get('crypto')):
                    var.put('z', var.get('window').get('crypto').callprop('random', Js(32.0)))
                    #for JS loop
                    var.put('t', Js(0.0))
                    while (var.get('t')<var.get('z').get('length')):
                        try:
                            var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (Js(255.0)&var.get('z').callprop('charCodeAt', var.get('t'))))
                        finally:
                                var.put('t',Js(var.get('t').to_number())+Js(1))
                #for JS loop
                
                while (var.get('rng_pptr')<var.get('rng_psize')):
                    PyJsComma(PyJsComma(var.put('t', var.get('Math').callprop('floor', (Js(65536.0)*var.get('Math').callprop('random')))),var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), PyJsBshift(var.get('t'),Js(8.0)))),var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (Js(255.0)&var.get('t'))))
                
                PyJsComma(var.put('rng_pptr', Js(0.0)),var.get('rng_seed_time')())
            @Js
            def PyJs_anonymous_66_(ba, this, arguments, var=var):
                var = Scope({'ba':ba, 'this':this, 'arguments':arguments}, var)
                var.registers(['ba', 'i'])
                pass
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('ba').get('length')):
                    try:
                        var.get('ba').put(var.get('i'), var.get('rng_get_byte')())
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
            PyJs_anonymous_66_._set_name('anonymous')
            @Js
            def PyJs_anonymous_67_(x, this, arguments, var=var):
                var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                var.registers(['x'])
                return var.get('x').callprop('modPowInt', var.get(u"this").get('e'), var.get(u"this").get('n'))
            PyJs_anonymous_67_._set_name('anonymous')
            @Js
            def PyJs_anonymous_68_(N, E, this, arguments, var=var):
                var = Scope({'N':N, 'E':E, 'this':this, 'arguments':arguments}, var)
                var.registers(['E', 'N'])
                (PyJsComma(var.get(u"this").put('n', var.get('parseBigInt')(var.get('N'), Js(16.0))),var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))) if ((((var.get(u"null")!=var.get('N')) and (var.get(u"null")!=var.get('E'))) and (var.get('N').get('length')>Js(0.0))) and (var.get('E').get('length')>Js(0.0))) else var.get('alert')(Js('Invalid RSA public key')))
            PyJs_anonymous_68_._set_name('anonymous')
            @Js
            def PyJs_anonymous_69_(text, this, arguments, var=var):
                var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
                var.registers(['m', 'c', 'text', 'h'])
                var.put('m', var.get('pkcs1pad2')(var.get('text'), ((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0))))
                if (var.get(u"null")==var.get('m')):
                    return var.get(u"null")
                var.put('c', var.get(u"this").callprop('doPublic', var.get('m')))
                if (var.get(u"null")==var.get('c')):
                    return var.get(u"null")
                var.put('h', var.get('c').callprop('toString', Js(16.0)))
                return (var.get('h') if (Js(0.0)==(Js(1.0)&var.get('h').get('length'))) else (Js('0')+var.get('h')))
            PyJs_anonymous_69_._set_name('anonymous')
            PyJsComma(PyJsComma(PyJsComma(var.get('SecureRandom').get('prototype').put('nextBytes', PyJs_anonymous_66_),var.get('RSAKey').get('prototype').put('doPublic', PyJs_anonymous_67_)),var.get('RSAKey').get('prototype').put('setPublic', PyJs_anonymous_68_)),var.get('RSAKey').get('prototype').put('encrypt', PyJs_anonymous_69_))
            var.put('rsaObj', var.get('RSAKey').create())
            var.put('n', var.get('nn'))
            var.put('e', var.get('ee'))
            var.get('rsaObj').callprop('setPublic', var.get('n'), var.get('e'))
            var.put('result', var.get('rsaObj').callprop('encrypt', var.get('val')))
            if (Js(256.0)!=var.get('result').get('length')):
                #for JS loop
                var.put('l', var.get('Math').callprop('abs', (Js(256.0)-var.get('result').get('length'))))
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('l')):
                    try:
                        var.put('result', (Js('0')+var.get('result')))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('result')
        PyJs_anonymous_8_._set_name('anonymous')
        @Js
        def PyJs_anonymous_70_(key, message, encrypt, mode, iv, padding, this, arguments, var=var):
            var = Scope({'key':key, 'message':message, 'encrypt':encrypt, 'mode':mode, 'iv':iv, 'padding':padding, 'this':this, 'arguments':arguments}, var)
            var.registers(['loopinc', 'iv', 'm', 'keys', 'padding', 'cbcright', 'spfunction4', 'len', 'right1', 'endloop', 'spfunction5', 'spfunction8', 'result', 'cbcright2', 'message', 'chunk', 'cbcleft', 'cbcleft2', 'spfunction6', 'left', 'mode', 'encrypt', 'iterations', 'right2', 'spfunction3', 'spfunction2', 'i', 'paddingChars', 'temp', 'looping', 'spfunction1', 'tempresult', 'right', 'j', 'spfunction7', 'key'])
            (var.get('encrypt') and var.put('message', var.get('unescape')(var.get('encodeURIComponent')(var.get('message')))))
            def PyJs_LONG_71_(var=var):
                return var.get('Array').create(Js(16843776.0), Js(0.0), Js(65536.0), Js(16843780.0), Js(16842756.0), Js(66564.0), Js(4.0), Js(65536.0), Js(1024.0), Js(16843776.0), Js(16843780.0), Js(1024.0), Js(16778244.0), Js(16842756.0), Js(16777216.0), Js(4.0), Js(1028.0), Js(16778240.0), Js(16778240.0), Js(66560.0), Js(66560.0), Js(16842752.0), Js(16842752.0), Js(16778244.0), Js(65540.0), Js(16777220.0), Js(16777220.0), Js(65540.0), Js(0.0), Js(1028.0), Js(66564.0), Js(16777216.0), Js(65536.0), Js(16843780.0), Js(4.0), Js(16842752.0), Js(16843776.0), Js(16777216.0), Js(16777216.0), Js(1024.0), Js(16842756.0), Js(65536.0), Js(66560.0), Js(16777220.0), Js(1024.0), Js(4.0), Js(16778244.0), Js(66564.0), Js(16843780.0), Js(65540.0), Js(16842752.0), Js(16778244.0), Js(16777220.0), Js(1028.0), Js(66564.0), Js(16843776.0), Js(1028.0), Js(16778240.0), Js(16778240.0), Js(0.0), Js(65540.0), Js(66560.0), Js(0.0), Js(16842756.0))
            var.put('spfunction1', PyJs_LONG_71_())
            def PyJs_LONG_72_(var=var):
                return var.get('Array').create((-Js(2146402272.0)), (-Js(2147450880.0)), Js(32768.0), Js(1081376.0), Js(1048576.0), Js(32.0), (-Js(2146435040.0)), (-Js(2147450848.0)), (-Js(2147483616.0)), (-Js(2146402272.0)), (-Js(2146402304.0)), (-Js(2147483648.0)), (-Js(2147450880.0)), Js(1048576.0), Js(32.0), (-Js(2146435040.0)), Js(1081344.0), Js(1048608.0), (-Js(2147450848.0)), Js(0.0), (-Js(2147483648.0)), Js(32768.0), Js(1081376.0), (-Js(2146435072.0)), Js(1048608.0), (-Js(2147483616.0)), Js(0.0), Js(1081344.0), Js(32800.0), (-Js(2146402304.0)), (-Js(2146435072.0)), Js(32800.0), Js(0.0), Js(1081376.0), (-Js(2146435040.0)), Js(1048576.0), (-Js(2147450848.0)), (-Js(2146435072.0)), (-Js(2146402304.0)), Js(32768.0), (-Js(2146435072.0)), (-Js(2147450880.0)), Js(32.0), (-Js(2146402272.0)), Js(1081376.0), Js(32.0), Js(32768.0), (-Js(2147483648.0)), Js(32800.0), (-Js(2146402304.0)), Js(1048576.0), (-Js(2147483616.0)), Js(1048608.0), (-Js(2147450848.0)), (-Js(2147483616.0)), Js(1048608.0), Js(1081344.0), Js(0.0), (-Js(2147450880.0)), Js(32800.0), (-Js(2147483648.0)), (-Js(2146435040.0)), (-Js(2146402272.0)), Js(1081344.0))
            var.put('spfunction2', PyJs_LONG_72_())
            def PyJs_LONG_73_(var=var):
                return var.get('Array').create(Js(520.0), Js(134349312.0), Js(0.0), Js(134348808.0), Js(134218240.0), Js(0.0), Js(131592.0), Js(134218240.0), Js(131080.0), Js(134217736.0), Js(134217736.0), Js(131072.0), Js(134349320.0), Js(131080.0), Js(134348800.0), Js(520.0), Js(134217728.0), Js(8.0), Js(134349312.0), Js(512.0), Js(131584.0), Js(134348800.0), Js(134348808.0), Js(131592.0), Js(134218248.0), Js(131584.0), Js(131072.0), Js(134218248.0), Js(8.0), Js(134349320.0), Js(512.0), Js(134217728.0), Js(134349312.0), Js(134217728.0), Js(131080.0), Js(520.0), Js(131072.0), Js(134349312.0), Js(134218240.0), Js(0.0), Js(512.0), Js(131080.0), Js(134349320.0), Js(134218240.0), Js(134217736.0), Js(512.0), Js(0.0), Js(134348808.0), Js(134218248.0), Js(131072.0), Js(134217728.0), Js(134349320.0), Js(8.0), Js(131592.0), Js(131584.0), Js(134217736.0), Js(134348800.0), Js(134218248.0), Js(520.0), Js(134348800.0), Js(131592.0), Js(8.0), Js(134348808.0), Js(131584.0))
            var.put('spfunction3', PyJs_LONG_73_())
            def PyJs_LONG_74_(var=var):
                return var.get('Array').create(Js(8396801.0), Js(8321.0), Js(8321.0), Js(128.0), Js(8396928.0), Js(8388737.0), Js(8388609.0), Js(8193.0), Js(0.0), Js(8396800.0), Js(8396800.0), Js(8396929.0), Js(129.0), Js(0.0), Js(8388736.0), Js(8388609.0), Js(1.0), Js(8192.0), Js(8388608.0), Js(8396801.0), Js(128.0), Js(8388608.0), Js(8193.0), Js(8320.0), Js(8388737.0), Js(1.0), Js(8320.0), Js(8388736.0), Js(8192.0), Js(8396928.0), Js(8396929.0), Js(129.0), Js(8388736.0), Js(8388609.0), Js(8396800.0), Js(8396929.0), Js(129.0), Js(0.0), Js(0.0), Js(8396800.0), Js(8320.0), Js(8388736.0), Js(8388737.0), Js(1.0), Js(8396801.0), Js(8321.0), Js(8321.0), Js(128.0), Js(8396929.0), Js(129.0), Js(1.0), Js(8192.0), Js(8388609.0), Js(8193.0), Js(8396928.0), Js(8388737.0), Js(8193.0), Js(8320.0), Js(8388608.0), Js(8396801.0), Js(128.0), Js(8388608.0), Js(8192.0), Js(8396928.0))
            var.put('spfunction4', PyJs_LONG_74_())
            def PyJs_LONG_75_(var=var):
                return var.get('Array').create(Js(256.0), Js(34078976.0), Js(34078720.0), Js(1107296512.0), Js(524288.0), Js(256.0), Js(1073741824.0), Js(34078720.0), Js(1074266368.0), Js(524288.0), Js(33554688.0), Js(1074266368.0), Js(1107296512.0), Js(1107820544.0), Js(524544.0), Js(1073741824.0), Js(33554432.0), Js(1074266112.0), Js(1074266112.0), Js(0.0), Js(1073742080.0), Js(1107820800.0), Js(1107820800.0), Js(33554688.0), Js(1107820544.0), Js(1073742080.0), Js(0.0), Js(1107296256.0), Js(34078976.0), Js(33554432.0), Js(1107296256.0), Js(524544.0), Js(524288.0), Js(1107296512.0), Js(256.0), Js(33554432.0), Js(1073741824.0), Js(34078720.0), Js(1107296512.0), Js(1074266368.0), Js(33554688.0), Js(1073741824.0), Js(1107820544.0), Js(34078976.0), Js(1074266368.0), Js(256.0), Js(33554432.0), Js(1107820544.0), Js(1107820800.0), Js(524544.0), Js(1107296256.0), Js(1107820800.0), Js(34078720.0), Js(0.0), Js(1074266112.0), Js(1107296256.0), Js(524544.0), Js(33554688.0), Js(1073742080.0), Js(524288.0), Js(0.0), Js(1074266112.0), Js(34078976.0), Js(1073742080.0))
            var.put('spfunction5', PyJs_LONG_75_())
            def PyJs_LONG_76_(var=var):
                return var.get('Array').create(Js(536870928.0), Js(541065216.0), Js(16384.0), Js(541081616.0), Js(541065216.0), Js(16.0), Js(541081616.0), Js(4194304.0), Js(536887296.0), Js(4210704.0), Js(4194304.0), Js(536870928.0), Js(4194320.0), Js(536887296.0), Js(536870912.0), Js(16400.0), Js(0.0), Js(4194320.0), Js(536887312.0), Js(16384.0), Js(4210688.0), Js(536887312.0), Js(16.0), Js(541065232.0), Js(541065232.0), Js(0.0), Js(4210704.0), Js(541081600.0), Js(16400.0), Js(4210688.0), Js(541081600.0), Js(536870912.0), Js(536887296.0), Js(16.0), Js(541065232.0), Js(4210688.0), Js(541081616.0), Js(4194304.0), Js(16400.0), Js(536870928.0), Js(4194304.0), Js(536887296.0), Js(536870912.0), Js(16400.0), Js(536870928.0), Js(541081616.0), Js(4210688.0), Js(541065216.0), Js(4210704.0), Js(541081600.0), Js(0.0), Js(541065232.0), Js(16.0), Js(16384.0), Js(541065216.0), Js(4210704.0), Js(16384.0), Js(4194320.0), Js(536887312.0), Js(0.0), Js(541081600.0), Js(536870912.0), Js(4194320.0), Js(536887312.0))
            var.put('spfunction6', PyJs_LONG_76_())
            def PyJs_LONG_77_(var=var):
                return var.get('Array').create(Js(2097152.0), Js(69206018.0), Js(67110914.0), Js(0.0), Js(2048.0), Js(67110914.0), Js(2099202.0), Js(69208064.0), Js(69208066.0), Js(2097152.0), Js(0.0), Js(67108866.0), Js(2.0), Js(67108864.0), Js(69206018.0), Js(2050.0), Js(67110912.0), Js(2099202.0), Js(2097154.0), Js(67110912.0), Js(67108866.0), Js(69206016.0), Js(69208064.0), Js(2097154.0), Js(69206016.0), Js(2048.0), Js(2050.0), Js(69208066.0), Js(2099200.0), Js(2.0), Js(67108864.0), Js(2099200.0), Js(67108864.0), Js(2099200.0), Js(2097152.0), Js(67110914.0), Js(67110914.0), Js(69206018.0), Js(69206018.0), Js(2.0), Js(2097154.0), Js(67108864.0), Js(67110912.0), Js(2097152.0), Js(69208064.0), Js(2050.0), Js(2099202.0), Js(69208064.0), Js(2050.0), Js(67108866.0), Js(69208066.0), Js(69206016.0), Js(2099200.0), Js(0.0), Js(2.0), Js(69208066.0), Js(0.0), Js(2099202.0), Js(69206016.0), Js(2048.0), Js(67108866.0), Js(67110912.0), Js(2048.0), Js(2097154.0))
            var.put('spfunction7', PyJs_LONG_77_())
            def PyJs_LONG_78_(var=var):
                return var.get('Array').create(Js(268439616.0), Js(4096.0), Js(262144.0), Js(268701760.0), Js(268435456.0), Js(268439616.0), Js(64.0), Js(268435456.0), Js(262208.0), Js(268697600.0), Js(268701760.0), Js(266240.0), Js(268701696.0), Js(266304.0), Js(4096.0), Js(64.0), Js(268697600.0), Js(268435520.0), Js(268439552.0), Js(4160.0), Js(266240.0), Js(262208.0), Js(268697664.0), Js(268701696.0), Js(4160.0), Js(0.0), Js(0.0), Js(268697664.0), Js(268435520.0), Js(268439552.0), Js(266304.0), Js(262144.0), Js(266304.0), Js(262144.0), Js(268701696.0), Js(4096.0), Js(64.0), Js(268697664.0), Js(4096.0), Js(266304.0), Js(268439552.0), Js(64.0), Js(268435520.0), Js(268697600.0), Js(268697664.0), Js(268435456.0), Js(262144.0), Js(268439616.0), Js(0.0), Js(268701760.0), Js(262208.0), Js(268435520.0), Js(268697600.0), Js(268439552.0), Js(268439616.0), Js(0.0), Js(268701760.0), Js(266240.0), Js(266240.0), Js(4160.0), Js(4160.0), Js(262208.0), Js(268435456.0), Js(268701696.0))
            var.put('spfunction8', PyJs_LONG_78_())
            var.put('keys', var.get('$').callprop('des_createKeys', var.get('key')))
            var.put('m', Js(0.0))
            var.put('len', var.get('message').get('length'))
            var.put('chunk', Js(0.0))
            var.put('iterations', (Js(3.0) if (Js(32.0)==var.get('keys').get('length')) else Js(9.0)))
            def PyJs_LONG_79_(var=var):
                return ((var.get('Array').create(Js(0.0), Js(32.0), Js(2.0)) if var.get('encrypt') else var.get('Array').create(Js(30.0), (-Js(2.0)), (-Js(2.0)))) if (Js(3.0)==var.get('iterations')) else (var.get('Array').create(Js(0.0), Js(32.0), Js(2.0), Js(62.0), Js(30.0), (-Js(2.0)), Js(64.0), Js(96.0), Js(2.0)) if var.get('encrypt') else var.get('Array').create(Js(94.0), Js(62.0), (-Js(2.0)), Js(32.0), Js(64.0), Js(2.0), Js(30.0), (-Js(2.0)), (-Js(2.0)))))
            def PyJs_LONG_80_(var=var):
                return ((var.get('encrypt') and PyJsComma(PyJsComma(var.put('temp', (Js(8.0)-(var.get('len')%Js(8.0)))),var.put('message', var.get('String').callprop('fromCharCode', var.get('temp'), var.get('temp'), var.get('temp'), var.get('temp'), var.get('temp'), var.get('temp'), var.get('temp'), var.get('temp')), '+')),(PyJsStrictEq(Js(8.0),var.get('temp')) and var.put('len', Js(8.0), '+')))) if (Js(1.0)==var.get('padding')) else (var.get('padding') or var.put('message', Js('\x00\x00\x00\x00\x00\x00\x00\x00'), '+')))
            PyJsComma(var.put('looping', PyJs_LONG_79_()),(var.put('message', Js('        '), '+') if (Js(2.0)==var.get('padding')) else PyJs_LONG_80_()))
            var.put('result', Js(''))
            var.put('tempresult', Js(''))
            #for JS loop
            def PyJs_LONG_81_(var=var):
                return ((((var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
            def PyJs_LONG_82_(var=var):
                return ((((var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
            ((Js(1.0)==var.get('mode')) and PyJsComma(PyJsComma(var.put('cbcleft', PyJs_LONG_81_()),var.put('cbcright', PyJs_LONG_82_())),var.put('m', Js(0.0))))
            while (var.get('m')<var.get('len')):
                #for JS loop
                def PyJs_LONG_85_(var=var):
                    def PyJs_LONG_83_(var=var):
                        return ((((var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
                    def PyJs_LONG_84_(var=var):
                        return ((((var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('left', PyJs_LONG_83_()),var.put('right', PyJs_LONG_84_())),((Js(1.0)==var.get('mode')) and (PyJsComma(var.put('left', var.get('cbcleft'), '^'),var.put('right', var.get('cbcright'), '^')) if var.get('encrypt') else PyJsComma(PyJsComma(PyJsComma(var.put('cbcleft2', var.get('cbcleft')),var.put('cbcright2', var.get('cbcright'))),var.put('cbcleft', var.get('left'))),var.put('cbcright', var.get('right')))))),var.put('left', (var.put('temp', (Js(252645135.0)&(PyJsBshift(var.get('left'),Js(4.0))^var.get('right'))))<<Js(4.0)), '^')),var.put('left', (var.put('temp', (Js(65535.0)&(PyJsBshift(var.get('left'),Js(16.0))^var.put('right', var.get('temp'), '^'))))<<Js(16.0)), '^')),var.put('left', var.put('temp', (Js(858993459.0)&(PyJsBshift(var.put('right', var.get('temp'), '^'),Js(2.0))^var.get('left')))), '^')),var.put('left', var.put('temp', (Js(16711935.0)&(PyJsBshift(var.put('right', (var.get('temp')<<Js(2.0)), '^'),Js(8.0))^var.get('left')))), '^')),var.put('left', ((var.put('left', (var.put('temp', (Js(1431655765.0)&(PyJsBshift(var.get('left'),Js(1.0))^var.put('right', (var.get('temp')<<Js(8.0)), '^'))))<<Js(1.0)), '^')<<Js(1.0))|PyJsBshift(var.get('left'),Js(31.0))))),var.put('right', ((var.put('right', var.get('temp'), '^')<<Js(1.0))|PyJsBshift(var.get('right'),Js(31.0))))),var.put('j', Js(0.0)))
                PyJs_LONG_85_()
                while (var.get('j')<var.get('iterations')):
                    try:
                        #for JS loop
                        PyJsComma(PyJsComma(var.put('endloop', var.get('looping').get((var.get('j')+Js(1.0)))),var.put('loopinc', var.get('looping').get((var.get('j')+Js(2.0))))),var.put('i', var.get('looping').get(var.get('j'))))
                        while (var.get('i')!=var.get('endloop')):
                            try:
                                def PyJs_LONG_87_(var=var):
                                    def PyJs_LONG_86_(var=var):
                                        return (((((var.get('spfunction2').get((PyJsBshift(var.get('right1'),Js(24.0))&Js(63.0)))|var.get('spfunction4').get((PyJsBshift(var.get('right1'),Js(16.0))&Js(63.0))))|var.get('spfunction6').get((PyJsBshift(var.get('right1'),Js(8.0))&Js(63.0))))|var.get('spfunction8').get((Js(63.0)&var.get('right1'))))|var.get('spfunction1').get((PyJsBshift(var.get('right2'),Js(24.0))&Js(63.0))))|var.get('spfunction3').get((PyJsBshift(var.get('right2'),Js(16.0))&Js(63.0))))
                                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('right1', (var.get('right')^var.get('keys').get(var.get('i')))),var.put('right2', ((PyJsBshift(var.get('right'),Js(4.0))|(var.get('right')<<Js(28.0)))^var.get('keys').get((var.get('i')+Js(1.0)))))),var.put('temp', var.get('left'))),var.put('left', var.get('right'))),var.put('right', (var.get('temp')^((PyJs_LONG_86_()|var.get('spfunction5').get((PyJsBshift(var.get('right2'),Js(8.0))&Js(63.0))))|var.get('spfunction7').get((Js(63.0)&var.get('right2')))))))
                                PyJs_LONG_87_()
                            finally:
                                    var.put('i', var.get('loopinc'), '+')
                        PyJsComma(PyJsComma(var.put('temp', var.get('left')),var.put('left', var.get('right'))),var.put('right', var.get('temp')))
                    finally:
                            var.put('j', Js(3.0), '+')
                def PyJs_LONG_89_(var=var):
                    def PyJs_LONG_88_(var=var):
                        return var.put('tempresult', var.get('String').callprop('fromCharCode', PyJsBshift(var.get('left'),Js(24.0)), (PyJsBshift(var.get('left'),Js(16.0))&Js(255.0)), (PyJsBshift(var.get('left'),Js(8.0))&Js(255.0)), (Js(255.0)&var.get('left')), PyJsBshift(var.get('right'),Js(24.0)), (PyJsBshift(var.get('right'),Js(16.0))&Js(255.0)), (PyJsBshift(var.get('right'),Js(8.0))&Js(255.0)), (Js(255.0)&var.get('right'))), '+')
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('right', (PyJsBshift(var.get('right'),Js(1.0))|(var.get('right')<<Js(31.0)))),var.put('right', var.put('temp', (Js(1431655765.0)&(PyJsBshift(var.put('left', (PyJsBshift(var.get('left'),Js(1.0))|(var.get('left')<<Js(31.0)))),Js(1.0))^var.get('right')))), '^')),var.put('right', (var.put('temp', (Js(16711935.0)&(PyJsBshift(var.get('right'),Js(8.0))^var.put('left', (var.get('temp')<<Js(1.0)), '^'))))<<Js(8.0)), '^')),var.put('right', (var.put('temp', (Js(858993459.0)&(PyJsBshift(var.get('right'),Js(2.0))^var.put('left', var.get('temp'), '^'))))<<Js(2.0)), '^')),var.put('right', var.put('temp', (Js(65535.0)&(PyJsBshift(var.put('left', var.get('temp'), '^'),Js(16.0))^var.get('right')))), '^')),var.put('right', var.put('temp', (Js(252645135.0)&(PyJsBshift(var.put('left', (var.get('temp')<<Js(16.0)), '^'),Js(4.0))^var.get('right')))), '^')),var.put('left', (var.get('temp')<<Js(4.0)), '^')),((Js(1.0)==var.get('mode')) and (PyJsComma(var.put('cbcleft', var.get('left')),var.put('cbcright', var.get('right'))) if var.get('encrypt') else PyJsComma(var.put('left', var.get('cbcleft2'), '^'),var.put('right', var.get('cbcright2'), '^'))))),PyJs_LONG_88_()),((Js(512.0)==var.put('chunk', Js(8.0), '+')) and PyJsComma(PyJsComma(var.put('result', var.get('tempresult'), '+'),var.put('tempresult', Js(''))),var.put('chunk', Js(0.0)))))
                PyJs_LONG_89_()
            
            if PyJsComma(PyJsComma(var.put('result', var.get('tempresult'), '+'),var.put('result', var.get('result').callprop('replace', JsRegExp('/\\0*$/g'), Js('')))),var.get('encrypt').neg()):
                if PyJsStrictEq(Js(1.0),var.get('padding')):
                    var.put('paddingChars', Js(0.0))
                    PyJsComma((var.put('len', var.get('result').get('length')) and var.put('paddingChars', var.get('result').callprop('charCodeAt', (var.get('len')-Js(1.0))))),((var.get('paddingChars')<=Js(8.0)) and var.put('result', var.get('result').callprop('substring', Js(0.0), (var.get('len')-var.get('paddingChars'))))))
                var.put('result', var.get('decodeURIComponent')(var.get('escape')(var.get('result'))))
            return var.get('result')
        PyJs_anonymous_70_._set_name('anonymous')
        @Js
        def PyJs_anonymous_90_(key, this, arguments, var=var):
            var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
            var.registers(['pc2bytes3', 'shifts', 'm', 'keys', 'pc2bytes4', 'pc2bytes8', 'pc2bytes6', 'pc2bytes11', 'righttemp', 'n', 'pc2bytes13', 'lefttemp', 'left', 'pc2bytes2', 'pc2bytes9', 'iterations', 'pc2bytes12', 'i', 'temp', 'pc2bytes5', 'right', 'pc2bytes10', 'pc2bytes0', 'j', 'pc2bytes7', 'key', 'pc2bytes1'])
            #for JS loop
            var.put('pc2bytes0', var.get('Array').create(Js(0.0), Js(4.0), Js(536870912.0), Js(536870916.0), Js(65536.0), Js(65540.0), Js(536936448.0), Js(536936452.0), Js(512.0), Js(516.0), Js(536871424.0), Js(536871428.0), Js(66048.0), Js(66052.0), Js(536936960.0), Js(536936964.0)))
            var.put('pc2bytes1', var.get('Array').create(Js(0.0), Js(1.0), Js(1048576.0), Js(1048577.0), Js(67108864.0), Js(67108865.0), Js(68157440.0), Js(68157441.0), Js(256.0), Js(257.0), Js(1048832.0), Js(1048833.0), Js(67109120.0), Js(67109121.0), Js(68157696.0), Js(68157697.0)))
            var.put('pc2bytes2', var.get('Array').create(Js(0.0), Js(8.0), Js(2048.0), Js(2056.0), Js(16777216.0), Js(16777224.0), Js(16779264.0), Js(16779272.0), Js(0.0), Js(8.0), Js(2048.0), Js(2056.0), Js(16777216.0), Js(16777224.0), Js(16779264.0), Js(16779272.0)))
            var.put('pc2bytes3', var.get('Array').create(Js(0.0), Js(2097152.0), Js(134217728.0), Js(136314880.0), Js(8192.0), Js(2105344.0), Js(134225920.0), Js(136323072.0), Js(131072.0), Js(2228224.0), Js(134348800.0), Js(136445952.0), Js(139264.0), Js(2236416.0), Js(134356992.0), Js(136454144.0)))
            var.put('pc2bytes4', var.get('Array').create(Js(0.0), Js(262144.0), Js(16.0), Js(262160.0), Js(0.0), Js(262144.0), Js(16.0), Js(262160.0), Js(4096.0), Js(266240.0), Js(4112.0), Js(266256.0), Js(4096.0), Js(266240.0), Js(4112.0), Js(266256.0)))
            var.put('pc2bytes5', var.get('Array').create(Js(0.0), Js(1024.0), Js(32.0), Js(1056.0), Js(0.0), Js(1024.0), Js(32.0), Js(1056.0), Js(33554432.0), Js(33555456.0), Js(33554464.0), Js(33555488.0), Js(33554432.0), Js(33555456.0), Js(33554464.0), Js(33555488.0)))
            var.put('pc2bytes6', var.get('Array').create(Js(0.0), Js(268435456.0), Js(524288.0), Js(268959744.0), Js(2.0), Js(268435458.0), Js(524290.0), Js(268959746.0), Js(0.0), Js(268435456.0), Js(524288.0), Js(268959744.0), Js(2.0), Js(268435458.0), Js(524290.0), Js(268959746.0)))
            var.put('pc2bytes7', var.get('Array').create(Js(0.0), Js(65536.0), Js(2048.0), Js(67584.0), Js(536870912.0), Js(536936448.0), Js(536872960.0), Js(536938496.0), Js(131072.0), Js(196608.0), Js(133120.0), Js(198656.0), Js(537001984.0), Js(537067520.0), Js(537004032.0), Js(537069568.0)))
            var.put('pc2bytes8', var.get('Array').create(Js(0.0), Js(262144.0), Js(0.0), Js(262144.0), Js(2.0), Js(262146.0), Js(2.0), Js(262146.0), Js(33554432.0), Js(33816576.0), Js(33554432.0), Js(33816576.0), Js(33554434.0), Js(33816578.0), Js(33554434.0), Js(33816578.0)))
            var.put('pc2bytes9', var.get('Array').create(Js(0.0), Js(268435456.0), Js(8.0), Js(268435464.0), Js(0.0), Js(268435456.0), Js(8.0), Js(268435464.0), Js(1024.0), Js(268436480.0), Js(1032.0), Js(268436488.0), Js(1024.0), Js(268436480.0), Js(1032.0), Js(268436488.0)))
            var.put('pc2bytes10', var.get('Array').create(Js(0.0), Js(32.0), Js(0.0), Js(32.0), Js(1048576.0), Js(1048608.0), Js(1048576.0), Js(1048608.0), Js(8192.0), Js(8224.0), Js(8192.0), Js(8224.0), Js(1056768.0), Js(1056800.0), Js(1056768.0), Js(1056800.0)))
            var.put('pc2bytes11', var.get('Array').create(Js(0.0), Js(16777216.0), Js(512.0), Js(16777728.0), Js(2097152.0), Js(18874368.0), Js(2097664.0), Js(18874880.0), Js(67108864.0), Js(83886080.0), Js(67109376.0), Js(83886592.0), Js(69206016.0), Js(85983232.0), Js(69206528.0), Js(85983744.0)))
            var.put('pc2bytes12', var.get('Array').create(Js(0.0), Js(4096.0), Js(134217728.0), Js(134221824.0), Js(524288.0), Js(528384.0), Js(134742016.0), Js(134746112.0), Js(16.0), Js(4112.0), Js(134217744.0), Js(134221840.0), Js(524304.0), Js(528400.0), Js(134742032.0), Js(134746128.0)))
            var.put('pc2bytes13', var.get('Array').create(Js(0.0), Js(4.0), Js(256.0), Js(260.0), Js(0.0), Js(4.0), Js(256.0), Js(260.0), Js(1.0), Js(5.0), Js(257.0), Js(261.0), Js(1.0), Js(5.0), Js(257.0), Js(261.0)))
            var.put('iterations', (Js(3.0) if (var.get('key').get('length')>Js(8.0)) else Js(1.0)))
            var.put('keys', var.get('Array').create((Js(32.0)*var.get('iterations'))))
            var.put('shifts', var.get('Array').create(Js(0.0), Js(0.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0)))
            var.put('m', Js(0.0))
            var.put('n', Js(0.0))
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('iterations')):
                try:
                    def PyJs_LONG_91_(var=var):
                        return ((((var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
                    var.put('left', PyJs_LONG_91_())
                    def PyJs_LONG_92_(var=var):
                        return ((((var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('key').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
                    var.put('right', PyJs_LONG_92_())
                    def PyJs_LONG_93_(var=var):
                        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('left', (var.put('temp', (Js(252645135.0)&(PyJsBshift(var.get('left'),Js(4.0))^var.get('right'))))<<Js(4.0)), '^'),var.put('left', var.put('temp', (Js(65535.0)&(PyJsBshift(var.put('right', var.get('temp'), '^'),(-Js(16.0)))^var.get('left')))), '^')),var.put('left', (var.put('temp', (Js(858993459.0)&(PyJsBshift(var.get('left'),Js(2.0))^var.put('right', (var.get('temp')<<(-Js(16.0))), '^'))))<<Js(2.0)), '^')),var.put('left', var.put('temp', (Js(65535.0)&(PyJsBshift(var.put('right', var.get('temp'), '^'),(-Js(16.0)))^var.get('left')))), '^')),var.put('left', (var.put('temp', (Js(1431655765.0)&(PyJsBshift(var.get('left'),Js(1.0))^var.put('right', (var.get('temp')<<(-Js(16.0))), '^'))))<<Js(1.0)), '^')),var.put('left', var.put('temp', (Js(16711935.0)&(PyJsBshift(var.put('right', var.get('temp'), '^'),Js(8.0))^var.get('left')))), '^')),var.put('temp', ((var.put('left', (var.put('temp', (Js(1431655765.0)&(PyJsBshift(var.get('left'),Js(1.0))^var.put('right', (var.get('temp')<<Js(8.0)), '^'))))<<Js(1.0)), '^')<<Js(8.0))|(PyJsBshift(var.put('right', var.get('temp'), '^'),Js(20.0))&Js(240.0))))),var.put('left', ((((var.get('right')<<Js(24.0))|((var.get('right')<<Js(8.0))&Js(16711680.0)))|(PyJsBshift(var.get('right'),Js(8.0))&Js(65280.0)))|(PyJsBshift(var.get('right'),Js(24.0))&Js(240.0))))),var.put('right', var.get('temp')))
                    PyJs_LONG_93_()
                    #for JS loop
                    var.put('i', Js(0.0))
                    while (var.get('i')<var.get('shifts').get('length')):
                        try:
                            def PyJs_LONG_97_(var=var):
                                def PyJs_LONG_94_(var=var):
                                    return (PyJsComma(var.put('left', ((var.get('left')<<Js(2.0))|PyJsBshift(var.get('left'),Js(26.0)))),var.put('right', ((var.get('right')<<Js(2.0))|PyJsBshift(var.get('right'),Js(26.0))))) if var.get('shifts').get(var.get('i')) else PyJsComma(var.put('left', ((var.get('left')<<Js(1.0))|PyJsBshift(var.get('left'),Js(27.0)))),var.put('right', ((var.get('right')<<Js(1.0))|PyJsBshift(var.get('right'),Js(27.0))))))
                                def PyJs_LONG_95_(var=var):
                                    return (((((var.get('pc2bytes0').get(PyJsBshift(var.put('left', (-Js(15.0)), '&'),Js(28.0)))|var.get('pc2bytes1').get((PyJsBshift(var.get('left'),Js(24.0))&Js(15.0))))|var.get('pc2bytes2').get((PyJsBshift(var.get('left'),Js(20.0))&Js(15.0))))|var.get('pc2bytes3').get((PyJsBshift(var.get('left'),Js(16.0))&Js(15.0))))|var.get('pc2bytes4').get((PyJsBshift(var.get('left'),Js(12.0))&Js(15.0))))|var.get('pc2bytes5').get((PyJsBshift(var.get('left'),Js(8.0))&Js(15.0))))
                                def PyJs_LONG_96_(var=var):
                                    return (((((var.get('pc2bytes7').get(PyJsBshift(var.get('right'),Js(28.0)))|var.get('pc2bytes8').get((PyJsBshift(var.get('right'),Js(24.0))&Js(15.0))))|var.get('pc2bytes9').get((PyJsBshift(var.get('right'),Js(20.0))&Js(15.0))))|var.get('pc2bytes10').get((PyJsBshift(var.get('right'),Js(16.0))&Js(15.0))))|var.get('pc2bytes11').get((PyJsBshift(var.get('right'),Js(12.0))&Js(15.0))))|var.get('pc2bytes12').get((PyJsBshift(var.get('right'),Js(8.0))&Js(15.0))))
                                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_94_(),var.put('right', (-Js(15.0)), '&')),var.put('lefttemp', (PyJs_LONG_95_()|var.get('pc2bytes6').get((PyJsBshift(var.get('left'),Js(4.0))&Js(15.0)))))),var.put('temp', (Js(65535.0)&(PyJsBshift(var.put('righttemp', (PyJs_LONG_96_()|var.get('pc2bytes13').get((PyJsBshift(var.get('right'),Js(4.0))&Js(15.0))))),Js(16.0))^var.get('lefttemp'))))),var.get('keys').put((var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)), (var.get('lefttemp')^var.get('temp')))),var.get('keys').put((var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)), (var.get('righttemp')^(var.get('temp')<<Js(16.0)))))
                            PyJs_LONG_97_()
                        finally:
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            return var.get('keys')
        PyJs_anonymous_90_._set_name('anonymous')
        @Js
        def PyJs_anonymous_98_(key, start, end, this, arguments, var=var):
            var = Scope({'key':key, 'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['key', 'start', 'end'])
            PyJs_Object_99_ = Js({'key':var.get('$').callprop('pad', var.get('key').callprop('slice', var.get('start'), var.get('end'))),'vector':Js(1.0)})
            return PyJs_Object_99_
        PyJs_anonymous_98_._set_name('anonymous')
        @Js
        def PyJs_anonymous_100_(key, this, arguments, var=var):
            var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
            var.registers(['key', 'i'])
            #for JS loop
            var.put('i', var.get('key').get('length'))
            while (var.get('i')<Js(24.0)):
                try:
                    var.put('key', Js('0'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('key')
        PyJs_anonymous_100_._set_name('anonymous')
        @Js
        def PyJs_anonymous_102_(input, this, arguments, var=var):
            var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
            var.registers(['input', 'genKey'])
            var.put('genKey', var.get('$').callprop('genkey', Js('PKCS5Padding'), Js(0.0), Js(24.0)))
            return var.get('btoa')(var.get('$').callprop('des', var.get('genKey').get('key'), var.get('input'), Js(1.0), Js(1.0), Js('26951234'), Js(1.0)))
        PyJs_anonymous_102_._set_name('anonymous')
        @Js
        def PyJs_anonymous_103_(input, this, arguments, var=var):
            var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
            var.registers(['input', 'genKey'])
            var.put('genKey', var.get('$').callprop('genkey', Js('PKCS5Padding'), Js(0.0), Js(24.0)))
            return var.get('$').callprop('des', var.get('genKey').get('key'), var.get('atob')(var.get('input')), Js(0.0), Js(1.0), Js('26951234'), Js(1.0))
        PyJs_anonymous_103_._set_name('anonymous')
        PyJs_Object_101_ = Js({'encrypt':PyJs_anonymous_102_,'decrypt':PyJs_anonymous_103_})
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('$').put('rsa', (var.get('$').get('rsa') or PyJs_Object_7_)),var.get('$').get('rsa').put('encrypt', PyJs_anonymous_8_)),var.get('$').put('des', PyJs_anonymous_70_)),var.get('$').put('des_createKeys', PyJs_anonymous_90_)),var.get('$').put('genkey', PyJs_anonymous_98_)),var.get('$').put('pad', PyJs_anonymous_100_)),var.get('$').put('DES3', PyJs_Object_101_))
    PyJs_LONG_104_()
PyJs_anonymous_6_._set_name('anonymous')
PyJs_anonymous_6_(var.get('jQuery')).neg()
pass


# Add lib to the module scope
tp_link_encryption = var.to_python()
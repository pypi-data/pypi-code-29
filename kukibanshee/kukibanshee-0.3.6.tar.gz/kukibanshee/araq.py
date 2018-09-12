import re

#copied from xdict.utils
def str_lstrip(s,char,count):
    '''
        str_lstrip('sssa','s',0)
        str_lstrip('sssa','s',1)
        str_lstrip('sssa','s',2)
        str_lstrip('sssa','s',3)
        str_lstrip('sssa','s',4)
    '''
    c = 0
    for i in range(0,s.__len__()):
        if(c==count):
            break
        else:
            if(s[i] == char):
                c = c+1
            else:
                break
    if(c==0):
        return(s)
    else:
        return(s[c:])

def str_rstrip(s,char,count):
    '''
        str_rstrip('asss','s',0)
        str_rstrip('asss','s',1)
        str_rstrip('asss','s',2)
        str_rstrip('asss','s',3)
        str_rstrip('asss','s',4)
    '''
    c = 0
    for i in range(s.__len__()-1,-1,-1):
        if(c==count):
            break
        else:
            if(s[i] == char):
                c = c+1
            else:
                break
    if(c==0):
        return(s)
    else:
        ei = s.__len__() - c
        return(s[:ei])



#regex 
def _real_dollar(s,m):
    '''
        $ Matches the end of the string or just before the newline at the end of the string
        this is used to solve the secariono below : 
        >>> regex = re.compile('^a$')
        >>> regex.search('a')
        <_sre.SRE_Match object; span=(0, 1), match='a'>  # expected
        
        #NOT expected when end with '\n'
        >>> regex.search('a\n')
        <_sre.SRE_Match object; span=(0, 1), match='a'> 
        
        >>> regex.search('a\na')

    '''
    #for compatible with old code
    regex = re.compile('')
    if(type(m) == type(regex)):
        m = m.search(s)
    else:
        pass
    ###############################
    if(m):
        length_1 = s.__len__()
        length_2 = m.group(0).__len__()
        if(length_1 == length_2):
            return(True)
        else:
            return(False)
    else:
        return(False)







def _creat_regex(unescaped_regex_str,**kwargs):
    '''something like re.escape, with the unescape part prefix and suffix'''
    if("prefix" in kwargs):
        prefix = kwargs['prefix']
    else:
        prefix =""
    if("suffix" in kwargs):
        suffix = kwargs['suffix']
    else:
        suffix =""
    regex_str = re.escape(unescaped_regex_str)
    regex_str = prefix + regex_str + suffix
    regex = re.compile(regex_str,re.DOTALL)
    return(regex)

def CONST_STR_help():
    abbrev = '''
        octs     _all_octets_str
        ckocts   _all_cookie_octets_str
        sps      _all_separators_str
        dels     _all_delimiters_str
        ndigits  _all_non_digits_str
        ndels    _all_non_delimiters_str
        ctls     _all_ctls_str
    '''
    print(abbrev)

def CONST_REGEX_help():
    abbrev = '''
        octs     re.escape _all_octets_str
        ckocts   re.escape _all_cookie_octets_str
        sps      re.escape _all_separators_str
        dels     re.escape _all_delimiters_str
        ndigits  re.escape _all_non_digits_str
        ndels    re.escape _all_non_delimiters_str
        ctls     re.escape _all_ctls_str
    '''
    print(abbrev)

def _all_octets_str():
    '''any 8-bit sequence of data except NUL'''
    octets = ""
    for i in range(1,256):
        octets = octets + chr(i)
    return(octets)

def _all_cookie_octets_str():
    '''
        %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E; 
        US-ASCII characters excluding CTLs,
        whitespace DQUOTE, comma, semicolon,
        and backslash 
    '''
    all_cookie_octets_str = "\x21"
    for i in range(0x23,0x2C):
        all_cookie_octets_str = all_cookie_octets_str + chr(i)
    for i in range(0x2D,0x3A):
        all_cookie_octets_str = all_cookie_octets_str + chr(i)
    for i in range(0x3C,0x5C):
        all_cookie_octets_str = all_cookie_octets_str + chr(i)
    for i in range(0x5D,0x7E):
        all_cookie_octets_str = all_cookie_octets_str + chr(i)
    return(all_cookie_octets_str)

def _all_separators_str():
    '''()<>@,;:"/[]?={} \t\\'''
    return('()<>@,;:"/[]?={} \t\\')

def _all_delimiters_str():
    '''delimiter = %x09 / %x20-2F / %x3B-40 / %x5B-60 / %x7B-7E'''
    delimiters = "\x09"
    for i in range(0x20,0x30):
        delimiters = delimiters + chr(i)
    for i in range(0x3B,0x41):
        delimiters = delimiters + chr(i)
    for i in range(0x5B,0x61):
        delimiters = delimiters + chr(i)
    for i in range(0x7B,0x7F):
        delimiters = delimiters + chr(i)
    return(delimiters)

def _all_non_digits_str():
    '''non-digit = %x00-2F / %x3A-FF'''
    nds = ""
    for i in range(0x00,0x30):
        nds = nds + chr(i)
    for i in range(0x3A,0x100):
        nds = nds + chr(i)
    return(nds)

def _all_non_delimiters_str():
    '''non-delimiter   = %x00-08 / %x0A-1F / DIGIT / ":" / ALPHA / %x7F-FF'''
    ndels = ":"
    for i in range(0x00,0x09):
        ndels = ndels + chr(i)
    for i in range(0x0A,0x20):
        ndels = ndels + chr(i)
    for i in range(0,10):
        ndels = ndels + str(i)
    for i in range(97,123):
        ndels = ndels + chr(i)
    for i in range(65,91):
        ndels = ndels + chr(i)
    for i in range(0x7F,0x100):
        ndels = ndels + chr(i)
    return(ndels)

def _all_ctls_str():
    ctrls =""
    for i in range(0,32):
        ctrls = ctrls + chr(i)
    ctrls = ctrls + "\x7f"
    return(ctrls)

CONST_STR = {
    'octs':_all_octets_str(),
    'ckocts':_all_cookie_octets_str(),
    'sps':_all_separators_str(),
    'dels':_all_delimiters_str(),
    'ndigits':_all_non_digits_str(),
    'ndels':_all_non_delimiters_str(),
    'ctls':_all_ctls_str()
}

CONST_REGEX = {
    'octs':re.escape(CONST_STR['octs']),
    'ckocts':re.escape(CONST_STR['ckocts']),
    'sps':re.escape(CONST_STR['sps']),
    'dels':re.escape(CONST_STR['dels']),
    'ndigits':re.escape(CONST_STR['ndigits']),
    'ndels':re.escape(CONST_STR['ndels']),
    'ctls':re.escape(CONST_STR['ctls'])
}


#
def _isNUL(c):
    '''null octet'''
    return(c=='\x00')

def _isOCTET(c):
    '''any 8-bit sequence of data except NUL'''
    regex_str = CONST_STR['octs']
    prefix = "^[" 
    suffix = "]$"
    regex = _creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(_real_dollar(c,m)))

def _isWSP(c):
    '''whitespace'''
    return(c=='\x20')

def _is_obs_fold(cc):
    '''CRLF'''
    return(cc=='\r\n')

def _isOWS(s):
    '''
        *( [ obs-fold ] WSP )
        # The OWS (optional whitespace) rule is used where zero or more linear   whitespace characters MAY appear
    '''
    regex = re.compile("^((\r\n)? )*$")
    m=regex.search(s)
    return(bool(_real_dollar(s,m)))

def _is_separators(c):
    '''
        HT = "\t"
        separators= 
            "(" | ")" | "<" | ">" | "@"| "," |
            ";" | ":" | "\" | <">| "/" | "[" |
            "]" | "?" | "=" | "{" | "}" | SP |
            HT 
    '''
    regex = re.compile("^[\(\)<>@,;:\\\\\"/\[\]\?=\{\} \t]$")
    m=regex.search(c)
    return(bool(_real_dollar(c,m)))







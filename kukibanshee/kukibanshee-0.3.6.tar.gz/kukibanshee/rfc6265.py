import re
import urllib.parse
from kukibanshee import araq
from kukibanshee import nozdormu
from kukibanshee import symmtera

#refer to http://publicsuffix.org/
#refer to https://publicsuffix.org/list/public_suffix_list.dat

PUBLICSUFFIXES = []

def is_public_suffixes(domain,**kwargs):
    '''
    '''
    if('public' in kwargs):
        public_suffixes = kwargs['public']
    else:
        public_suffixes = PUBLICSUFFIXES
    cond = (domain in public_suffixes)
    return(cond)

def is_cookie_octet(c):
    '''
        %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E; 
        US-ASCII characters excluding CTLs,
        whitespace DQUOTE, comma, semicolon,
        and backslash 
    '''
    regex_str = araq.CONST_STR['ckocts']
    prefix = "^[" 
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(s,m)))

def is_cookie_value(s):
    '''cookie-value      = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE ) '''
    regex_str = araq.CONST_STR['ckocts']
    prefix = "^[" 
    suffix = "]*$"
    regex1 = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m1=regex1.search(s)
    regex_str = araq.CONST_STR['ckocts']
    prefix = "^\"[" 
    suffix = "]*\"$"
    regex2 = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m2=regex2.search(s)
    rslt = (bool(araq._real_dollar(s,m1))) | (bool(araq._real_dollar(s,m2)))
    return(rslt)

def is_token(s):
    '''1*<any CHAR except CTLs or separators> '''
    regex_ctls_str = araq.CONST_STR['ctls']
    regex_separators_str = araq.CONST_STR['sps']
    regex_str = regex_ctls_str + regex_separators_str
    prefix = "^[^"
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_cookie_name(s):
    '''
        RFC 6265    page-9
        cookie-name       = token 
    '''
    return(is_token(s))

def is_cookie_pair(s):
    '''cookie-pair       = cookie-name "=" cookie-value'''
    try:
        eq_loc = s.index("=")
    except:
        return(False)
    else:
        pass
    name = s[:eq_loc]
    value = s[(eq_loc+1):]
    cond1 = is_token(name)
    cond2 = is_cookie_value(value)
    if(cond1 & cond2):
        return(True)
    else:
        return(False)

def is_sane_cookie_date(s,**kwargs):
    '''
        sane-cookie-date  = <rfc1123-date, defined in [RFC2616], Section 3.3.1>
        SP = " "
        date1 = 2DIGIT SP month SP 4DIGIT
        wkday = "Mon" | "Tue" | "Wed" | "Thu" | "Fri" | "Sat" | "Sun"
        rfc1123-date = wkday "," SP date1 SP time SP "GMT"
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'strict'
    tf = nozdormu.detect_time_fmt(s)
    if(mode == 'strict'):
        cond = ('rfc1123' == tf)
    elif(mode == 'rfc1123-loose'):
        cond = ('rfc1123' in tf)
    else:
        #实际应用中rfc1123,rfc1123_tzoffset,rfc850_a,都有
        cond = True
    if(cond):
        return(True)
    else:
        return(False)

def is_expires_value(s):
    '''"Expires=" sane-cookie-date
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
        
    '''
    return(is_sane_cookie_date(s))

def is_expires_av(s):
    '''
        the attribute-name case-insensitively matches the string   "Expires"
        expires-av        = "Expires=" sane-cookie-date
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
    '''
    prefix = str.lower(s[:8])
    if(prefix=="expires="):
        scd = s[9:]
        return(is_sane_cookie_date(scd))
    else:
        return(False)

def is_max_age_value(s):
    '''
        "Max-Age=" non-zero-digit *DIGIT
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
    '''
    regex= re.compile("^[1-9][0-9]*$")
    m = regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_maxage_av(s):
    '''
        the attribute-name case-insensitively matches the string   "Max-Age"
        "Max-Age=" non-zero-digit *DIGIT
        In practice, both expires-av and max-age-av
        are limited to dates representable by the
        user agent. 
    '''
    prefix = s[:8]
    if(prefix=="max-age="):
        nums = s[9:]
        regex= re.compile("^[1-9][0-9]*$")
        m = regex.search(nums)
        return(bool(araq._real_dollar(nums,m)))
    else:
        return(False)

def is_secure_av(s):
    '''"Secure"'''
    s = str.lower(s)
    return(s=='secure')

def is_httponly_av(s):
    '''"HttpOnly"'''
    s = str.lower(s)
    return(s=='httponly')

def is_path_value(s):
    '''<any CHAR except CTLs or ";">''' 
    regex_ctls_str = araq.CONST_STR['ctls']
    regex_str = regex_ctls_str + ";"
    prefix = "^[^"
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_path_av(s):
    '''
        "Path=" path-value
    '''
    prefix = str.lower(s[:5])
    if(prefix == "path="):
        p = s[6:]
        return(is_path_value(p))
    else:
        return(False)

def is_extension_av(s):
    '''<any CHAR except CTLs or ";">'''
    regex_ctls_str = araq.CONST_STR['ctls']
    regex_str = regex_ctls_str + ";"
    prefix = "^[^"
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def remove_domain_leading_dot(domain):
    '''
        Note that a leading %x2E ("."), if present,
        is ignored even though that character is not permitted, 
        but a trailing %x2E ("."), if present, 
        will cause the user agent to ignore   the attribute.
    '''
    domain = araq.str_lstrip(domain,".",1)
    return(domain)

def is_domain_value(s,**kwargs):
    '''
        domain-value = <subdomain>; 
        defined in [RFC1034], Section 3.5
            <subdomain> ::= <label> | <subdomain> "." <label>
            <label> ::= <letter> [ [ <ldh-str> ] <let-dig> ]
            <ldh-str> ::= <let-dig-hyp> | <let-dig-hyp> <ldh-str>
            <let-dig-hyp> ::= <let-dig> | "-"
            <let-dig> ::= <letter> | <digit>
            <letter> ::= any one of the 52 alphabetic characters A through Z in upper case and a through z in lower case
            <digit> ::= any one of the ten digits 0 through 9
        enhanced by [RFC1123], Section 2.1
        
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'loose'
    if(mode == 'strict'):
        pass
    else:
        s = remove_domain_leading_dot(s)
    regex_label = re.compile("^[a-zA-Z](([0-9a-zA-Z\-])*[0-9a-zA-Z])*$")
    arr = s.split(".")
    rslt = True
    for i in range(0,arr.__len__()):
        m = regex_label.search(arr[i])
        cond = bool(araq._real_dollar(arr[i],m))
        if(cond):
            pass
        else:
            rslt = False
            break
    return(rslt)

def is_domain_av(s):
    '''
        "Domain=" domain-value  
    '''
    prefix = str.lower(s[:7])
    if(prefix == "domain="):
        dm = s[8:]
        return(is_domain_value(dm))
    else:
        return(False)

def is_cookie_av(s):
    '''
        cookie-av = expires-av / max-age-av / domain-av /path-av / secure-av / httponly-av /extension-av
    '''
    expires = is_expires_av(s)
    maxage = is_maxage_av(s)
    domain = is_domain_av(s)
    path = is_path_av(s)
    secure = is_secure_av(s)
    httponly = is_httponly_av(s)
    extension = is_extension_av(s)
    return(expires|maxage|domain|path|secure|httponly|extension)

def is_delimiter(c):
    '''delimiter = %x09 / %x20-2F / %x3B-40 / %x5B-60 / %x7B-7E'''
    regex_str = araq.CONST_STR['dels']
    prefix = "^["
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(c,m)))

#5.1.1 Dates

def is_time_field(s):
    '''time-field      = 1*2DIGIT'''
    regex = re.compile("^[0-9]{1,2}$")
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_hms_time(s):
    '''hms-time = time-field ":" time-field ":" time-field'''
    regex_str = "^[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}$"
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_non_digit(c):
    '''non-digit = %x00-2F / %x3A-FF'''
    nds = araq.CONST_STR['ndigits']
    regex_str = nds
    prefix = "^[" 
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(c,m)))

def is_non_delimiter(c):
    '''non-delimiter   = %x00-08 / %x0A-1F / DIGIT / ":" / ALPHA / %x7F-FF'''
    ndels = araq.CONST_STR['ndels']
    regex_str = ndels
    prefix = "^[" 
    suffix = "]$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(c)
    return(bool(araq._real_dollar(c,m)))

def is_date_token(s):
    '''date-token      = 1*non-delimiter'''
    dt = araq.CONST_STR['ndels']
    regex_str = dt
    prefix = "^[" 
    suffix = "]+$"
    regex = araq._creat_regex(regex_str,prefix=prefix,suffix=suffix)
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_date_token_list(s):
    '''date-token-list = date-token *( 1*delimiter date-token )'''
    dt = re.escape(araq.CONST_STR['ndels'])
    ads = re.escape(araq.CONST_STR['dels'])
    regex_str = "^[" + dt + "]+" +"([" +ads+ "]+"+"[" + dt + "]+)*$"
    m=regex.search(s)
    return(bool(araq._real_dollar(s,m)))

def is_cookie_date(s):
    '''cookie-date     = *delimiter date-token-list *delimiter'''
    ads = re.escape(araq.CONST_STR['dels'])
    regex_str = "([" + ads + "]*)" + "(.*)" + "([" + ads + "]*)"
    regex = re.compile(regex_str,re.DOTALL)
    m = regex.search(s)
    try:
        dtl = m.group(2)
    except:
        return(False)
    else:
        pass
    return(is_date_token_list(dtl))

def is_time(s):
    '''
        time            = hms-time ( non-digit *OCTET )
        cant understand why ( non-digit *OCTET )
    '''
    regex_str = "^([0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2})"
    #cant understand why ( non-digit *OCTET )
    nds = "[" + re.escape(araq.CONST_STR['ndigits']) + "]{0,1}"
    prefix = "["
    octs = re.escape(araq.CONST_STR['octs'])
    suffix = "]*$"
    regex_str = regex_str + nds + prefix + octs + suffix
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_year(s):
    '''
        year = 2*4DIGIT ( non-digit *OCTET )
        cant understand why ( non-digit *OCTET )
    '''
    # regex_str = "^([0-9]{2,4})"
    #cant understand why ( non-digit *OCTET )
    # nds = "[" + re.escape(araq.CONST_STR['ndigits']) + "]{0,1}"
    # prefix = "["
    # octs = re.escape(araq.CONST_STR['octs'])
    # suffix = "]*$"
    # regex_str = regex_str + nds + prefix + octs + suffix
    #avoid conflict with day-of-month ,only support 4numbers year
    regex_str = "^([0-9]{4})$"
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_month(s,**kwargs):
    '''( "jan" / "feb" / "mar" / "apr" /"may" / "jun" / "jul" / "aug" /"sep" / "oct" / "nov" / "dec" ) *OCTET
        mode = 'loose' will case-insensitively
        by default loose
    '''
    if('mode' in kwargs):
       mode = kwargs['mode']
    else:
        mode = 'loose'
    if(mode == 'loose'):
        s = str.lower(s)
    else:
        pass
    regex_str = "^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)"
    prefix = "["
    octs = re.escape(araq.CONST_STR['octs'])
    suffix = "]*$"
    regex_str = regex_str + prefix + octs + suffix
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)

def is_day_of_month(s,**kwargs):
    '''
        day-of-month    = 1*2DIGIT ( non-digit *OCTET )
        cant understand why ( non-digit *OCTET )
    '''
    # regex_str = "^[0-9]{1,2}"
    # ndts = re.escape(araq.CONST_STR['ndigits'])
    # prefix = "["
    # octs = re.escape(araq.CONST_STR['octs'])
    # suffix = "]*$"
    #cant understand why ( non-digit *OCTET )
    # regex_str = regex_str + "[" + ndts + "]{0,1}" + prefix + octs + suffix
    regex_str = "^[0-9]{1,2}$"
    regex = re.compile(regex_str)
    m=regex.search(s)
    rslt = (bool(araq._real_dollar(s,m)))
    return(rslt)


CORERULES = {
    'NUL' : araq._isNUL,
    'OCTET' : araq._isOCTET,
    'WSP' : araq._isWSP,
    'OWS' : araq._isOWS,
    'cookie-header':'IMPLEMENTED IN drone.py : validate_ckheader',
    'cookie-string':'IMPLEMENTED IN drone.py : validate_ckstr',
    'obs-fold' : araq._is_obs_fold,
    'cookie-octet' : is_cookie_octet,
    'cookie-value' : is_cookie_value,
    'cookie-name' : is_token,
    'sane-cookie-date' : is_sane_cookie_date,
    'cookie-pair' : is_cookie_pair,
    'expires-av' : is_expires_av,
    'max-age-av' : is_maxage_av,
    'secure-av' : is_secure_av,
    'httponly-av' : is_httponly_av,
    'path-value' : is_path_value,
    'extension-av' : is_extension_av,
    'path-av' : is_path_av,
    'domain-av' : is_domain_av,
    'cookie-av' : is_cookie_av,
    'set-cookie-string' : 'IMPLEMENTED IN drone.py validate_setckstr',
    'set-cookie-header' : 'IMPLEMENTED IN drone.py validate_setckheader',
    'delimiter' : is_delimiter,
    'time-field' : is_time_field,
    'hms-time' : is_hms_time,
    'time' : is_time,
    'non-digit' : is_non_digit,
    'non-delimiter' : is_non_delimiter,
    'date-token' : is_date_token,
    'date-token-list' : is_date_token_list,
    'cookie-date' : is_cookie_date,
    'year': is_year,
    'month': is_month,
    'day-of-month': is_day_of_month
}

def split_cookie_date_str(s):
    '''
        split cookie_date_str to date-tokens list
        split_cookie_date_str('Tue, 27 Mar 2018 05:30:16')
        >>> split_cookie_date_str('Tue, 27 Mar 2018 05:30:16')
        ['Tue', '27', 'Mar', '2018', '05:30:16']
        >>>
    '''
    def _open_token(tok,input_symbol,rslt):
        tok = tok + input_symbol
        return(tok)
    _append_token = _open_token
    def _close_token(tok,input_symbol,rslt):
        rslt.append(tok)
        tok = ''
        return(tok)
    machine = symmtera.FSM()
    machine.add("INIT",is_delimiter,None,"DEL")
    machine.add("INIT",is_non_delimiter,_open_token,"TOK")
    machine.add("DEL",is_delimiter,None,"DEL")
    machine.add("DEL",is_non_delimiter,_open_token,"TOK")
    machine.add("TOK",is_delimiter,_close_token,"DEL")
    machine.add("TOK",is_non_delimiter,_append_token,"TOK")
    curr_state = "INIT"
    rslt = []
    tok= ''
    for i in range(0,s.__len__()):
        input_symbol = s[i]
        action,next_state,trigger_checker = machine.search(curr_state,input_symbol)
        if(action):
            tok = action(tok,input_symbol,rslt)
        else:
            pass
        curr_state = next_state
    if(curr_state == 'INIT'):
        return([])
    elif(curr_state == 'DEL'):
        pass
    else:
        rslt.append(tok)
    return(rslt)

def parse_cookie_date(s):
    '''
        cookie_date_dict = parse_cookie_date('Tue, 27 Mar 2018 05:30:16')
        pobj(cookie_date_dict)
        #rfc6265 Page-14 Page-15
        2. Process each date-token sequentially in the order the date-tokens appear in the cookie-date:
        
            1.  If the found-time flag is not set and the token matches thetime production, 
                set the found-time flag and set the hour value,minute-value,and second-value 
                to the numbers denoted by the digits in the date-token, respectively.  
                Skip the  remaining sub-steps and continue to the next date-token.
            2.  If the found-day-of-month flag is not set and the date-token matches the day-of-month production,
                set the found-day-of  month flag and set the day-of-month-value to the number 
                denoted by the date-token. Skip the remaining sub-steps and continue to the next date-token.
        
        3.  If the found-month flag is not set and the date-token matches the month production, 
            set the found-month flag and set the month-value to the month denoted by the date-token.  
            Skip the remaining sub-steps and continue to the next date-token.
        4.  If the found-year flag is not set and the date-token matches the year production, 
            set the found-year flag and set the year-value to the number denoted by the date-token. 
            Skip the remaining sub-steps and continue to the next date-token.
        3.  If the year-value is greater than or equal to 70 and less than or equal to 99, 
            increment the year-value by 1900.
        4.  If the year-value is greater than or equal to 0 and less than or 
            equal to 69, increment the year-value by 2000.
            1.  NOTE: Some existing user agents interpret two-digit years differently.
        5.  Abort these steps and fail to parse the cookie-date if:
            *  at least one of the found-day-of-month, found-month, found year, 
               or found-time flags is not set,
            *  the day-of-month-value is less than 1 or greater than 31,
            *  the year-value is less than 1601,
            *  the hour-value is greater than 23,
            *  the minute-value is greater than 59, or
            *  the second-value is greater than 59.
            (Note that leap seconds cannot be represented in this syntax.)
        6.  Let the parsed-cookie-date be the date whose day-of-month, month, 
            year, hour, minute, and second (in UTC) are the day-of-month value, 
            the month-value, the year-value, the hour-value, the minute-value, 
            and the second-value, respectively.  If no such date exists, 
            abort these steps and fail to parse the cookie-date.
        7.  Return the parsed-cookie-date as the result of this algorithm.
    '''
    toks = split_cookie_date_str(s)
    cookie_date_dict = {
        'found-time':False,
        'hour-value':None,
        'minute-value':None,
        'second-value': None,
        'found-day-of-month':False,
        'day-of-month-value':None,
        'found-month':False,
        'month-value':None,
        'found-year':False,
        'year-value':None,
        '_timestamp':None,
    }
    tests = ['hms-time','day-of-month','month','year']
    for tok in toks:
        if('hms-time' in tests):
            cond = CORERULES['hms-time'](tok)
            if(cond):
                tmp = tok.split(":")
                if((int(tmp[0])<0) | (int(tmp[0])>23)):
                    pass
                else:
                    cookie_date_dict['hour-value'] = int(tmp[0])
                if((int(tmp[1])<0) | (int(tmp[1])>59)):
                    pass
                else:
                    cookie_date_dict['minute-value'] = tmp[1]
                if((int(tmp[2])<0) | (int(tmp[2])>59)):
                    pass
                else:
                    cookie_date_dict['second-value'] = tmp[2]
                cookie_date_dict['found-time'] = True
                tests.remove('hms-time')
            else:
                pass
        if('day-of-month' in tests):
            cond = CORERULES['day-of-month'](tok)
            if(cond):
                regex = re.compile("[0-9]{1,2}")
                tmp = regex.search(tok).group(0)
                if((int(tmp)<1) | (int(tmp)>31)):
                    pass
                else:
                    cookie_date_dict['day-of-month-value'] = int(tmp)
                cookie_date_dict['found-day-of-month'] = True
                tests.remove('day-of-month')
            else:
                pass
        if('month' in tests):
            cond = CORERULES['month'](tok)
            if(cond):
                tmp = tok[0:3]
                cookie_date_dict['month-value'] = tmp
                cookie_date_dict['found-month'] = True
                tests.remove('month')
            else:
                pass
        if('year' in tests):
            cond = CORERULES['year'](tok)
            if(cond):
                regex = re.compile("[0-9]{2,4}")
                tmp = regex.search(tok).group(0)
                if((int(tmp)>=70)&(int(tmp)<=99)):
                    tmp = 1900 + int(tmp)
                elif((int(tmp)>=0)&(int(tmp)<=69)):
                    tmp = 2000 + int(tmp)
                else:
                    tmp = int(tmp)
                cookie_date_dict['year-value'] = tmp
                cookie_date_dict['found-year'] = True
                tests.remove('year')
            else:
                pass
        else:
            pass
    cookie_date_dict['_timestamp'] = nozdormu.str2ts(s)
    return(cookie_date_dict)

def domain_in_domain(dom1,dom2):
    '''
        domain_in_domain('www.baidu.com','baidu.com')
    '''
    dom2 = dom2.lower()
    dom1 = dom1.lower()
    dom2 = remove_domain_leading_dot(dom2) 
    dom1 = remove_domain_leading_dot(dom1)
    dom1_arr = dom1.split(".")
    dom2_arr = dom2.split(".")
    length1 = dom1_arr.__len__()
    length2 = dom2_arr.__len__()
    if(length1 < length2):
        return(False)
    else:
        dom1_arr.reverse()
        dom2_arr.reverse()
        for i in range(length2-1,-1,-1):
            cond = (dom1_arr[i] == dom2_arr[i])
            if(cond):
                pass
            else:
                return(False)
        return(True)

def format_origin(server_url):
    if(is_domain_value(server_url)):
        server_url = '//'+server_url
    else:
        #url
        pass
    netloc =  urllib.parse.urlparse(server_url).netloc
    return(netloc)

def origin_in_domain(server_url,domain):
    '''
        origin_in_domain('http://foo.example.com',"example.com")
        origin_in_domain('http://foo.example.com',"baz.foo.example.com")
        
        The user agent will reject cookies unless the Domain attribute
        specifies a scope for the cookie that would include the origin server.
        For example, the user agent will accept a cookie with a Domain attribute
        of "example.com" or of "foo.example.com" from foo.example.com, but the 
        user agent will not accept a cookie with a Domain attribute of "bar.example.com" 
        or of "baz.foo.example.com".
    '''
    domain = remove_domain_leading_dot(domain)
    netloc = format_origin(server_url)
    netloc = remove_domain_leading_dot(netloc)
    cond = domain_in_domain(netloc,domain)
    return(cond)

def target_in_domain(target_url,domain):
    '''
        target_in_domain('http://bar.example.com',"example.com")
    '''
    domain = remove_domain_leading_dot(domain)
    netloc =  urllib.parse.urlparse(target_url).netloc
    netloc = remove_domain_leading_dot(netloc)
    cond = domain_in_domain(netloc,domain)
    return(cond)

def in_domain(domain,**kwargs):
    '''
        in_domain("example.com",target = 'http://bar.example.com', origin = 'http://foo.example.com')
        
        NOTE: For security reasons, many user agents are configured to reject 
        Domain attributes that correspond to "public suffixes".  For example,
        some user agents will reject Domain attributes of "com" or "co.uk". 
    '''
    src_url = kwargs['origin']
    dst_url = kwargs['target']
    if('public' in kwargs):
        reject_public_suffixes = kwargs['public']
    else:
        reject_public_suffixes=PUBLICSUFFIXES
    cond_src = origin_in_domain(src_url,domain)
    cond_dst = target_in_domain(dst_url,domain)
    cond_pub_suffixes = True
    domain = remove_domain_leading_dot(domain)
    for i in range(0,reject_public_suffixes.__len__()):
        cond = (domain == reject_public_suffixes[i])
        if(cond):
            pass
        else:
            cond_pub_suffixes = False
            break
    if(cond_src & cond_dst & cond_pub_suffixes):
        return(True)
    else:
        return(False)


def  canonicalize_hostname(hn):
    '''
        A canonicalized host name is the string generated by the following algorithm:
            1.  Convert the host name to a sequence of individual domain name labels.
            2.  Convert each label that is not a Non-Reserved LDH (NR-LDH) label,
                to an A-label (see Section 2.3.2.1 of [RFC5890] for the former and latter), 
                or to a "punycode label" (a label resulting from the "ToASCII" conversion in Section 4 of [RFC3490]), 
                as appropriate (see Section 6.3 of this specification).
            3.  Concatenate the resulting labels, separated by a %x2E (".") character.
    '''
    print("NOT IMPLEMENTED YET")
    return(hn)

def is_hostname(s):
    print("NOT IMPLEMENTED YET")
    return(True)

def domain_matching(s,domain):
    '''
        A string domain-matches a given domain string if at least one of the following conditions hold:
           o  The domain string and the string are identical.  
             (Note that both the domain string and the string will 
              have been canonicalized to lower case at this point.)
           o  All of the following conditions hold:
              *  The domain string is a suffix of the string.
              *  The last character of the string that is not included in the 
                 domain string is a %x2E (".") character.
              *  The string is a host name (i.e., not an IP address).
    '''
    domain = domain.lower()
    s = s.lower()
    dlen = domain.__len__()
    slen = s.__len__()
    if(dlen > slen):
        cond = False
    else:
        if(domain == s):
            cond = True
        elif(domain == s[0:dlen]):
            if(s[dlen]=="."):
                if(is_hostname(s)):
                    cond = True
                else:
                    cond = False
            else:
                return(False)
        else:
            cond = False
    return(cond)


#@@@@
def format_path(s,mode="strict"):
    '''
        >>> format_path('a')
        '/a'
        >>> format_path('/a')
        '/a'
        >>>
        >>>
        >>> format_path('/a/')
        '/a'
        >>> format_path('/a/b')
        '/a/b'
        >>> format_path('/a/b/')
        '/a/b'
        >>>
        >>> format_path('a',mode='loose')
        '/'
        >>> format_path('')
        '/'
        
        1 .Let uri-path be the path portion of the request-uri if such a portion exists (and empty otherwise).
        For example, if the request-uri contains just a path (and optional query string),
        then the uri-path is that path (without the %x3F ("?") character or query string), 
        and if the request-uri contains a full absoluteURI, 
        the uri-path is the path component of that URI.
        
        2 .If the uri-path is empty or if the first character of the uri
        path is not a %x2F ("/") character, output %x2F ("/") and skip the remaining steps
        ---------------this step is puzzle ,the loose mode will be this behavior
        
        3. If the uri-path contains no more than one %x2F ("/") character,
        output %x2F ("/") and skip the remaining step.
        
        4. Output the characters of the uri-path from the first character up to, 
        but not including, the right-most %x2F ("/").
    '''
    #step 1
    s =  urllib.parse.urlparse(s).path
    #step 2
    if(s == ""):
        return("/")
    elif(s[0]!="/"):
        if(mode == "loose"):
            return("/")
        else:
            s = "/" + s
            s = araq.str_rstrip(s,"/",1)
            return(s)
    #step 3
    elif(s=="/"):
        return("/")
    #step 4:
    else:
        s = araq.str_rstrip(s,"/",1)
        return(s)

def path_in_path(path2,path1,mode='strict'):
    '''
        path_in_path('/a/b','/a/')
        path_in_path('/a/b/','/a/')
        path_in_path('/a/b','/a')
        path_in_path('/a/b/','/a')
        path_in_path('/a/b','a')
        path_in_path('/a/b/','a')
        path_in_path('/a/b','a')
        path_in_path('/a/b/','a')
        path_in_path('/a/b/','')
    '''
    path1 = format_path(path1,mode=mode)
    path1 = araq.str_lstrip(path1,"/",1)
    path2 = format_path(path2,mode=mode)
    path2 = araq.str_lstrip(path2,"/",1)
    p1_arr = path1.split("/")
    if(p1_arr == [""]):
        return(True)
    else:
        pass
    p2_arr = path2.split("/")
    length1 = p1_arr.__len__()
    length2 = p2_arr.__len__()
    if(length1 > length2):
        return(False)
    else:
        for i in range(length1-1,-1,-1):
            cond = (p1_arr[i] == p2_arr[i])
            if(cond):
                pass
            else:
                return(False)
        return(True)

def path_matching(dst_path,path):
    '''
        A request-path path-matches a given cookie-path if at least one of   the following conditions holds:
        o  The cookie-path and the request-path are identical.
        o  The cookie-path is a prefix of the request-path, 
           and the last character of the cookie-path is %x2F ("/").
        o  The cookie-path is a prefix of the request-path, 
           and the first character of the request-path that 
           is not included in the cookie path is a %x2F ("/") character.
    '''
    plength = path.__len__()
    if(plength > dst_path.__len__()):
        cond = False
    elif(path == dst_path):
        cond = True
    elif(dst_path[0:plength] == path):
        if(path[-1] == "/"):
            cond = True
        else:
            if(dst_path[plength]=="/"):
                cond = True
            else:
                cond = False
    else:
        cond = False
    return(cond)

def url_in_path(dst_url,path):
    '''
        A request-path path-matches a given cookie-path if at least one of   the following conditions holds:
        o  The cookie-path and the request-path are identical.
        o  The cookie-path is a prefix of the request-path, 
           and the last character of the cookie-path is %x2F ("/").
        o  The cookie-path is a prefix of the request-path, 
           and the first character of the request-path that 
           is not included in the cookie path is a %x2F ("/") character.
    '''
    dst_path = urllib.parse.urlparse(dst_url).path
    return(path_matching(path,dst_path))



















# If the user agent receives a new cookie with the same cookie-name,   
# domain-value, and path-value as a cookie that it has already stored,   
# the existing cookie is evicted and replaced with the new cookie.



# 10.  If the cookie was received from a "non-HTTP" API and the        cookie’s http-only-flag is set, abort these steps and ignore the        cookie entirely.
   # 11.  If the cookie store contains a cookie with the same name,        domain, and path as the newly created cookie:
        # 1.  Let old-cookie be the existing cookie with the same name,            domain, and path as the newly created cookie.  (Notice that            this algorithm maintains the invariant that there is at most            one such cookie.)
        # 2.  If the newly created cookie was received from a "non-HTTP"            API and the old-cookie’s http-only-flag is set, abort these            steps and ignore the newly created cookie entirely.
        # 3.  Update the creation-time of the newly created cookie to            match the creation-time of the old-cookie.
        # 4.  Remove the old-cookie from the cookie store.
 


#"Cookie: BIGipServer~Public~vs-onlinechannel2.ext.wd.govt.nz_443.app~vs-onlinechannel2.ext.wd.govt.nz_443_pool=rd1906o00000000000000000000ffff0ae82285o80; TS013d8ed5=0105b6b7b66d6b29124893459b055cd1f4a5a7335b12046ffe1a55a0b1d7c59a2898116c3630e396b30c74f7a246bceef6f531669bc27c85ed400d8f7a5caa16c9e4bbe36ec00851c66cab0d5c90325df26f2234f1; TSPD_101=08819c2a25ab28002cfb583c7dbacbe5871ed5c87ecb3f59eb3a88cabd414fc824ba07b50c9ffc25ee5cd77337f984e508c7223e67051000d70c291105bfdc6e9483047df012ed90:; __RequestVerificationToken=h835fLFxEuqhkzpklhfFifRibVRTPPcgTAcOQqYS4usAV_20QUDv-fpkYg9z7YRTyXJFzmqLNoi0nelpGLtGmZQaBy41"

#Unless the cookie’s attributes indicate otherwise, the cookie is   returned only to the origin server (and not, for example, to any   subdomains), and it expires at the end of the current session (as   defined by the user agent).  User agents ignore unrecognized cookie   attributes (but not the entire cookie).


# (
  # 'Set-Cookie',
  # 'BIGipServer~Public~vs-onlinechannel2.ext.wd.govt.nz_443.app~vs-onlinechannel2.ext.wd.govt.nz_443_pool=rd1906o00000000000000000000ffff0ae82284o80; path=/'
 # ),
 # (
  # 'Set-Cookie',
  # 'TS013d8ed5=0105b6b7b661820adb08f47c5ea240ddfc5866334894c224bcaa1865eb72664797ad1905f3d90d64182687996238bb77e476bd5daa7bfa3381cca3fff2f42dba045a7bb096; Path=/; Secure; HTTPOnly'
 # )



#Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epaxjzubchbotfbwr5te1gwf









import os
import time
import json
import urllib.parse
import elist.elist as elel
from kukibanshee import rfc6265
from kukibanshee import drone
from kukibanshee import nozdormu
from kukibanshee.Resources import public_suffixes as pub
#pub.PUBLICSUFFIXES

#
class originException(Exception):
    pass

# 
SETCKREJECTLOG = {
    'origin':'server url of the response not in domain',
    'public_suffix':'the domain is a public_suffix',
}

INVALIDLOG = {
    'expiry':'the Cookie expired',
    'domain':'dst_url netloc not in Cookie Domain',
    'path':'dst_url path not in Cookie Path',
    'secure':'dst_url only for https'
}

def new_cookie():
    Cookie = {
        'origin':None,
        'Expires':None,
        'Max-Age':None,
        'Domain':None,
        'Path':None,
        'Secure':None,
        'HttpOnly':None,
        'extension-av':None,
        'name':None,  
        'value':None,
        'expiry-time':None,
        'creation-time':None, 
        'last-access-time': None,
        'persistent-flag': False,
        'host-only-flag': False, 
        'secure-only-flag':False,
        'http-only-flag':False,
        'unquote':False,
        'unquote_plus':False,
        '_req-type':'Cookie',
        '_resp-type':'Set-Cookie',
        '_reject':False,
        '_reject_reason':None,
    }
    return(Cookie)

def fillCookieDomain(Cookie,domain,**kwargs):
    '''
        Page20 Let cookie-domain be the attribute-value without the leading %x2E (".") character
        
        "If the server omits the Domain attribute, the user 
        agent will return the cookie only to the origin server"
        
        4.1.2.3
            The user agent will reject cookies unless the Domain attribute
            specifies a scope for the cookie that would include the origin server.
            For example, the user agent will accept a cookie with a 
            Domain attribute of "example.com" or of "foo.example.com" from 
            foo.example.com, but the user agent will not accept a cookie with a 
            Domain attribute of "bar.example.com" or of "baz.foo.example.com".

            For security reasons, many user agents are configured to reject
            Domain attributes that correspond to "public suffixes".
        
        4. If the cookie-attribute-list contains an attribute with an attribute-name of "Domain":
           Let the domain-attribute be the attribute-value of the last attribute in the 
           cookie-attribute-list with an attribute-name of "Domain".
           Otherwise:
               Let the domain-attribute be the empty string.
        
        5.  If the user agent is configured to reject "public suffixes" 
            and the domain-attribute is a public suffix:
                If the domain-attribute is identical to the canonicalized request-host:
                    Let the domain-attribute be the empty string.
            Otherwise:
                    Ignore the cookie entirely and abort these steps.
                    
            NOTE: A "public suffix" is a domain that is controlled by a public registry, 
            such as "com", "co.uk", and "pvt.k12.wy.us". 
            This step is essential for preventing attacker.com from disrupting the integrity 
            of example.com by setting a cookie with a Domain attribute of "com".  
            Unfortunately, the set of  public suffixes (also known as "registry controlled domains")
            changes over time.  If feasible, user agents SHOULD use an up-to-date public suffix list, 
            such as the one maintained by the Mozilla project at <http://publicsuffix.org/>.
        
        6.  If the domain-attribute is non-empty:
                If the canonicalized request-host does not domain-match the domain-attribute:
                    Ignore the cookie entirely and abort these steps.
                Otherwise:
                    Set the cookie’s host-only-flag to false.
                    Set the cookie’s domain to the domain-attribute.
            Otherwise:
                Set the cookie’s host-only-flag to true.
                Set the cookie’s domain to the canonicalized request-host.
 
    '''
    #必须有origin,必须是合法的origin
    origin = Cookie['origin']
    origin = rfc6265.format_origin(origin)
    cond_origin = rfc6265.is_domain_value(origin)
    if(cond_origin):
        pass
    else:
        raise originException('origin must be a valid domain or url with valid netloc')
    #######################33
    # Page20 Let cookie-domain be the attribute-value without the leading %x2E (".") character
    if(domain == None):
        pass
    else:
        domain = rfc6265.remove_domain_leading_dot(domain)
    # 检查origin(发送包含set-cookie的response的server_url,也就是你访问的web url)
    # 如果domain 不为空 ，必须包含origin 
    cond_domain = not((domain==None)|(domain == ''))
    if(cond_domain):
        valid_origin = rfc6265.origin_in_domain(origin,domain)
    else:
        valid_origin = True 
    if(valid_origin):
        pass
    else:
        Cookie['_reject'] = True
        Cookie['_reject_reason'] = 'origin'
        return(Cookie)
    #检查public_suffixes 
    if('reject_public' in kwargs):
        reject_public = kwargs['reject_public']
    else:
        reject_public = True
    if(reject_public):
        if(domain in pub.PUBLICSUFFIXES):
            Cookie['Domain'] = domain
            Cookie['_reject'] = True
            Cookie['_reject_reason'] = 'public_suffix'
            return(Cookie)
        else:
            pass
    else:
        pass
    #是否空Domain (host-only-flag)
    if((domain == None)|(domain == '')):
        Cookie['host-only-flag'] = True
        Cookie['Domain'] = origin 
    else:
        Cookie['host-only-flag'] = False
        Cookie['Domain'] = domain
    return(Cookie)

def fillCookieExpires(Cookie,expires,**kwargs):
    '''
        Let the expiry-time be the result of parsing the attribute-value as cookie-date (see Section 5.1.1).
        If the attribute-value failed to parse as a cookie date, ignore the cookie-av.
        
        If a cookie has both the Max-Age and the Expires attribute, the Max Age 
        attribute has precedence and controls the expiration date of the cookie. 
        If a cookie has neither the Max-Age nor the Expires attribute, 
        the user agent will retain the cookie until "the current session 
        is over" (as defined by the user agent).
    '''
    if((expires == None) | (expires == '')):
        pass
    else:
        if('disable_sane_check' in kwargs):
            disable_sane_check = kwargs['disable_sane_check']
        else:
            disable_sane_check = False
        if(disable_sane_check):
            Cookie['Expires'] = expires
            #Max-Age override Exipires
            if(Cookie['Max-Age']):
                pass
            else:
                Cookie['expiry-time'] = nozdormu.str2ts(expires)
                Cookie['persistent-flag'] = True
        else:
            if('mode' in kwargs):
                mode = kwargs['mode']
            else:
                mode = 'loose'
            cond = rfc6265.is_sane_cookie_date(expires,mode = mode)
            if(cond):
                Cookie['Expires'] = expires
                #Max-Age override Exipires
                if(Cookie['Max-Age']):
                    pass
                else:
                    Cookie['expiry-time'] = nozdormu.str2ts(expires)
                    Cookie['persistent-flag'] = True
            else:
                Cookie['Expires'] = None
                #Max-Age override Exipires
                if(Cookie['Max-Age']):
                    pass
                else:
                    Cookie['expiry-time'] = None
                    Cookie['persistent-flag'] = False
    return(Cookie)

def fillCookieMaxage(Cookie,maxage,**kwargs):
    '''
        If the first character of the attribute-value is not a DIGIT or a "-" character, 
        ignore the cookie-av.
        #cant understand why minus Max-Age permitted, not support this secarino
        
        If the remainder of attribute-value contains a non-DIGIT character,
        ignore the cookie-av.
        Let delta-seconds be the attribute-value converted to an integer.
        If delta-seconds is less than or equal to zero (0), let expiry-time
        be the earliest representable date and time.  
        Otherwise, let the expiry-time be the current date and time plus delta-seconds seconds.
    '''
    if(maxage == None):
        pass
    else:
        cond = rfc6265.is_max_age_value(maxage)
        if(cond):
            Cookie['Max-Age'] = maxage
            if(Cookie['creation-time']):
                Cookie['expiry-time'] = Cookie['creation-time'] + int(maxage)
            else:
                Cookie['expiry-time'] = time.time() + int(maxage)
            Cookie['persistent-flag'] = True
        else:
            Cookie['Max-Age'] = None
            #dont modify the expiry-time, it maybe setby Expires
            #dont modify the persistant-flag, it maybe setby Expires
    return(Cookie)

def fillCookieSecure(Cookie,secure):
    Cookie['Secure'] = secure
    if(secure):
        Cookie['secure-only-flag'] = True
    else:
        Cookie['secure-only-flag'] = False
    return(Cookie)

def fillCookieHttpOnly(Cookie,httponly):
    Cookie['HttpOnly'] = httponly
    if(httponly):
        Cookie['http-only-flag'] = True
    else:
        Cookie['http-only-flag'] = False
    return(Cookie)

def fillCookiePath(Cookie,path,**kwargs):
    '''
        If the cookie-attribute-list contains an attribute with an attribute-name of "Path", 
        set the cookie’s path to attribute value of the last attribute in the cookie-attribute-list 
        with an attribute-name of "Path".  
        Otherwise, set the cookie’s path to the default-path of the request-uri.
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'strict'
    if(path == None):
        Cookie['Path'] = rfc6265.format_path(urllib.parse.urlparse(dst_url).path,mode=mode)
        
    else:
        Cookie['Path'] = path
    return(Cookie)

def extension_handler(extension_av,**kwargs):
    '''
        Not Implemented
    '''
    return(extension_av)

def setckdict2Cookie(setckdict,**kwargs):
    '''
        2.
            Create a new cookie with name cookie-name, value cookie-value.
            Set the creation-time and the last-access-time to the currentdate and time
        
        3.  If the cookie-attribute-list contains an attribute with an attribute-name of "Max-Age":
                Set the cookie’s persistent-flag to true.
                Set the cookie’s expiry-time to attribute-value of the last attribute 
                in the cookie-attribute-list with an attribute-name of "Max-Age".
            Otherwise, if the cookie-attribute-list contains an attribute with an attribute-name of "Expires" 
            (and does not contain an attribute with an attribute-name of "Max-Age"):
                Set the cookie’s persistent-flag to true.
                Set the cookie’s expiry-time to attribute-value of the last 
                attribute in the cookie-attribute-list with an attribute-name of "Expires".
            Otherwise:
                Set the cookie’s persistent-flag to false.
    '''
    #for further check ,must input origin(server netloc or server_url )
    origin = kwargs['origin']
    origin = rfc6265.format_origin(origin)
    cond_origin = rfc6265.is_domain_value(origin)
    if(cond_origin):
        pass
    else:
        raise originException('origin must be a valid domain or url with valid netloc')
    ####
    name = drone.get_ckavalue(setckdict,'name')
    value = drone.get_ckavalue(setckdict,'value')
    expires = drone.get_ckavalue(setckdict,'Expires')
    maxage = drone.get_ckavalue(setckdict,'Max-Age')
    domain = drone.get_ckavalue(setckdict,'Domain')
    path = drone.get_ckavalue(setckdict,'Path')
    secure = drone.get_ckavalue(setckdict,'Secure')
    httponly = drone.get_ckavalue(setckdict,'HttpOnly')
    extension = drone.get_ckavalue(setckdict,'extension-av')
    # if('mode' in kwargs):
        # mode = kwargs['mode']
    # else:
        # mode = 'loose'
    ck = new_cookie()
    ck['origin'] = origin
    ck['name'] = name
    ck['value'] = value
    ck['creation-time'] = time.time()
    ck['last-access-time'] = ck['creation-time']
    fillCookieDomain(ck,domain,origin=origin)
    fillCookieExpires(ck,expires)
    #If Max-Age exist,let the Max-Age override Expires
    fillCookieMaxage(ck,maxage)
    fillCookiePath(ck,path)
    fillCookieSecure(ck,secure)
    fillCookieHttpOnly(ck,httponly)
    ck['extension-av'] = extension
    if('unquote' in kwargs):
        ck['unquote'] = kwargs['unquote']
    else:
        ck['unquote'] = True
    if('unquote_plus' in kwargs):
        ck['unquote_plus'] = kwargs['unquote_plus']
    else:
        ck['unquote_plus'] = True
    return(ck)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def setckstr2Cookie(setckstr,origin):
    setckdict = drone.str2setckdict(setckstr)
    ck = setckdict2Cookie(setckdict,origin=origin)
    return(ck)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def read_file_content(**kwargs):
    fd = open(kwargs['fn'],kwargs['op'])
    rslt = fd.read()
    fd.close()
    return(rslt)

def write_to_file(**kwargs):
    fd = open(kwargs['fn'],kwargs['op'])
    fd.write(kwargs['content'])
    fd.close()

def cond_persistant(ck):
    '''
    '''
    persistant = ck['persistant-flag']
    return(persistant)

def cond_expired(ck):
    '''
    '''
    ####
    expiry = ck['expiry-time']
    if(expiry == None):
        cond = False 
    else:
        now = time.time()
        cond = (now >= expiry)
    if(cond):
        print(INVALIDLOG['expiry'])
    else:
        pass
    return(cond)

def cond_domain(ck,server):
    '''
        The cookie’s host-only-flag is true and the canonicalized request-host is 
        identical to the cookie’s domain.

        The cookie’s host-only-flag is false and the canonicalized request-host 
        domain-matches the cookie’s domain.
    '''
    if(ck['host-only-flag']):
        cond = (server == ck['Domain'])
    else:
        cond = rfc6265.domain_in_domain(server,ck['Domain'])
    if(cond):
        pass
    else:
        print(INVALIDLOG['domain'])
    return(cond)

def cond_path(ck,path):
    '''
        The request-uri’s path path-matches the cookie’s path.
    '''
    cond = rfc6265.path_in_path(path,ck['Path'])
    if(cond):
        pass
    else:
        print(INVALIDLOG['path'])
    return(cond)

def cond_secure(ck,scheme):
    '''
    '''
    if(ck['secure-only-flag']):
        cond = (scheme == 'https')
    else:
        cond = True
    if(cond):
        pass
    else:
        print(INVALIDLOG['secure'])
    return(cond)


#ck        Cookie.ck     是一个dict
#ckl       cookie-list   

def sort_ckl(ckl,**kwargs):
    '''
        Cookies with longer paths are listed before cookies with shorter paths.
        Among cookies that have equal-length path fields, cookies with earlier creation-times are 
        listed before cookies with later creation-times
    '''
    def add_plen(ele):
        if(ele['Path'] == None):
            ele['plen'] = 0
        else:
            ele['plen'] = ele['Path'].__len__()
    def del_plen(ele):
        del ele['plen']
    ckl = elel.array_map(ckl,add_plen)
    ckl = elel.sortDictList(ckl,['plen','creation-time'])
    ckl = elel.array_map(ckl,del_plen)
    return(ckl)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def slctckpair(ck,dst_url):
        '''
            get valid ckpair for dst_url
        '''
        rslt = urllib.parse.urlparse(dst_url)
        scheme = rslt.scheme
        netloc = rslt.netloc
        path = rslt.path
        cond1 = not(cond_expired(ck))
        cond2 = cond_domain(ck,netloc)
        cond3 = cond_path(ck,path)
        cond4 = cond_secure(ck,scheme)
        cond = (cond1 & cond2 & cond3 & cond4)
        if(cond):
            if(ck['unquote']):
                if(ck['unquote_plus']):
                    name = urllib.parse.quote_plus(ck['name'])
                    value = urllib.parse.quote_plus(ck['value'])
                else:
                    name = urllib.parse.quote(ck['name'])
                    value = urllib.parse.quote(ck['value'])
            else:
                name = ck['name']
                value = ck['value']
            ckpair = drone.nv2ckpair(name,value)
            return(ckpair)
        else:
            return(None)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def ckl2ckstr(ckl,dst_url):
    ckpl = elel.array_map(ckl,slctckpair,dst_url)
    ckstr = drone.pl2ckstr(ckpl)
    return(ckstr)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

ANADBPATH = '/opt/PY/PY3/kukibashee/kukibanshee/Resources/anadb.json'
JARDBPATH = '/opt/PY/PY3/kukibashee/kukibanshee/Resources/jardb.json'

class Cookie():
    '''
        wait-for-implement:
             Update the last-access-time of each cookie in the cookie-list to 
             the current date and time
    '''
    def __init__(self,setck,**kwargs):
        origin = kwargs['origin']
        if('unquote' in kwargs):
            unquote = kwargs['unquote']
        else:
            unquote = False
        if('unquote_plus' in kwargs):
            unquote_plus = kwargs['unquote_plus']
        else:
            unquote_plus = False
        if(unquote):
            setck = drone.unquote_setck(setck,plus = unquote_plus)
        else:
            pass
        setckdict = drone.split_setck(setck)['setckdict']
        self.ck = setckdict2Cookie(setckdict,unquote=unquote,unquote_plus=unquote_plus,origin=origin)
    def __repr__(self):
        return(self.ck.__str__())
    def ckpair(self,**kwargs):
        '''
            get valid ckpair for dst_url
        '''
        dst_url = kwargs['url']
        rslt = urllib.parse.urlparse(dst_url)
        scheme = rslt.scheme
        netloc = rslt.netloc
        cond1 = not(cond_expired(self.ck))
        cond2 = cond_domain(self.ck,netloc)
        cond3 = cond_path(self.ck,path)
        cond4 = cond_secure(self.ck,scheme)
        cond = (cond1 & cond2 & cond3 & cond4)
        if(cond):
            if(self.ck['unquote']):
                if(self.ck['unquote_plus']):
                    name = urllib.parse.quote_plus(self.ck['name'])
                    value = urllib.parse.quote_plus(self.ck['value'])
                else:
                    name = urllib.parse.quote(self.ck['name'])
                    value = urllib.parse.quote(self.ck['value'])
            else:
                name = self.ck['name']
                value = self.ck['value']
            ckpair = drone.nv2ckpair(name,value)
            return(ckpair)
        else:
            return(None)
    ###############################
    def save2mem(self,**kwargs):
        '''
            保存到in-mem jar 中 ，in-mem jar 是一个由Cookie(ck) 构成的数组cookie-list 
        '''
        inmem_jar = kwargs['jar']
        if(self.ck['_reject'] == True):
            print("No store rejected")
        elif(self.ck['persistant-flag'] == True):
            cond = (self.ck['expiry-time']<=time.time())
            print("No store expired persistant ")
        else:
            inmem_jar.cks = elel.cond_remove_all(inmem_jar.cks,cond_func=cond_expired)
            inmem_jar.cks.append(self.ck)
            inmem_jar.cks = sort_ckl(ckl)
    @classmethod
    def save_ck(cls,Cookie,myDir):
        '''
        '''
        if(os.path.exists(myDir)):
            content = read_file_content(fn=myDir,op='r+')
            arr = json.loads(content)
            arr.append(Cookie)
            arr = sort_ckl(arr)
            write_to_file(fn=myDir,content=json.dumps(arr),op='w+')
        else:
            arr = [Cookie]
            write_to_file(fn=myDir,content=json.dumps(arr),op='w+')
    def save2file(self,**kwargs):
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'analysis'
        if(mode == 'analysis'):
            if('myDir' in kwargs):
                myDir = kwargs['myDir']
            else:
                myDir = ANADBPATH
            save_ck(self.ck,myDir)
        else:
            # for jar 
            if('myDir' in kwargs):
                myDir = kwargs['myDir']
            else:
                myDir = JARDBPATH
            if(self.ck['_reject'] == True):
                print("No save rejected Cookie to jar,only to ana")
            elif(self.ck['persistant-flag'] == False):
                print("No store non-persistant into jar file")
            elif(self.ck['persistant-flag'] == True):
                cond = (self.ck['expiry-time']<=time.time())
                print("No store expired persistant ")
            else:
                save_ck(self.ck,myDir)


class Jar():
    '''
        cks : Cookies 
    '''
    def __init__(self,**kwargs):
        self.cks = []
    def loads(self,myDir):
        if(os.path.exists(myDir)):
            content = read_file_content(fn=myDir,op='r+')
            arr = json.loads(content)
            arr = elel.cond_select_all(arr,cond_func=cond_persistant)
            arr = elel.cond_remove_all(arr,cond_func=cond_expired)
        else:
            arr = []
        self.cktl.extend(arr)
    ####
    def remove_non_persistant(self):
        '''
            should only save persistant-flag setted Cookie into jar
        '''
        self.cks = elel.cond_select_all(self.cks,cond_func=cond_persistant)
        self.cks = sort_ckl(arr)
    def remove_expired(self):
        '''
            The user agent MUST evict all expired cookies from the cookie store if, 
            at any time, an expired cookie exists in the cookie store
        '''
        self.cks = elel.cond_remove_all(self.cks,cond_func=cond_expired)
        self.cks = sort_ckl(arr)
    ####
    @classmethod
    def save_ckl(cls,ckl,myDir):
        '''
        '''
        if(os.path.exists(myDir)):
            content = read_file_content(fn=myDir,op='r+')
            arr = json.loads(content)
            arr.extend(ckl)
            arr = elel.cond_select_all(arr,cond_func=cond_persistant)
            arr = elel.cond_remove_all(arr,cond_func=cond_expired)
            arr = sort_ckl(arr)
            write_to_file(fn=myDir,content=json.dumps(arr),op='w+')
        else:
            arr = ckl
            arr = elel.cond_select_all(arr,cond_func=cond_persistant)
            arr = elel.cond_remove_all(arr,cond_func=cond_expired)
            write_to_file(fn=myDir,content=json.dumps(arr),op='w+')
    ####
    def save(self,**kwargs):
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'analysis'
        if(mode == 'analysis'):
            if('myDir' in kwargs):
                myDir = kwargs['myDir']
            else:
                myDir = ANADBPATH
            save_ckl(ckl,myDir)
        else:
            if('myDir' in kwargs):
                myDir = kwargs['myDir']
            else:
                myDir = JARDBPATH
            save_ckl(ckl,myDir)
    ####
    def ckpl(self,**kwargs):
        dst_url = kwargs['url']
        ckpl = elel.array_map(setcktl,lambda setck:Cookie(setck).ckpair(url=dst_url))
        return(ckpl)
    def ckstr(self,**kwargs):
        dst_url = kwargs['url']
        ckpl = elel.array_map(setcktl,lambda setck:Cookie(setck).ckpair(url=dst_url))
        ckstr = drone.list2ckstr(ckpl)
        return(ckstr)
    @classmethod
    def setcktl2ckstr(cls,setcktl,**kwargs):
        '''
        '''
        dst_url = kwargs['url']
        ckpl = elel.array_map(setcktl,lambda setck:Cookie(setck).ckpair(url=dst_url))
        ckstr = drone.list2ckstr(ckpl)
        return(ckstr)


####################################################################
# 当组成一个用于request 的ckheader 时，来源有三个
# 1. 多个 set-cookie-header  in response : setcktl2ckstr  Jar.ckstr
# 2. cookie-pair in javascript
# 3. Jar : Jar.loads 
#####################################################################    

############################################################
#------------wait for implement hierachy jar------------------
#jar
#    ----domain1
#            ----path11
#    ----domain12
#            ----path21
#            ----path22
##############################################################

#5.3. Storage Model
 # The user agent stores the following fields about each cookie: name,
 # value, expiry-time, domain, path, creation-time, last-access-time,
 # persistent-flag, host-only-flag, secure-only-flag, and http-only
# flag.
 # When the user agent "receives a cookie" from a request-uri with name
 # cookie-name, value cookie-value, and attributes cookie-attribute
# list, the user agent MUST process the cookie as follows:
 # 1. A user agent MAY ignore a received cookie in its entirety. For
 # example, the user agent might wish to block receiving cookies
 # from "third-party" responses or the user agent might not wish to
 # store cookies that exceed some size.
# 2. Create a new cookie with name cookie-name, value cookie-value.
 # Set the creation-time and the last-access-time to the current
 # date and time.
 # 3. If the cookie-attribute-list contains an attribute with an
 # attribute-name of "Max-Age":
 # Set the cookie’s persistent-flag to true.
 # Set the cookie’s expiry-time to attribute-value of the last
 # attribute in the cookie-attribute-list with an attribute-name
 # of "Max-Age".
 # Otherwise, if the cookie-attribute-list contains an attribute
 # with an attribute-name of "Expires" (and does not contain an
 # attribute with an attribute-name of "Max-Age"):
 # Set the cookie’s persistent-flag to true.
 # Set the cookie’s expiry-time to attribute-value of the last
 # attribute in the cookie-attribute-list with an attribute-name
 # of "Expires".
 # Otherwise:
 # Set the cookie’s persistent-flag to false.
 # Set the cookie’s expiry-time to the latest representable
 # date.
 # 4. If the cookie-attribute-list contains an attribute with an
 # attribute-name of "Domain":
 # Let the domain-attribute be the attribute-value of the last
 # attribute in the cookie-attribute-list with an attribute-name
 # of "Domain".
 # Otherwise:
 # Let the domain-attribute be the empty string.
 # 5. If the user agent is configured to reject "public suffixes" and
 # the domain-attribute is a public suffix:
 # If the domain-attribute is identical to the canonicalized
 # request-host:
 # Let the domain-attribute be the empty string.
 # Otherwise:
 # Ignore the cookie entirely and abort these steps.
 # NOTE: A "public suffix" is a domain that is controlled by a
 # public registry, such as "com", "co.uk", and "pvt.k12.wy.us".
 # This step is essential for preventing attacker.com from
 # disrupting the integrity of example.com by setting a cookie
 # with a Domain attribute of "com". Unfortunately, the set of
 # public suffixes (also known as "registry controlled domains")
 # changes over time. If feasible, user agents SHOULD use an
 # up-to-date public suffix list, such as the one maintained by
 # the Mozilla project at <http://publicsuffix.org/>.
 # 6. If the domain-attribute is non-empty:
 # If the canonicalized request-host does not domain-match the
 # domain-attribute:
 # Ignore the cookie entirely and abort these steps.
 # Otherwise:
 # Set the cookie’s host-only-flag to false.
 # Set the cookie’s domain to the domain-attribute.
 # Otherwise:
 # Set the cookie’s host-only-flag to true.
 # Set the cookie’s domain to the canonicalized request-host.
 # 7. If the cookie-attribute-list contains an attribute with an
 # attribute-name of "Path", set the cookie’s path to attribute
# value of the last attribute in the cookie-attribute-list with an
 # attribute-name of "Path". Otherwise, set the cookie’s path to
 # the default-path of the request-uri.
 # 8. If the cookie-attribute-list contains an attribute with an
 # attribute-name of "Secure", set the cookie’s secure-only-flag to
 # true. Otherwise, set the cookie’s secure-only-flag to false.
 # 9. If the cookie-attribute-list contains an attribute with an
 # attribute-name of "HttpOnly", set the cookie’s http-only-flag to
 # true. Otherwise, set the cookie’s http-only-flag to false.
# 10. If the cookie was received from a "non-HTTP" API and the
 # cookie’s http-only-flag is set, abort these steps and ignore the
 # cookie entirely.
 # 11. If the cookie store contains a cookie with the same name,
 # domain, and path as the newly created cookie:
 # 1. Let old-cookie be the existing cookie with the same name,
 # domain, and path as the newly created cookie. (Notice that
 # this algorithm maintains the invariant that there is at most
 # one such cookie.)
 # 2. If the newly created cookie was received from a "non-HTTP"
 # API and the old-cookie’s http-only-flag is set, abort these
 # steps and ignore the newly created cookie entirely.
 # 3. Update the creation-time of the newly created cookie to
 # match the creation-time of the old-cookie.
 # 4. Remove the old-cookie from the cookie store.
 # 12. Insert the newly created cookie into the cookie store.
 # A cookie is "expired" if the cookie has an expiry date in the past.
 # The user agent MUST evict all expired cookies from the cookie store
 # if, at any time, an expired cookie exists in the cookie store.
 # At any time, the user agent MAY "remove excess cookies" from the
 # cookie store if the number of cookies sharing a domain field exceeds
 # some implementation-defined upper bound (such as 50 cookies).
 # At any time, the user agent MAY "remove excess cookies" from the
 # cookie store if the cookie store exceeds some predetermined upper
 # bound (such as 3000 cookies).
 # When the user agent removes excess cookies from the cookie store, the
 # user agent MUST evict cookies in the following priority order:
 # 1. Expired cookies.
 # 2. Cookies that share a domain field with more than a predetermined
 # number of other cookies.
 # 3. All cookies.
 # If two cookies have the same removal priority, the user agent MUST
 # evict the cookie with the earliest last-access date first.
 # When "the current session is over" (as defined by the user agent),
 # the user agent MUST remove from the cookie store all cookies with the
 # persistent-flag set to false.


 

import elist.elist as elel
import tlist.tlist as tltl
from kukibanshee import rfc6265
import re
import copy
import urllib.parse




def help():
    if(func_name == ''):
        doc = '''
            >>> from kukibanshee.drone import *
            >>> ckpair = "TS=0105b666"
            >>> ckpt = ckpair2tuple(ckpair)
            >>> ckpt
            ('TS', '0105b666')
            >>>
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)
    elif(func_name == ''):
        doc = '''
        '''
        print(doc)


VALIDATEFUNCS = {
    'name': rfc6265.is_cookie_name,
    'value': rfc6265.is_cookie_value,
    'Expires': rfc6265.is_expires_av,
    'Max-Age': rfc6265.is_maxage_av,
    'Path': rfc6265.is_path_av,
    'Domain': rfc6265.is_domain_av,
    'Secure': rfc6265.is_secure_av,
    'HttpOnly': rfc6265.is_httponly_av,
    'extension-av':rfc6265.is_extension_av
}

SEPARATORS = {
    'ckheader':': ',
    'ckstr':'; ',
    'ckpair':'=',
    'setckheader':': ',
    'setckstr':'; ',
    'ckav':'='
}

TYPES = {
    'cktype': "Cookie",
    'setcktype': "Set-Cookie"
}

CKAVNAMES = ['Expires','Max-Age','Domain','Path','Secure','HttpOnly']
CKAVLOWERNAMES = ['expires','max-age','domain','path','secure','httponly']


#ckheader              cookie-header              "Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax"
#cktype                cookie-type                "Cookie"
#ckstr                 cookie-string              "BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epaxjzubchbotfbwr5te1gwf"
#ckpair                cookie-pair                "TS=0105b666"
#ckname                cookie-name                "TS"
#ckvalue               cookie-value               "0105b666"
#cknv                  cookie-name-and-value      "TS","0105b666"
#ckpt                  cookie-pairTuple           ("TS","0105b666")
#ckpd                  cookie-pairDict            {"TS":"0105b666"}
#ckele                 cookie-element             ckpair | cknv | ckpt | ckpd
#ckpl                  cookie-pair-list           ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epaxjzubchbotfbwr5te1gwf']
#ckpdl                 cookie-pair-dictList       [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
#ckptl                 cookie-pair-tupleList      [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
#ckdict                cookie-dict  
#ckbody                cookie-body                ckstr | ckpl | ckptl | ckpdl | ckdict
              

#Part.1  cookie-pair
#命名规则priority ckele > ckpair > cknv > ckpt > ckpd
#[ckpair2tuple,tuple2ckpair,ckpair2nv,nv2ckpair,ckpair2dict,dict2ckpair,cknv2tuple,tuple2cknv,cknv2dict,dict2cknv,ckpt2dict,dict2ckpt]
# ['ckpair2tuple', 'tuple2ckpair', 'ckpair2nv', 'nv2ckpair', 'ckpair2dict', 'dict2ckpair', 'cknv2tuple', 'tuple2cknv', 'cknv2dict', 'dict2cknv', 'ckpt2dict', 'dict2ckpt']
# [
#     ckpair2tuple,
#     tuple2ckpair,
#     ckpair2nv,
#     nv2ckpair,
#     ckpair2dict,
#     dict2ckpair,
#     cknv2tuple,
#     tuple2cknv,
#     cknv2dict,
#     dict2cknv,
#     ckpt2dict,
#     dict2ckpt
# ]

def ckpair2tuple(ckpair):
    '''
        from kukibanshee.drone import *
        ckpair = "TS=0105b666"
        ckpt = ckpair2tuple(ckpair)
        ckpt
        ckpair = "TS=rc=1&ef=2"
        ckpt = ckpair2tuple(ckpair)
        ckpt
    '''
    eq_loc = ckpair.index("=")
    ckname = ckpair[:eq_loc]
    ckvalue = ckpair[(eq_loc+1):]
    ckpt = (ckname,ckvalue)
    return(ckpt)

def tuple2ckpair(ckpt):
    '''
        ckpt = ("TS","0105b666")
        ckpair = tuple2ckpair(ckpt)
        ckpair
    '''
    ckname,ckvalue = ckpt
    ckpair = ckname+ SEPARATORS['ckpair'] +ckvalue
    return(ckpair)

def ckpair2nv(ckpair):
    '''
        ckpair = "TS=0105b666"
        ckname,ckvalue = ckpair2nv(ckpair)
        ckname
        ckvalue
    '''
    return(ckpair2tuple(ckpair))

def nv2ckpair(ckname,ckvalue):
    '''
        ckname = "TS"
        ckvalue = "0105b666"
        ckpair = nv2ckpair(ckname,ckvalue)
        ckpair
    '''
    return(tuple2ckpair((ckname,ckvalue)))

def ckpair2dict(ckpair):
    '''
        ckpair = "TS=0105b666"
        ckpd = ckpair2dict(ckpair)
        pobj(ckpd)
    '''
    ckname,ckvalue = ckpair2nv(ckpair)
    return({ckname:ckvalue})

def dict2ckpair(ckpd):
    '''
        ckpd = {"TS": "0105b666"}
        ckpair = dict2ckpair(ckpd)
        ckpair
    '''
    ckname = list(ckpd.keys())[0]
    ckvalue = list(ckpd.values())[0]
    return(nv2ckpair(ckname,ckvalue))

def cknv2tuple(ckname,ckvalue):
    '''
        ckname = "TS"
        ckvalue = "0105b666"
        ckpt = cknv2tuple(ckname,ckvalue)
        ckpt
    '''
    return((ckname,ckvalue))

def tuple2cknv(ckpt):
    '''
        ckpt = ("TS","0105b666")
        ckname,ckvalue = tuple2cknv(ckpt)
        ckname
        ckvalue
    '''
    return(ckpt)

def cknv2dict(ckname,ckvalue):
    '''
        ckname = "TS"
        ckvalue = "0105b666"
        ckpd = cknv2dict(ckname,ckvalue)
        ckpd
    '''
    return({ckname : ckvalue})

def dict2cknv(ckpd):
    '''
        ckpd = {"TS": "0105b666"}
        ckname,ckvalue = dict2cknv(ckpd)
        ckname
        ckvalue
    '''
    ckname = list(ckpd.keys())[0]
    ckvalue = list(ckpd.values())[0]
    return((ckname,ckvalue))

def ckpt2dict(ckpt):
    '''
        ckpt = ("TS","0105b666")
        ckpd = ckpt2dict(ckpt)
        pobj(ckpd)
    '''
    ckname,ckvalue = ckpt
    return({ckname:ckvalue})

def dict2ckpt(ckpd):
    '''
        ckpd = {"TS": "0105b666"}
        ckpt = dict2ckpt(ckpd)
        ckpt 
    '''
    return(dict2cknv(ckpd))

#validate_ckpt
def validate_ckpt(ckpt):
    '''
    '''
    if(type(ckpt) == type(())):
        ckname,ckvalue = tuple2cknv(ckpt)
        cond1 = rfc6265.is_cookie_name(ckname)
        cond2 = rfc6265.is_cookie_value(ckvalue)
        return(cond1 & cond2)        
    else:
        return(False)

def validate_ckpd(ckpd):
    ckpt = dict2ckpt(ckpd)
    return(validate_ckpt(ckpt))

def validate_ckpair(ckpair):
    ckpt = ckpair2tuple(ckpair)
    return(validate_ckpt(ckpt))

def validate_cknv(ckname,ckvalue):
    ckpt = cknv2tuple(ckname,ckvalue)
    return(validate_ckpt(ckpt))

def validate_ckele(ckele,*args):
    ckpt = ckele2pt(ckele,*args)
    return(validate_ckpt(ckpt))

#cookie-element
def detect_ckele(ckele,*args):
    '''
        ckele = "TS=0105b666"
        detect_ckele(ckele)
        ckele = ("TS","0105b666")
        detect_ckele(ckele)
        ckele = {"TS": "0105b666"}
        detect_ckele(ckele)
        ckname = "TS"
        ckvalue = "0105b666"
        detect_ckele(ckname,ckvalue)
    '''
    length = args.__len__()
    if(length == 0):
        if(type(ckele) == type('')):
            return('ckpair')
        elif(type(ckele) == type(())):
            return('ckpt')
        elif(type(ckele) == type(dict({}))):
            return('ckpd')
        else:
            return('unknown')
    elif(length == 1):
        return('cknv')
    else:
        return('unknown')

def ckele2pt(ckele,*args):
    '''
        ckele = "TS=0105b666"
        ckpt = ckele2pt(ckele)
        pobj(ckpt)
        ckele = ("TS","0105b666")
        ckpt = ckele2pt(ckele)
        pobj(ckpt)
        ckele = {"TS": "0105b666"}
        ckpt = ckele2pt(ckele)
        pobj(ckpt)
        ckname = "TS"
        ckvalue = "0105b666"
        ckpt = ckele2pt(ckname,ckvalue)
        pobj(ckpt)
    '''
    mode = detect_ckele(ckele,*args)
    if(mode == 'ckpair'):
        ckpt = ckpair2tuple(ckele)
    elif(mode == 'ckpt'):
        ckpt = ckele
    elif(mode == 'ckpd'):
        ckpt = dict2ckpt(ckele)
    elif(mode == 'ckname'):
        return(ckele,args[0])
    else:
        print("unknown ")
        return(None)
    return(ckpt)

#
def convert_ckele(ckele,*args,**kwargs):
    '''
        ckele = "TS=0105b666"
        ckpt = convert_ckele(ckele,mode='ckpt')
        pobj(ckpt)
        ckele = ("TS","0105b666")
        ckpair = convert_ckele(ckele,mode='ckpair')
        pobj(ckpair)
        ckele = {"TS": "0105b666"}
        ckname,ckvalue = convert_ckele(ckele,mode='cknv')
        ckname
        ckvalue
        ckname = "TS"
        ckvalue = "0105b666"
        ckpd = convert_ckele(ckname,ckvalue,mode='ckpd')
        pobj(ckpd)
    '''
    if('validate' in kwargs):
        valid = validate_ckele(ckele)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckele')
        return(None)
    mode = detect_ckele(ckele,*args)
    if(mode == 'ckpair'):
        ckpt = ckpair2tuple(ckele)
    elif(mode == 'ckpt'):
        ckpt = ckele
    elif(mode == 'ckpd'):
        ckpt = dict2ckpt(ckele)
    elif(mode == 'cknv'):
        ckpt = cknv2tuple(ckele,args[0])
    else:
        print("unknow mode")
        return(None)
    if('mode' in kwargs):
        to_mode = kwargs['mode']
    else:
        to_mode = 'ckpt'
    if(to_mode == 'ckpair'):
        ckele = tuple2ckpair(ckpt)
    elif(to_mode == 'ckpt'):
        ckele = ckpt
    elif(to_mode == 'ckpd'):
        ckele = ckpt2dict(ckpt)
    elif(to_mode == 'cknv'):
        ckname,ckvalue = tuple2cknv(ckpt)
        return((ckname,ckvalue))
    else:
        print("unknow mode")
        return(None)
    return(ckele)


#Part.2 cookie-string
#命名规则priority ckstr > ckpl > ckptl > ckpdl > ckdict

#ckstr2pl             ckstr2list
#pl2ckstr             list2ckstr
#ckstr2ptl            ckstr2tupleList
#ptl2ckstr            tupleList2ckstr
#ckstr2pdl            ckstr2dictList
#pdl2ckstr            dictList2ckstr
#ckpl2ptl             ckpl2tupleList
#ptl2ckpl             tupleList2ckpl
#ckpl2pdl             ckpl2dictList
#pdl2ckpl             dictList2ckpl
#ckptl2pdl            ckptl2dictList
#pdl2ckptl            dictList2ckptl

##cookie-dict 不能保持原有次序,并且不允许重复key值,但是使用和阅读方便
#ckstr2dict          
#dict2ckstr       
#ckpl2dict
#dict2ckpl
#ckptl2dict
#dict2ckptl
#ckpdl2dict
#dict2ckpdl



# ABBREV 
#[ckstr2pl,pl2ckstr,ckstr2ptl,ptl2ckstr,ckstr2pdl,pdl2ckstr,ckpl2ptl,ptl2ckpl,ckpl2pdl,pdl2ckpl,ckptl2pdl,pdl2ckptl]
# [
#     ckstr2pl,
#     pl2ckstr,
#     ckstr2ptl,
#     ptl2ckstr,
#     ckstr2pdl,
#     pdl2ckstr,
#     ckpl2ptl,
#     ptl2ckpl,
#     ckpl2pdl,
#     pdl2ckpl,
#     ckptl2pdl,
#     pdl2ckptl
# ]
#[ckstr2list,list2ckstr,ckstr2tupleList,tupleList2ckstr,ckstr2dictList,dictList2ckstr,ckpl2tupleList,tupleList2ckpl,ckpl2dictList,dictList2ckpl,ckptl2dictList,dictList2ckptl]
#[
# ckstr2list,
# list2ckstr,
# ckstr2tupleList,
# tupleList2ckstr,
# ckstr2dictList,
# dictList2ckstr,
# ckpl2tupleList,
# tupleList2ckpl,
# ckpl2dictList,
# dictList2ckpl,
# ckptl2dictList,
# dictList2ckptl
#]

##cookie-dict 不能保持原有次序,并且不允许重复key值,但是使用和阅读方便
#[ckstr2dict,dict2ckstr,ckpl2dict,dict2ckpl,ckptl2dict,dict2ckptl,ckpdl2dict,dict2ckpdl]
# [
    # ckstr2dict,          
    # dict2ckstr,       
    # ckpl2dict,
    # dict2ckpl,
    # ckptl2dict,
    # dict2ckptl,
    # ckpdl2dict,
    # dict2ckpdl,
#]
#['ckstr2pl', 'pl2ckstr', 'ckstr2ptl', 'ptl2ckstr', 'ckstr2pdl', 'pdl2ckstr', 'ckpl2ptl', 'ptl2ckpl', 'ckpl2pdl', 'pdl2ckpl', 'ckptl2pdl', 'pdl2ckptl', 'ckstr2list', 'list2ckstr', 'ckstr2tupleList', 'tupleList2ckstr', 'ckstr2dictList', 'dictList2ckstr', 'ckpl2tupleList', 'tupleList2ckpl', 'ckpl2dictList', 'dictList2ckpl', 'ckptl2dictList', 'dictList2ckptl', 'ckstr2dict', 'dict2ckstr', 'ckpl2dict', 'dict2ckpl', 'ckptl2dict', 'dict2ckptl', 'ckpdl2dict', 'dict2ckpdl']


#转换规则: 所有结构转换为ckptl , 然后再由ckptl 转换为其他格式

def ckstr2pl(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ckstr2ckpl(ckstr)
        pobj(ckpl)
        #ckstr2list = ckstr2pl
    '''
    ckpl = ckstr.split(SEPARATORS['ckstr'])
    return(ckpl)

ckstr2list = ckstr2pl

def pl2ckstr(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckstr = pl2ckstr(ckpl)
        ckstr
        #list2ckstr
    '''
    ckstr = elel.join(ckpl,separator = SEPARATORS['ckstr'])
    return(ckstr)

list2ckstr = pl2ckstr

def ckstr2ptl(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckptl = ckstr2ptl(ckstr)
        pobj(ckptl)
        #ckstr2tupleList = ckstr2ptl
    '''
    ckpl = ckstr2pl(ckstr)
    ckptl = ckpl2ptl(ckpl)
    return(ckptl)

ckstr2tupleList = ckstr2ptl

def ptl2ckstr(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckstr = ptl2ckstr(ckptl)
        ckstr
        #tupleList2ckstr = ptl2ckstr
    '''
    ckpl = ptl2ckpl(ckptl)
    ckstr = pl2ckstr(ckpl)
    return(ckstr)

tupleList2ckstr = ptl2ckstr

def ckstr2pdl(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpdl = ckstr2pdl(ckstr)
        pobj(ckpdl)
        #ckstr2dictList = ckstr2pdl
    '''
    ckpl = ckstr2pl(ckstr)
    ckpdl = ckpl2pdl(ckpl)
    return(ckpdl)

ckstr2dictList = ckstr2pdl

def pdl2ckstr(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckstr = pdl2ckstr(ckpdl)
        ckstr
        #dictList2ckstr = pdl2ckstr
    '''
    ckpl = pdl2ckpl(ckpdl)
    ckstr = pl2ckstr(ckpl)
    return(ckstr)

dictList2ckstr = pdl2ckstr

def ckpl2ptl(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckptl = ckpl2ptl(ckpl)
        pobj(ckptl)
        #ckpl2tupleList = ckpl2ptl
    '''
    ckptl = elel.array_map(ckpl,ckpair2tuple)
    return(ckptl)

ckpl2tupleList = ckpl2ptl

def ptl2ckpl(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpl = ptl2ckpl(ckptl)
        pobj(ckpl)
        #tupleList2ckpl = ptl2ckpl
    '''
    ckpl = elel.array_map(ckptl,tuple2ckpair)
    return(ckpl)

tupleList2ckpl = ptl2ckpl

def ckpl2pdl(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckpdl = ckpl2pdl(ckpl)
        pobj(ckpdl)
        #ckpl2dictList = ckpl2pdl
    '''
    ckpdl = elel.array_map(ckpl,ckpair2dict)
    return(ckpdl)

ckpl2dictList = ckpl2pdl

def pdl2ckpl(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckpl = pdl2ckpl(ckpdl)
        pobj(ckpl)
        #dictList2ckpl = pdl2ckpl
    '''
    ckpl = elel.array_map(ckpdl,dict2ckpair)
    return(ckpl)

dictList2ckpl = pdl2ckpl

def ckptl2pdl(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = ckptl2pdl(ckptl)
        pobj(ckpdl)
        #ckptl2dictList = ckptl2pdl
    '''
    ckpdl = elel.array_map(ckptl,ckpt2dict)
    return(ckpdl)

ckptl2dictList = ckptl2pdl

def pdl2ckptl(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckptl = pdl2ckptl(ckpdl)
        pobj(ckptl)
        #dictList2ckptl = pdl2ckptl
    '''
    ckptl = elel.array_map(ckpdl,dict2ckpt)
    return(ckptl)

dictList2ckptl = pdl2ckptl

def ckstr2dict(ckstr):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckdict = ckstr2dict(ckstr)
        pobj(ckdict)
    '''
    ckptl = ckstr2ptl(ckstr)
    ckdict = ckptl2dict(ckptl)
    return(ckdict)

def dict2ckstr(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckstr = dict2ckstr(ckdict)
        ckstr
    '''
    ckptl = dict2ckptl(ckdict)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def ckpl2dict(ckpl):
    '''
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckdict = ckpl2dict(ckpl)
        pobj(ckdict)
    '''
    ckptl = ckpl2ptl(ckpl)
    ckdict = ckptl2dict(ckptl)
    return(ckdict)

def dict2ckpl(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckpl = dict2ckpl(ckdict)
        pobj(ckpl)
    '''
    ckptl = dict2ckptl(ckdict)
    ckpl = ptl2ckpl(ckptl)
    return(ckpl)

def ckptl2dict(ckptl):
    '''
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        d = ckptl2dict(ckptl)
        pobj(d)
    '''
    return(dict(ckptl))

def dict2ckptl(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckptl = dict2ckptl(ckdict)
        pobj(ckptl)
    '''
    return(list(ckdict.items()))

def ckpdl2dict(ckpdl):
    '''
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = ckpdl2dict(ckpdl)
        pobj(ckdict)
    '''
    ckptl = pdl2ckptl(ckpdl)
    return(ckptl2dict(ckptl))
    
def dict2ckpdl(ckdict):
    '''
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckpdl = dict2ckpdl(ckdict)
        pobj(ckpdl)
    '''
    ckptl = dict2ckptl(ckdict)
    ckpdl = ckptl2pdl(ckptl)
    return(ckpdl)

######wait to implement
# [validate_ckstr,validate_ckpl,validate_ckptl,validate_ckpdl,validate_ckdict,detect_ckbody,validate_ckbody]
# ['validate_ckstr', 'validate_ckpl', 'validate_ckptl', 'validate_ckpdl', 'validate_ckdict', 'detect_ckbody', 'validate_ckbody']

def validate_ckstr(ckstr):
    '''
    '''
    ckptl = ckstr2ptl(ckstr)
    return(validate_ckptl(ckptl))

def validate_ckpl(ckpl):
    '''
    '''
    ckptl = ckpl2ptl(ckpl)
    return(validate_ckptl(ckptl))

def validate_ckptl(ckptl):
    '''
    '''
    rslt = elel.every(ckptl,validate_ckpt)
    print(rslt)
    return(rslt[0])

def validate_ckpdl(ckpdl):
    '''
    '''
    ckptl = pdl2ckptl(ckpdl)
    return(validate_ckptl(ckptl))

def validate_ckdict(ckdict):
    '''
    '''
    ckptl = dict2ckptl(ckdict)
    return(validate_ckptl(ckptl))

def detect_ckbody(ckbody):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'ASP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        detect_ckbody(ckstr)
        detect_ckbody(ckpl)
        detect_ckbody(ckptl)
        detect_ckbody(ckpdl)
        detect_ckbody(ckdict)
    '''
    if(type(ckbody) == type('')):
        return('ckstr')
    elif(type(ckbody) == type([])):
        if(type(ckbody[0]) == type('')):
            return('ckpl')
        elif(type(ckbody[0]) == type(())):
            return('ckptl')
        elif(type(ckbody[0]) == type(dict({}))):
            return('ckpdl')
        else:
            return('unknown')
    elif(type(ckbody) == type(dict())):
        return('ckdict')
    else:
        return('unknown')

def validate_ckbody(ckbody):
    '''
    '''
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        return(validate_ckstr(ckbody))
    elif(mode == 'ckpl'):
        return(validate_ckpl(ckbody))
    elif(mode == 'ckptl'):
        return(validate_ckptl(ckbody))
    elif(mode == 'ckpdl'):
        return(validate_ckpdl(ckbody))
    elif(mode == 'ckdict'):
        return(validate_ckdict(ckbody))
    else:
        print("unknow mode")
        return(False)


#[ckbody2ptl,select_ckbody,convert_ckbody,prepend_ckbody,append_ckbody,insert_ckbody,remove_ckbody]

def ckbody2ptl(ckbody,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        ckbody2ptl(ckstr)
        ckbody2ptl(ckpl)
        ckbody2ptl(ckptl)
        ckbody2ptl(ckpdl)
        ckbody2ptl(ckdict)
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        ckptl = ckstr2ptl(ckbody)
    elif(mode == 'ckpl'):
        ckptl = ckpl2ptl(ckbody)
    elif(mode == 'ckptl'):
        ckptl = ckbody
    elif(mode == 'ckpdl'):
        ckptl = pdl2ckptl(ckbody)
    elif(mode == 'ckdict'):
        ckptl = dict2ckptl(ckbody)
    else:
        print("unknow mode")
        return(None)
    return(ckptl)

def convert_ckbody(ckbody,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        convert_ckbody(ckstr)
        ckbody = convert_ckbody(ckpl,mode='ckdict')
        pobj(ckbody)
        convert_ckbody(ckptl,mode='ckpdl')
        convert_ckbody(ckpdl,mode='ckstr')
        ckbody = convert_ckbody(ckdict,mode='ckpl')
        elel.forEach(ckbody,print)
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        ckptl = ckstr2ptl(ckbody)
    elif(mode == 'ckpl'):
        ckptl = ckpl2ptl(ckbody)
    elif(mode == 'ckptl'):
        ckptl = ckbody
    elif(mode == 'ckpdl'):
        ckptl = pdl2ckptl(ckbody)
    elif(mode == 'ckdict'):
        ckptl = dict2ckptl(ckbody)
    else:
        print("unknow mode")
        return(None)
    if('mode' in kwargs):
        to_mode = kwargs['mode']
    else:
        to_mode = 'ckptl'
    if(to_mode == 'ckstr'):
        ckbody = ptl2ckstr(ckptl)
    elif(to_mode == 'ckpl'):
        ckbody = ptl2ckpl(ckptl)
    elif(to_mode == 'ckptl'):
        ckbody = ckptl
    elif(to_mode == 'ckpdl'):
        ckbody = ckptl2pdl(ckptl)
    elif(to_mode == 'ckdict'):
        ckbody = ckptl2dict(ckptl)
    else:
        print("unknow mode")
        return(None)
    return(ckbody)

# 返回ckstr
def select_ckbody(ckbody,*cknames,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        selected = select_ckbody(ckstr,'BIGipServer','TSPD_101')
        selected 
        selected = select_ckbody(ckstr,'TSPD_101','BIGipServer')
        ckdict = ckstr2dict(selected)
        pobj(ckdict)
        #select_ckbody,via ckname, allow duplecate, return ckstr
    '''
    def via_ckname(ele,cknames):
        ckname = ele[0]
        cond = (ckname in cknames)
        return(cond)
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    cknames = list(cknames)
    ckptl = ckbody2ptl(ckbody)
    selected = elel.find_all(ckptl,via_ckname,cknames)
    selected = elel.array_map(selected,lambda ele:ele['value'])
    ckstr = ptl2ckstr(selected)
    return(ckstr)

# 单独的ckpair 可以看作ckstr
# 单独的ckpd   可以看作ckdict
# 所以只需要判断下 单独ckpt 即可
def prepend_ckbody(dst_ckbody,src_ckbody,**kwargs):
    '''
        dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = prepend_ckbody(dst_ckbody,src_ckbody)
        ckstr
        #return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
        #attention ckdict cant keep the order!
        #ckstr include ckpair
        #ckdict include ckpd
    '''
    if(type(src_ckbody) == type(())):
        src_ckbody = [src_ckbody]
    else:
        pass
    src_ckptl = convert_ckbody(src_ckbody)
    dst_ckptl = convert_ckbody(dst_ckbody)
    ckptl = elel.prextend(dst_ckptl,src_ckptl)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def append_ckbody(dst_ckbody,src_ckbody,**kwargs):
    '''
        dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = append_ckbody(dst_ckbody,src_ckbody)
        ckstr
        #return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
        #attention ckdict cant keep the order!
        #ckstr include ckpair
        #ckdict include ckpd
    '''
    if(type(src_ckbody) == type(())):
        src_ckbody = [src_ckbody]
    else:
        pass
    src_ckptl = convert_ckbody(src_ckbody)
    dst_ckptl = convert_ckbody(dst_ckbody)
    ckptl = elel.extend(dst_ckptl,src_ckptl)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def insert_ckbody(dst_ckbody,src_ckbody,location,**kwargs):
    '''
        dst_ckbody = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = insert_ckbody(dst_ckbody,src_ckbody,1)
        ckstr
        # return ckstr, params could be ckdict/ckpl/ckpdl/ckptl/ckstr
    '''
    if(type(src_ckbody) == type(())):
        src_ckbody = [src_ckbody]
    else:
        pass
    src_ckptl = convert_ckbody(src_ckbody)
    dst_ckptl = convert_ckbody(dst_ckbody)
    ckptl = elel.insert_section(dst_ckptl,src_ckptl,location)
    ckstr = ptl2ckstr(ckptl)
    return(ckstr)

def remove_ckbody(ckbody,ckname,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        lefted = remove_ckbody(ckstr,'TS013d8ed5')
        lefted 
        ckdict = ckstr2dict(lefted)
        pobj(ckdict)
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        lefted = remove_ckbody(ckstr,'TS013d8ed5',which=1)
        lefted 
        ckdict = ckstr2dict(lefted)
        pobj(ckdict)
        #remove_ckbody,via ckname, allow duplecate, return ckstr,by default remove_all
    '''
    def via_ckname(ele,ckname):
        cond = (ckname ==  ele[0])
        return(cond)
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    if('which' in kwargs):
        which = kwargs['which']
    else:
        which = None
    ckptl = ckbody2ptl(ckbody)
    if(which == None):
        lefted = elel.cond_remove_all(ckptl,cond_func=via_ckname,cond_func_args=[ckname])
    else:
        lefted = elel.cond_remove_some(ckptl,which,cond_func=via_ckname,cond_func_args=[ckname])
    ckstr = ptl2ckstr(lefted)
    return(ckstr)

def replace_ckbody(ckbody,ckname,ckele,*args,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace=replace')
        replaced 
        replaced = replace_ckbody(ckstr,'TS013d8ed5',('TSreplace','replace'))
        replaced 
        replaced = replace_ckbody(ckstr,'TS013d8ed5',{'TSreplace':'replace'})
        replaced 
        replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace','replace')
        replaced 
        ####
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace=replace',which=0)
        replaced 
        replaced = replace_ckbody(ckstr,'TS013d8ed5',('TSreplace','replace'),which=1)
        replaced 
        replaced = replace_ckbody(ckstr,'TS013d8ed5',{'TSreplace':'replace'},which=0)
        replaced 
        replaced = replace_ckbody(ckstr,'TS013d8ed5','TSreplace','replace',which=1)
        replaced 
        #replace_ckbody,via ckname, allow duplecate, return ckstr,by default replace_all
    '''
    def via_ckname(ele,ckname):
        cond = (ckname ==  ele[0])
        return(cond)
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    if('which' in kwargs):
        which = kwargs['which']
    else:
        which = None
    ckptl = ckbody2ptl(ckbody)
    ckpt  = convert_ckele(ckele,*args)
    selected = elel.find_all(ckptl,via_ckname,ckname)
    selected_indexes = elel.array_map(selected,lambda ele:ele['index'])
    if(which == None):
        replaced = elel.replace_seqs(ckptl,ckpt,selected_indexes)
    else:
        index = selected_indexes[which]
        ckptl[index] = ckpt
        replaced = ckptl
    ckstr = ptl2ckstr(replaced)
    return(ckstr)

def uniqualize_ckbody(ckbody,*cknames,**kwargs):
    '''
        ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        uniqulized = uniqualize_ckbody(ckstr)
        uniqulized
        
        ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
        uniqulized = uniqualize_ckbody(ckstr,reserved = reserved)
        uniqulized 
        
        ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        uniqulized = uniqualize_ckbody(ckstr,'BIGipServer','TS013d8ed5')
        uniqulized 
        
        ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        reserved = {'BIGipServer':1,'TS013d8ed5':0}
        uniqulized = uniqualize_ckbody(ckstr,'BIGipServer','TS013d8ed5',reserved=reserved)
        uniqulized 
        
        ####
        #uniqualize_ckbody,via ckname, allow duplecate, return ckstr,by default uniqulize_all
        #
    '''
    def via_ckname(ele,cknames):
        cond = (ele[0] in cknames)
        if(cond):
            ckname = ele[0]
        else:
            ckname = None
        return(ckname)
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    if('reserved' in kwargs):
        reserved = kwargs['reserved']
    else:
        reserved = None
    cknames = list(cknames)
    ckptl = ckbody2ptl(ckbody)
    if(cknames.__len__()==0):
        cknames = elel.array_map(ckptl,lambda ele:ele[0])
    else:
        pass
    uniqulized = elel.cond_uniqualize(ckptl,cond_func=via_ckname,cond_func_args=[cknames],reserved_mapping=reserved)
    ckstr = ptl2ckstr(uniqulized)
    return(ckstr)

uniqulize_ckbody = uniqualize_ckbody
#Part.3
#命名规则 priority ckheader > ckbody >ckstr > ckpl > ckptl > ckpdl >ckdict
####

def split_ckheader(ckheader,**kwargs):
    '''
        ckheader = "Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax"
        pobj(split_ckheader(ckheader))
        pobj(split_ckheader(ckheader,mode='ckstr'))
        pobj(split_ckheader(ckheader,mode='ckpl'))
        pobj(split_ckheader(ckheader,mode='ckptl'))
        pobj(split_ckheader(ckheader,mode='ckpdl'))
        pobj(split_ckheader(ckheader,mode='ckdict'))
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'ckptl'
    cktype,ckstr = tuple(ckheader.split(SEPARATORS['ckheader']))
    if(mode == 'ckstr'):
        return({'cktype':cktype,'ckstr':ckstr})
    elif(mode == 'ckpl'):
        ckpl = ckstr2pl(ckstr)
        return({'cktype':cktype,'ckpl':ckpl})
    elif(mode == 'ckptl'):
        ckptl = ckstr2ptl(ckstr)
        return({'cktype':cktype,'ckptl':ckptl})
    elif(mode == 'ckpdl'):
        ckpdl = ckstr2pdl(ckstr)
        return({'cktype':cktype,'ckpdl':ckpdl})
    elif(mode == 'ckdict'):
        ckdict = ckstr2dict(ckstr)
        return({'cktype':cktype,'ckdict':ckdict})
    else:
        print("unknow mode")
        return(None)

def validate_ckheader(ckheader):
    '''
    '''
    cktype,ckstr = tuple(ckheader.split(SEPARATORS['ckheader']))
    cond1 = (cktype == TYPES['cktype'])
    if(cond1):
        cond2 = validate_ckstr(ckstr)
        if(cond2):
            return(True)
        else:
            return(False)
    else:
        print("cktype wrong!")
        return(False)

def cons_ckheader(ckbody,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        ckpl = ['BIGipServer=rd19', 'TS013d8ed5=0105b6b0', 'TSPD_101=08819c2a', '__RequestVerificationToken=9VdrIliI', 'SP.NET_SessionId=epax']
        ckptl = [('BIGipServer', 'rd19'), ('TS013d8ed5', '0105b6b0'), ('TSPD_101', '08819c2a'), ('__RequestVerificationToken', '9VdrIliI'), ('ASP.NET_SessionId', 'epax')]
        ckpdl = [{'BIGipServer': 'rd19'}, {'TS013d8ed5': '0105b6b0'}, {'TSPD_101': '08819c2a'}, {'__RequestVerificationToken': '9VdrIliI'}, {'ASP.NET_SessionId': 'epax'}]
        ckdict = {'__RequestVerificationToken': '9VdrIliI', 'ASP.NET_SessionId': 'epax', 'BIGipServer': 'rd19', 'TS013d8ed5': '0105b6b0', 'TSPD_101': '08819c2a'}
        cons_ckheader(ckstr)
        cons_ckheader(ckpl)
        cons_ckheader(ckptl)
        cons_ckheader(ckpdl)
        cons_ckheader(ckdict)
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    mode = detect_ckbody(ckbody)
    if(mode == 'ckstr'):
        ckstr = ckbody
    elif(mode == 'ckpl'):
        ckstr = pl2ckstr(ckbody)
    elif(mode == 'ckptl'):
        ckstr = ptl2ckstr(ckbody)
    elif(mode == 'ckpdl'):
        ckstr = pdl2ckstr(ckbody)
    elif(mode == 'ckdict'):
        ckstr = dict2ckstr(ckbody)
    else:
        print("unknow mode")
        return(None)
    ckheader = TYPES['cktype']+SEPARATORS['ckheader']+ckstr
    return(ckheader)

def select_ckheader(ckheader,*cknames,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        selected = select_ckheader(ckheader,'BIGipServer','TSPD_101')
        selected 
        selected = select_ckheader(ckheader,'TSPD_101','BIGipServer')
        selected
    '''
    if('validate' in kwargs):
        valid = validate_ckbody(ckbody)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    tmp = split_ckheader(ckheader)
    ckbody = tmp['ckptl']
    cktype = tmp['cktype']
    ckbody = select_ckbody(ckbody,*cknames,**kwargs)
    ckheader = cons_ckheader(ckbody,**kwargs)
    return(ckheader)

def is_ckheader(ckheader,**kwargs):
    '''
        roughly check
        the detail check : validate = True 
    '''
    if('validate' in kwargs):
        valid = validate_ckheader(ckheader)
    else:
        valid = True
    if(valid):
        pass
    else:
        print('invalid ckbody')
        return(None)
    if(type(ckheader) == type('')):
        length = TYPES['cktype'].__len__()
        cond = (ckheader[0:length] == TYPES['cktype'])
        return(cond)
    else:
        return(False)

def prepend_ckheader(ckheader,src,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        prepended = prepend_ckheader(ckheader,src)
        prepended
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        prepended = prepend_ckheader(ckheader,src)
        prepended 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
        prepended = prepend_ckheader(ckheader,src)
        prepended 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        prepended = prepend_ckheader(ckheader,src)
        prepended 
    
    '''
    #if src is not ckheader , treated as ckbody
    cond = is_ckheader(src)
    if(cond):
        src_ckheader = src 
        src_ckbody = split_ckheader(src_ckheader)['ckptl']
    else:
        src_ckbody = src 
    dst_ckbody = split_ckheader(ckheader)['ckptl']
    ckbody = prepend_ckbody(dst_ckbody,src_ckbody)
    ckheader = cons_ckheader(ckbody)
    return(ckheader)

def append_ckheader(ckheader,src,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        appended = append_ckheader(ckheader,src)
        appended
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        appended = append_ckheader(ckheader,src)
        appended 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
        appended = append_ckheader(ckheader,src)
        appended 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        appended = append_ckheader(ckheader,src)
        appended
    '''
    #if src is not ckheader , treated as ckbody
    cond = is_ckheader(src)
    if(cond):
        src_ckheader = src 
        src_ckbody = split_ckheader(src_ckheader)['ckptl']
    else:
        src_ckbody = src 
    dst_ckbody = split_ckheader(ckheader)['ckptl']
    ckbody = append_ckbody(dst_ckbody,src_ckbody)
    ckheader = cons_ckheader(ckbody)
    return(ckheader)

def insert_ckheader(ckheader,src,location,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        inserted = insert_ckheader(ckheader,src,0)
        inserted
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        inserted = insert_ckheader(ckheader,src,1)
        inserted 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = [('__RequestVerificationToken','9VdrIliI'),('ASP.NET_SessionId','epax')]
        inserted = insert_ckheader(ckheader,src,2)
        inserted 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        inserted = insert_ckheader(ckheader,src,3)
        inserted
    '''
    #if src is not ckheader , treated as ckbody
    cond = is_ckheader(src)
    if(cond):
        src_ckheader = src 
        src_ckbody = split_ckheader(src_ckheader)['ckptl']
    else:
        src_ckbody = src 
    dst_ckbody = split_ckheader(ckheader)['ckptl']
    ckbody = insert_ckbody(dst_ckbody,src_ckbody,location)
    ckheader = cons_ckheader(ckbody)
    return(ckheader)

def remove_ckheader(ckheader,ckname,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        removed = remove_ckheader(ckheader,'TS013d8ed5')
        removed 

        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        removed = remove_ckheader(ckheader,'TS013d8ed5',which=1)
        removed 

        #remove_ckheader,via ckname, allow duplecate, return ckheader,by default remove_all
    '''
    if('which' in kwargs):
        which = kwargs['which']
    else:
        which = None
    dst_ckbody = split_ckheader(ckheader)['ckptl']
    ckbody = remove_ckbody(dst_ckbody,ckname,which=which)
    ckheader = cons_ckheader(ckbody)
    return(ckheader)

def replace_ckheader(ckheader,ckname,ckele,*args,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace=replace')
        replaced 
        replaced = replace_ckheader(ckheader,'TS013d8ed5',('TSreplace','replace'))
        replaced 
        replaced = replace_ckheader(ckheader,'TS013d8ed5',{'TSreplace':'replace'})
        replaced 
        replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace','replace')
        replaced 
        ####
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace=replace',which=0)
        replaced 
        replaced = replace_ckheader(ckheader,'TS013d8ed5',('TSreplace','replace'),which=1)
        replaced 
        replaced = replace_ckheader(ckheader,'TS013d8ed5',{'TSreplace':'replace'},which=0)
        replaced 
        replaced = replace_ckheader(ckheader,'TS013d8ed5','TSreplace','replace',which=1)
        replaced 
        #replace_ckheader,via ckname, allow duplecate, return ckheader,by default replace_all
    '''
    if('which' in kwargs):
        which = kwargs['which']
    else:
        which = None
    dst_ckbody = split_ckheader(ckheader)['ckptl']
    ckbody = replace_ckbody(dst_ckbody,ckname,ckele,*args,**kwargs)
    ckheader = cons_ckheader(ckbody)
    return(ckheader)

def uniqualize_ckheader(ckheader,*cknames,**kwargs):
    '''
        ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        uniqulized = uniqualize_ckheader(ckheader)
        uniqulized
        
        ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        reserved = {'BIGipServer':1,'TS013d8ed5':0,'SID':1}
        uniqulized = uniqualize_ckheader(ckheader,reserved = reserved)
        uniqulized 
        
        ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5')
        uniqulized 
        
        ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        reserved = {'BIGipServer':1,'TS013d8ed5':0}
        uniqulized = uniqualize_ckheader(ckheader,'BIGipServer','TS013d8ed5',reserved=reserved)
        uniqulized 
        
        ####
        #uniqualize_ckheader,via ckname, allow duplecate, return ckheader,by default uniqulize_all
        #
    '''
    if('reserved' in kwargs):
        reserved = kwargs['reserved']
    else:
        reserved = None
    dst_ckbody = split_ckheader(ckheader)['ckptl']
    ckbody = uniqualize_ckbody(dst_ckbody,*cknames,**kwargs)
    ckheader = cons_ckheader(ckbody)
    return(ckheader)


def quote_ckheader(ckheader,**kwargs):
    if('plus' in kwargs):
        plus = kwargs['plus']
    else:
        plus = True
    if('plus'):
        ckheader = urllib.parse.quote_plus(ckheader)
    else:
        ckheader = urllib.parse.quote(ckheader)
    return(ckheader)    


#wrapped API: apply to either ckbody or ckheader
def select(horb,*cknames,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        selected = select(ckstr,'BIGipServer','TSPD_101')
        selected 
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        selected = select(ckheader,'BIGipServer','TSPD_101')
        selected 
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(select_ckheader(horb,*cknames,**kwargs))
    else:
        return(select_ckbody(horb,*cknames,**kwargs))

def prepend(horb,src,**kwargs):
    '''
        dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = prepend(dst_ckbody,src_ckbody)
        ckstr
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        prepended = prepend(ckheader,src)
        prepended
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(prepend_ckheader(horb,src,**kwargs))
    else:
        return(prepend_ckbody(horb,src,**kwargs))

def append(horb,src,**kwargs):
    '''
        dst_ckbody = {'__RequestVerificationToken':'9VdrIliI','ASP.NET_SessionId':'epax'}
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = append(dst_ckbody,src_ckbody)
        ckstr
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        appended = append(ckheader,src)
        appended
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(append_ckheader(horb,src,**kwargs))
    else:
        return(append_ckbody(horb,src,**kwargs))

def insert(horb,src,location,**kwargs):
    '''
        dst_ckbody = '__RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        src_ckbody = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a'
        ckstr = insert(dst_ckbody,src_ckbody,1)
        ckstr
        
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0'
        src = 'Cookie: __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        inserted = insert(ckheader,src,0)
        inserted
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(insert_ckheader(horb,src,location,**kwargs))
    else:
        return(insert_ckbody(horb,src,location,**kwargs))

def remove(horb,ckname,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        lefted = remove(ckstr,'TS013d8ed5')
        lefted 
        #####
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        removed = remove(ckheader,'TS013d8ed5')
        removed 
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(remove_ckheader(horb,ckname,**kwargs))
    else:
        return(remove_ckbody(horb,ckname,**kwargs))

def replace(horb,ckname,ckele,*args,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace(ckstr,'TS013d8ed5','TSreplace=replace')
        replaced 
        ####
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace(ckheader,'TS013d8ed5','TSreplace=replace')
        replaced 
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(replace_ckheader(horb,ckname,ckele,*args,**kwargs))
    else:
        return(replace_ckbody(horb,ckname,ckele,*args,**kwargs))

def replace_same(horb,ckele,*args,**kwargs):
    '''
        ckstr = 'BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace_same(ckstr,'TS013d8ed5=replace')
        replaced
        ####
        ckheader = 'Cookie: BIGipServer=rd19; TS013d8ed5=0105b6b0; TSPD_101=08819c2a; TS013d8ed5=0105b6b0; __RequestVerificationToken=9VdrIliI; ASP.NET_SessionId=epax'
        replaced = replace_same(ckheader,'TS013d8ed5=replace')
        replaced
        
    '''
    ckname,ckvalue = ckele2pt(ckele)
    return(replace(horb,ckname,ckele,*args,**kwargs))



def uniqualize(horb,*cknames,**kwargs):
    '''
        ckstr = 'BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        uniqulized = uniqualize(ckstr)
        uniqulized
        ####
        ckheader = 'Cookie: BIGipServer=rd0; TS013d8ed5=T0; BIGipServer=rd1; TS013d8ed5=T1; SID=0; SID=1'
        uniqulized = uniqualize_ckheader(ckheader)
        uniqulized
    '''
    cond = is_ckheader(horb)
    if(cond):
        return(uniqualize_ckheader(horb,*cknames,**kwargs))
    else:
        return(uniqualize_ckbody(horb,*cknames,**kwargs))

#####

def includes(horb,ckname,**kwargs):
    cond = is_ckheader(horb)
    if(cond):
        ckstr = split_ckheader(horb,mode="ckstr")['ckstr'] 
    else:
        ckstr = horb
    return(ckname in ckstr2dict(ckstr))


def get(horb,ckname,**kwargs):
    cond = is_ckheader(horb)
    if(cond):
        ckstr = split_ckheader(horb,mode="ckstr")['ckstr']
    else:
        ckstr = horb
    ckptl = ckstr2ptl(ckstr)
    l = tltl.get_value(ckptl,ckname)
    if(l.__len__() == 1):
        return(l[0])
    else:
        return(l)





#####this function need from xdict.jprint import pobj
def show(horb):
    '''
        horb = "Cookie: TS=ts001; Data=History=001; Auth=ABCD001; rToken=EohV; BIGipServer=rd001; ASP.NET_SessionId=sesn001; TSPD=tspd001"
        show(horb)
    '''
    try:
        from xdict.jprint import pobj
    except:
        pobj = print
    else:
        pass
    cond = is_ckheader(horb)
    if(cond):
        ckdict = split_ckheader(horb,mode='ckdict')
    else:
        #treated as ckbody
        ckdict = convert_ckbody(horb,mode='ckdict')
    pobj(ckdict)

#####

#Part.4 Set-Cookie
# 客户端 只要实现 split_setckheader 即可
# 因为每个set-cookie-header 只能包含一条cookie-pair,所以只要支持python返回的一种数据格式setcktuple即可
#setckheader       set-cookie-header     "Set-Cookie: __Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict"
#setcktuple        set-cookie-tuple     ('Set-Cookie', 'TSPD_101_R0=e7b7; Max-Age=5; Path=/secure/abc.htm')
#setck             setckheader | setcktuple

#setcktype         set-cookie-type       "Set-Cookie"
#一个response 中可能包含多条 set-cookie-header
#setcktl           set-cookie-tupleList   [('Set-Cookie', 'BIGipServe=rd0; path=/'), ('Set-Cookie', 'TS=0105; Path=/; Secure; HTTPOnly')]

#命名规则  setckheader > setcktuple 

def setckheader2tuple(setckheader,**kwargs):
    '''
        setckheader = "Set-Cookie: __Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict"
        setcktuple = setckheader2tuple(setckheader)
        pobj(setcktuple)
        #for python urllib compatible
    '''
    setcktuple = tuple(setckheader.split(SEPARATORS['setckheader']))
    return(setcktuple)

def tuple2setckheader(setcktuple,**kwargs):
    '''
        setcktuple = ('Set-Cookie', '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict')
        setckheader = tuple2setckheader(setcktuple)
        setckheader
    '''
    setcktype,setckstr = setcktuple
    setckheader = setcktype + SEPARATORS['setckheader']+ setckstr
    return(setckheader)

def tl2setckheaders(setcktl,**kwargs):
    '''
        setcktl = [('Set-Cookie', 'BIGipServe=rd0; path=/'), ('Set-Cookie', 'TS=0105; Path=/; Secure; HTTPOnly')]
        setckhs = tl2setckheaders(setcktl)
        pobj(setckhs)
    '''
    setckhs = elel.array_map(setcktl,tuple2setckheader)
    return(setckhs)

def setckheaders2tl(setckheaders,**kwargs):
    '''
        setckhs = ['Set-Cookie: BIGipServe=rd0; path=/','Set-Cookie: TS=0105; Path=/; Secure; HTTPOnly']
        setcktl = setckheaders2tl(setckheaders)
        pobj(setcktl)
    '''
    setcktl = elel.array_map(setckheaders,setckheader2tuple)
    return(setcktl)


#一些invalid 的set-cookie-str 可能会包含多个cookie-pair ,多个同名的cookie-av, 这个放在validate format里面做
#目前假定所有server发送的都是正确的格式

#单个setckbody
#setckstr          set-cookie-string      "__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict"              #cookie-pair *( ";" SP cookie-av ) 
#setckdict         set-cookie-dict      {'SameSite=Strict': True, 'Path': '/', 'value': 'Tz98', 'HttpOnly': True, 'Secure': True, 'name': '__Host-user_session', 'Expires': 'Tue, 27 Mar 2018 05:30:16 -0000'}
#setckbody         setckstr | setckdict  

#若干setckbody组成的list,因为response可能返回多个setckbody 
#setcksl           set-cookie_stringList  
#setckdl           set-cookie-dictList    

#命名规则  setckbody > setckdict > setckstr 

def str2setckdict(setckstr,**kwargs):
    '''
        setckstr = "__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict"
        setckdict = str2setckdict(setckstr)
        pobj(setckdict)
        #attribute-name case-insensitively 
    '''
    l = setckstr.split(SEPARATORS['setckstr'])
    setckdict = {}
    ckname,ckvalue = ckpair2nv(l[0])
    setckdict['name'] = ckname
    setckdict['value'] = ckvalue
    l.pop(0)
    for ckav in l:
        attr,value = ckav2tuple(ckav)
        attr = uniform_ckavattr(attr)
        if(attr):
            setckdict[attr] = value
        else:
            setckdict[ckav] = True 
    return(setckdict)

def setckdict2str(setckdict,**kwargs):
    '''
        setckdict = {
             'HttpOnly': True,
             'SameSite=Strict': True,
             'value': 'Tz98',
             'Expires': 'Tue, 27 Mar 2018 05:30:16 -0000',
             'Secure': True,
             'name': '__Host-user_session',
             'Path': '/'
        }
        setckstr = setckdict2str(setckdict)
        setckstr
    '''
    setckdict = copy.deepcopy(setckdict)
    setckstr = nv2ckpair(setckdict['name'],setckdict['value'])
    setckdict.pop('name')
    setckdict.pop('value')
    for i in range(0,CKAVNAMES.__len__()):
        attr = CKAVNAMES[i]
        if(attr in setckdict):
            value = setckdict[attr]
            if(value == True):
                setckstr = setckstr + SEPARATORS['setckstr'] + attr
            else:
                ckpair = nv2ckpair(attr,value)
                setckstr = setckstr + SEPARATORS['setckstr'] + ckpair
            setckdict.pop(attr)
        else:
            pass
    for extav in setckdict:
        setckstr = setckstr + SEPARATORS['setckstr'] + extav
    return(setckstr)

def sl2setckdl(setcksl):
    '''
        setcksl = ['BIGipServe=rd0; path=/', 'TS=0105; Path=/; Secure; HTTPOnly']
        setckdl = sl2setckdl(setcksl)
        pobj(setckdl)
    '''
    setckdl = elel.array_map(setcksl,str2setckdict)
    return(setckdl)

def setckdl2sl(setckdl):
    '''
        setckdl = [{'Path': '/', 'value': 'rd0', 'name': 'BIGipServe'}, {'Secure': True, 'Path': '/', 'value': '0105', 'HttpOnly': True, 'name': 'TS'}]
        setcksl = setckdl2sl(setckdl)
        pobj(setcksl)
    '''
    setcksl = elel.array_map(setckdl,setckdict2str)
    return(setcksl)

#命名规则  setckheaders > setcktl > setckdl > setcksl 

def setckheader2str(setckheader):
    '''
        setckheader = 'Set-Cookie: BIGipServe=rd0; path=/'
        setckstr = setckheader2str(setckheader)
        setckstr
    '''
    return(setckheader.split(SEPARATORS['setckheader'])[1])

def setckheaders2sl(setckheaders):
    '''
        setckhs = ['Set-Cookie: BIGipServe=rd0; path=/','Set-Cookie: TS=0105; Path=/; Secure; HTTPOnly']
        setcksl = setckheaders2sl(setckhs)
        pobj(setcksl)
    '''
    setcksl = elel.array_map(setckheaders,setckheader2str)
    return(setcksl)

def str2setckheader(setckstr):
    '''
        setckstr = 'BIGipServe=rd0; path=/'
        setckheader = str2setckheader(setckstr)
        setckheader
    '''
    return(TYPES['setcktype'] + SEPARATORS['setckheader']+setckstr)

def sl2setckheaders(setcksl):
    '''
        setcksl = ['BIGipServe=rd0; path=/', 'TS=0105; Path=/; Secure; HTTPOnly']
        setckhs = sl2setckheaders(setcksl)
        pobj(setckhs)
    '''
    setckheaders = elel.array_map(setcksl,str2setckheader)
    return(setckheaders)

def setckheader2dict(setckheader):
    '''
        setckheader = 'Set-Cookie: BIGipServe=rd0; path=/'
        setckdict = setckheader2dict(setckheader)
        pobj(setckdict)
    '''
    setckstr = setckheader2str(setckheader)
    setckdict = str2setckdict(setckstr)
    return(setckdict)

def setckheaders2dl(setckheaders):
    '''
        setckhs = ['Set-Cookie: BIGipServe=rd0; path=/','Set-Cookie: TS=0105; Path=/; Secure; HTTPOnly']
        setckdl = setckheaders2dl(setckhs)
        pobj(setckdl)
    '''
    setckdl = elel.array_map(setckheaders,setckheader2dict)
    return(setckdl)

def dict2setckheader(setckdict):
    '''
        setckdict = {'Path': '/', 'value': 'rd0', 'name': 'BIGipServe'}
        setckheader = dict2setckheader(setckdict)
        setckheader
    '''
    setckstr = setckdict2str(setckdict)
    setckheader = str2setckheader(setckstr)
    return(setckheader)

def dl2setckheaders(setckdl):
    '''
        setckdl = [{'Path': '/', 'value': 'rd0', 'name': 'BIGipServe'}, {'Secure': True, 'Path': '/', 'value': '0105', 'HttpOnly': True, 'name': 'TS'}]
        setckhs = dl2setckheaders(setckdl)
        pobj(setckhs)
    '''
    setckhs = elel.array_map(setckdl,dict2setckheader)
    return(setckhs)

def setcktuple2str(setcktuple):
    '''
        setcktuple = ('Set-Cookie', '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict')
        setckstr = setcktuple2str(setcktuple)
        setckstr
    '''
    return(setcktuple[1])

def setcktl2sl(setcktl):
    '''
        setcktl = [('Set-Cookie', 'BIGipServe=rd0; path=/'), ('Set-Cookie', 'TS=0105; Path=/; Secure; HTTPOnly')]
        setcksl = setcktl2sl(setcktl)
        pobj(setcksl)
    '''
    setcksl = elel.array_map(setcktl,setcktuple2str)
    return(setcksl)


def str2setcktuple(setckstr):
    '''
        setckstr = '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict'
        setcktuple = str2setcktuple(setckstr)
        pobj(setcktuple)
    '''
    setcktuple = (TYPES['setcktype'],setckstr)
    return(setcktuple)

def sl2setcktl(setcksl):
    '''
        setcksl = ['BIGipServe=rd0; path=/', 'TS=0105; Path=/; Secure; HTTPOnly']
        setcktl = sl2setcktl(setcksl)
        pobj(setcktl)
    '''
    setcktl = elel.array_map(setcksl,str2setcktuple)
    return(setcktl)

def setcktuple2dict(setcktuple):
    '''
        setcktuple = ('Set-Cookie', '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict')
        setckdict = setcktuple2dict(setcktuple)
        pobj(setckdict)
    '''
    setckstr = setcktuple2str(setcktuple)
    setckdict = str2setckdict(setckstr)
    return(setckdict)

def setcktl2dl(setcktl):
    '''
        setcktl = [('Set-Cookie', 'BIGipServe=rd0; path=/'), ('Set-Cookie', 'TS=0105; Path=/; Secure; HTTPOnly')]
        setckdl = setcktl2dl(setcktl)
        pobj(setckdl)
    '''
    setckdl = elel.array_map(setcktl,setcktuple2dict)
    return(setckdl)

def dict2setcktuple(setckdict):
    '''
        setckdict = {'HttpOnly': True, 'SameSite=Strict': True, 'value': 'Tz98', 'Expires': 'Tue, 27 Mar 2018 05:30:16 -0000', 'Secure': True, 'name': '__Host-user_session', 'Path': '/'}
        setcktuple = dict2setcktuple(setckdict)
        pobj(setcktuple)
    '''
    setckstr = setckdict2str(setckdict)
    setcktuple = str2setcktuple(setckstr)
    return(setcktuple)

def dl2setcktl(setckdl):
    '''
        setckdl = [{'Path': '/', 'value': 'rd0', 'name': 'BIGipServe'}, {'Secure': True, 'Path': '/', 'value': '0105', 'HttpOnly': True, 'name': 'TS'}]
        setcktl = dl2setcktl(setckdl)
        pobj(setcktl)
    '''
    setcktl = elel.array_map(setckdl,dict2setcktuple)
    return(setcktl)


def detect_setck(setck,**kwargs):
    '''
    '''
    if(type(setck) == type('')):
        return('setckheader')
    elif(type(setck) == type(())):
        return('setcktuple')
    else:
        print('currently only support two format: setck = setckheader|setcktuple')
        return(None)

def split_setck(setck,**kwargs):
    '''
        setck = ('Set-Cookie', '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict')
        setckdict = drone.split_setck(setck)
        pobj(setckdict)
        ####
        setck = 'Set-Cookie: BIGipServe=rd0; path=/'
        setckdict = drone.split_setck(setck)
        pobj(setckdict)
    '''
    from_mode = detect_setck(setck)
    if(from_mode == 'setckheader'):
        setckheader = setck
    elif(from_mode == 'setcktuple'):
        setckheader = tuple2setckheader(setck)
    else:
        print("Unknown...")
        return(None)
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'setckdict'
    return(split_setckheader(setckheader,mode=mode))    


def unquote_setck(setck,**kwargs):
    '''
    '''
    if('plus' in kwargs):
        plus = kwargs['plus']
    else:
        plus = True
    setckstr = split_setck(setck,mode='setckstr')['setckstr']
    if('plus'):
        setckstr = urllib.parse.unquote_plus(setckstr)
    else:
        setckstr = urllib.parse.unquote(setckstr)
    return(TYPES['setcktype']+ SEPARATORS['setckheader'] + setckstr)



def split_setckheader(setckheader,**kwargs):
    '''
        setckheader = "Set-Cookie: __Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict"
        pobj(split_setckheader(setckheader))
        
        pobj(split_setckheader(setckheader,mode='setckstr'))
    '''
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'setckdict'
    setcktype,setckstr = tuple(setckheader.split(SEPARATORS['setckheader']))
    if(mode == 'setckstr'):
        return({'setcktype':setcktype,'setckstr':setckstr})
    elif(mode == 'setckdict'):
        setckdict = str2setckdict(setckstr)
        return({'cktype':setcktype,'setckdict':setckdict})
    else:
        print("unknow mode")
        return(None)



def detect_setckbody(setckbody,**kwargs):
    '''
        setckbody = '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict'
        detect_setckbody(setckbody)
        
        setckbody = {
                       'value': 'Tz98',
                       'Expires': 'Tue, 27 Mar 2018 05:30:16 -0000',
                       'name': '__Host-user_session',
                       'Secure': True,
                       'Path': '/',
                       'HttpOnly': True,
                       'SameSite=Strict': True
                      }
        detect_setckbody(setckbody)
    '''
    if(type(setckbody) == type('')):
        return('setckstr')
    elif(type(setckbody) == type(dict({}))):
        return('setckdict')
    else:
        print('unknown')
        return(None)


def validate_setckstr(setckstr,**kwargs):
    '''
        setckstr = "__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict"
        
    '''
    setckdict = str2setckdict(setckstr)
    cond = True
    for key in setckdict:
        value = get_ckavalue(setckdict,key)
        if(key in VALIDATEFUNCS):
            cond = VALIDATEFUNCS[key](value)
        else:
            cond = VALIDATEFUNCS['extension-av'](value)
        if(cond):
            pass
        else:
            return(False)
    return(cond)

def validate_setckheader(setckheader,**kwargs):
    '''
    '''
    rslt = split_setckheader(setckheader,mode = 'setckstr')
    setcktype = rslt['setcktype']
    setckstr  = rslt['setckstr']
    cond1 = (rslt['setcktype'] == TYPES['setcktype'])
    cond2 = validate_setckstr(setckstr)
    cond = (cond1 & cond2)
    return(cond)
    
##
def classify_setckdl(setckdl,**kwargs):
    '''
        setckdl = [{'value': 'rd1', 'Path': '/', 'name': 'BIGipServer'}, {'value': '0105', 'HttpOnly': True, 'Path': '/', 'name': 'TS', 'Secure': True}]
        pobj(setckdl)
        classified = classify_setckdl(setckdl,via='secure')
        pobj(classified['yes'])
        pobj(classified['no'])
    '''
    via = str.lower(kwargs['via'])
    def cond_func(ele,via):
        via = uniform_ckavattr(via)
        cond1 = (via in ele)
        if(cond1):
            cond = (ele[via] == True)
        else:
            cond = False
        return(cond)
    rslt = {}
    rslt['yes'] = []
    rslt['no'] = []
    length = setckdl.__len__()
    for i in range(0,length):
        ele = setckdl[i]
        cond = cond_func(ele,via)
        if(cond):
            rslt['yes'].append(ele)
        else:
            rslt['no'].append(ele)
    return(rslt)


def classify_setcktl(setcktl,**kwargs):
    '''
        setcktl = [('Set-Cookie', 'BIGipServer=rd1; path=/'), ('Set-Cookie', 'TS=0105; Path=/; Secure; HTTPOnly')]
        #pobj(setcktl)
        classified = classify_setcktl(setcktl,via='secure')
        pobj(classified['yes'])
        pobj(classified['no'])
    '''
    via = str.lower(kwargs['via'])
    setckdl = setcktl2dl(setcktl)
    rslt = classify_setckdl(setckdl,via=via)
    rslt['yes'] = dl2setcktl(rslt['yes'])
    rslt['no'] = dl2setcktl(rslt['no'])
    return(rslt)


def setcktl2ckstr(setcktl):
    '''
        this function only do string-level work ,
        will not do domain/path/expiry/secure/httponly/ management
        for real /domain/path/expiry/secure/httponly/ management,
        refer to jar.py->class Jar->.setcktl2ckstr
        
        setcktl = [('Set-Cookie', 'BIGipServer=rd1; path=/'), ('Set-Cookie', 'TS=002; Path=/')]
        setcktl2ckstr(setcktl)
    '''
    def cond_func(ele):
        ckpair = nv2ckpair(ele['name'],ele['value'])
        return(ckpair)
    setckdl = setcktl2dl(setcktl)
    ckpl = elel.array_map(setckdl,cond_func)
    ckstr = pl2ckstr(ckpl)
    return(ckstr)


def setcktl2ckpl(setcktl):
    '''
        this function only do string-level work ,
        will not do domain/path/expiry/secure/httponly/ management
        for real /domain/path/expiry/secure/httponly/ management,
        refer to jar.py->class Jar->.setcktl2ckstr

        setcktl = [('Set-Cookie', 'ASP.NET_SessionId=zz; path=/; HttpOnly'), ('Set-Cookie', 'TS=0105; Path=/; Secure; HTTPOnly')]
        ckpl = setcktl2ckpl(setcktl) 
        pobj(ckpl)
    '''
    ckstr = setcktl2ckstr(setcktl)
    ckpl = ckstr2pl(ckstr)
    return(ckpl)



#ckavattr            ['expires','max-age','domain','path','secure','httponly']
#expav             expires-av 
#expval            expires-value sane-cookie-date 
#mageav            max-age-av 
#mageval           max-age-value 
#domav             domain-av 
#domval            domain-value 
#pathav            path-av 
#pathval           path-value
#secuav            secure-av 
#honlyav           httponly-av 
#extav             extension-av  #<any CHAR except CTLs or ";">
#ckav              expav | mageav |domav | pathav | secuav | honlyav | extav          #cookie-av ##attribute-name case-insensitively 


def uniform_ckavattr(ckavattr,**kwargs):
    '''
        uniform_ckavattr('expires')
        uniform_ckavattr('max-Age')
        pobj(CKAVNAMES)
        
        uniform_ckavattr('nAme',names=CKAVNAMES+['name','value','extension-av'])
        
    '''
    if('names' in kwargs):
        names = kwargs['names']
    else:
        names = CKAVNAMES
    lowernames = elel.array_map(names,str.lower)
    ckavattr = ckavattr.lower()
    cond = (ckavattr in lowernames)
    if(cond):
        index = lowernames.index(ckavattr)
        return(names[index])
    else:
        return(None)

def ckav2tuple(ckav,**kwargs):
    '''
        ckav = 'expires=Tue, 27 Mar 2018 05:30:16 -0000'
        ckav2tuple(ckav)
        
        ckav = 'HttpOnly'
        ckav2tuple(ckav)
        
        #note :extension-av will be splited 
    '''
    regex = re.compile("(.*?)=(.*)")
    m = regex.search(ckav)
    if(m):
        k = m.group(1)
        v = m.group(2)
    else:
        k = ckav
        v = True
    return((k,v))

def get_ckavalue(setckbody,ckavattr,**kwargs):
    '''
        setckbody = '__Host-user_session=Tz98; path=/; expires=Tue, 27 Mar 2018 05:30:16 -0000; secure; HttpOnly; SameSite=Strict'
        
        get_ckavalue(setckbody,'Expires')
        
        get_ckavalue(setckbody,'name')
        
        get_ckavalue(setckbody,'value')
        
        get_ckavalue(setckbody,'PATH')
        
        get_ckavalue(setckbody,'httponly')
        
        get_ckavalue(setckbody,'extension-av')
    '''
    attr = uniform_ckavattr(ckavattr,names=CKAVNAMES+['name','value','extension-av'])
    mode = detect_setckbody(setckbody)
    if(mode=='setckstr'):
        setckdict = str2setckdict(setckbody)
    elif(mode == 'setckdict'):
        setckdict = setckbody
    else:
        print('unknown')
        return(None)
    if(attr in setckdict):
        value = setckdict[attr]
        if(value == True):
            return(attr)
        else:
            return(value)
    elif(attr == 'extension-av'):
        rslt = []
        for attr in setckdict:
            if(attr in CKAVNAMES+['name','value']):
                pass
            else:
                rslt.append(attr)
        return(rslt)
    else:
        print("not exist")
        return(None)

def detect_ckav(ckav,**kwargs):
    '''
        ckav = "path=/"
        detect_ckav(ckav)
        ckav = "expires=Tue, 27 Mar 2018 05:30:16 -0000"
        detect_ckav(ckav)
        ckav = "HttpOnly"
        detect_ckav(ckav)
        ckav = "SameSite=Strict"
        detect_ckav(ckav)
    '''
    t = ckav2tuple(ckav)
    key = t[0]
    key = uniform_ckavattr(key)
    if(key):
        return(key)
    else:
        return('extension-av')
    
def validate_ckav(ckav,**kwargs):
    '''
    '''
    cond = rfc6265.is_cookie_av(ckav)
    return(cond)
    
    
# @@@@@@@@@@@@@@@@@@
# select without jar filter handling
def setcksl2ckstr(setcksl):
    setcktl = sl2setcktl(setcksl)
    ckstr = setcktl2ckstr(setcktl)
    return(ckstr)



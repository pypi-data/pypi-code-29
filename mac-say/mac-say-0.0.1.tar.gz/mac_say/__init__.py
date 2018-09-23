#!/usr/bin/env python
# -*- coding: utf-8 -*-
from public import public
import runcmd
import values

@public
def say(args, background=False):
    r = runcmd.run(["say"] + values.get(args), background=background)
    if not background:
        r._raise()


def _voice_info(string):
    values = list(filter(None,string.split(" ")))
    name = values[0]
    lang = values[1]
    description = " ".join(values[3:])
    return name,lang,description

def _voices(lang=None):
    cmd = ["/usr/bin/say","-v","?"]
    out = runcmd.run(cmd).out
    for l in out.splitlines():
        _name,_lang,_description = _voice_info(l)
        if not lang or (lang and lang in _lang):
            yield _name,_lang,_description

@public
def voices(lang=None):
    return list(_voices(lang))


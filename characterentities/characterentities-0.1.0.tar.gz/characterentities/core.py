'''
'''

import re
import sys

if sys.version_info[0] == 2:
    from htmlentitydefs import codepoint2name, name2codepoint
elif sys.version_info[0] == 3:
    from html.entities import codepoint2name, name2codepoint
    unichr = chr


class CharacterEntities(object):
    def decode(data):
        '''convert HTML encoded characters to ordinary characters
        :param str data: data to be decoded
        :rtype: str
        '''
        def fixup(m):
            text = m.group(0)
            if text[:2] == "&#":
                try:
                    if text[:3] == "&#x":
                        return unichr(int(text[3:-1], 16))
                    else:
                        return unichr(int(text[2:-1]))
                except ValueError:
                    pass
            else:
                try:
                    text = unichr(name2codepoint[text[1:-1]])
                except KeyError:
                    pass
            return text
        return re.sub(r"&#?\w+;", fixup, data)


    def encode(data, specialchars=True):
        '''
        :param str data: data to be encoded
        :param bool specialchars: whenether to encode SGML special characters
        :rtype str:
        '''
        regexp = r'[^\x00-\x7F]'
        if specialchars:
            regexp += r'|[<>"&]'
        def fixup(m):
            o = ord(m.group(0))
            try:
                return '&{};'.format(codepoint2name[o])
            except KeyError:
                return '&#x{:x};'.format(o)
        return re.sub(regexp, fixup, data)

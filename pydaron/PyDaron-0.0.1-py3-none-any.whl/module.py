from __future__ import division
import string

alphabet = list(string.printable)
alphabet.remove('\n')
alphabet.append('Д')
alphabet.append('Й')
alphabet.append("é")
alphabet.append("è")
alphabet.append("à")
alphabet.append("@")
alphabet.append("û")
alphabet.append('ê')
alphabet.append("ï")
alphabet.append("ç")
alphabet.remove('\r')
alphabet.append('🤑')
alphabet.append('🤢')
alphabet.append('🤔')
alphabet.append('🐠')
alphabet.append('🐟')
alphabet.append('🐡')
alphabet.append('🦈')
alphabet.append('🐋')
def multiply(string,cle):

    len_string  = len(string)
    len_cle = len(cle)

    divi = float()
    divi = len_string/len_cle

    divi_up = None
    if int(divi) != divi:
        divi_up = int(divi)
        divi_up += 1

    if divi_up:
        cle *= divi_up
        cle = cle[0:len_string]

    else:
        cle *= int(divi)

    return cle

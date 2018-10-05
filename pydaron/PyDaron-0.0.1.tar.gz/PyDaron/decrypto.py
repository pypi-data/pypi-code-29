# -*- coding: utf-8 -*-

from __future__ import division
def decrypt(string,key):

    import PyDaron.module as module
    import time


    cle = key
    cle = module.multiply(string,cle)
    alphabet=module.alphabet

    tuples_list = []
    for s_letter,nbr in zip(string,range(0,len(string))):


        #print(str(alphabet.index(s_letter))+' : '+str(alphabet.index(cle[nbr])))
        tuples_list.append([str(alphabet.index(s_letter)),str(alphabet.index(cle[nbr]))])
    crypted = []
    for tuple_i in tuples_list:
        t1 = int(tuple_i[0])
        t2 = int(tuple_i[1])
        add_r = t1 - t2
        if add_r < 0:
            add_r = len(alphabet) + add_r
        crypted.append(alphabet[add_r])

    print('Decrypted : '+''.join(crypted))
    return (''.join(crypted))

def main():
    import sys
    arg1, arg2 = sys.argv[1], sys.argv[2]
    decrypt(arg1, arg2)

if __name__ == "__main__":
    main()

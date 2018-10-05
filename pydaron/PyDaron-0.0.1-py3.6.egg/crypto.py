

# -*- coding: utf-8 -*-

def crypt(string,key):

    import PyDaron.module as module

    cle = key




    alphabet=module.alphabet
    cle = module.multiply(string,cle)
    tuples_list = []
    crypted = []
    for s_letter,nbr in zip(string,range(0,len(string))):
        tuples_list.append([str(alphabet.index(s_letter)),str(alphabet.index(cle[nbr]))])
    print('\n')
    for tuple_i in tuples_list:
        t1 = int(tuple_i[0])
        t2 = int(tuple_i[1])
        add_r = t1 + t2
        if add_r > len(alphabet)-1:
            add_r = add_r-len(alphabet)
        crypted.append(alphabet[add_r])
    print('Message crypte : '+''.join(crypted))
    print('Cle : '+key)

    return [''.join(crypted),key]

def main():
    import sys

    arg1, arg2 = sys.argv[1], sys.argv[2]
    string = arg1
    key = arg2
    crypt(string,key)


if __name__ == "__main__":
    main()

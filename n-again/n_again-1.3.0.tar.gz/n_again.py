"""this is a simple expriment"""
import sys
def print_lol(the_list,indent=False,leavel=0,f=sys.stdout):
        for each in the_list:
                if isinstance(each,list):
                        print_lol(each,indent,leavel+1,f)
                else:
                        if indent:
                                for num in range(leavel):
                                        print("\t",end='',file=f)
                        print(each,file=f)



"""
input:(the_list,en_tab=False,tab=0,outfile=sys.stdout)
         列表， 是否使能缩进，缩进量，输出位置
ouput:print each_item in the list
date:2018/09/14
programer:Lee
"""
import sys

def print_list(the_list,en_tab=False,tab=0,outfile=sys.stdout):
        for each_item in the_list:
                if isinstance(each_item,list):
                        print_list(each_item,en_tab,tab+1,outfile)	#recursion
                else:
                        if en_tab:
                                for x in range(tab):
                                        print('\t',end='',file=outfile)
                        print(each_item,file=outfile)

			


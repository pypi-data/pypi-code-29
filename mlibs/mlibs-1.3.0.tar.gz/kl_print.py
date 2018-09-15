"""
input:list
ouput:print each_item in the list
date:2018/09/14
programer:Lee
"""

def print_list(the_list,en_tab=False,tab=0):
        for each_item in the_list:
                if isinstance(each_item,list):
                        print_list(each_item,en_tab,tab+1)	#recursion
                else:
                        if en_tab:
                                for x in range(tab):
                                        print('\t',end='')
                        print(each_item)

			


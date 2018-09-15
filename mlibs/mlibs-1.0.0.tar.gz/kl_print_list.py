"""
input:list
ouput:print each_item in the list
date:2018/09/14
programer:Lee
"""

def print_list(the_list):
        for each_item in the_list:
                if isinstance(each_item,list):
                        print_list(each_item)	#recursion
                else:
                        print(each_item)

			


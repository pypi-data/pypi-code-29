'''这是一个名为nester.py的模块，包含一个名为print_lol函数，这个函数的作用是打印
列表，其中有可能包含（也可能不包含）嵌套列表'''

def print_lol(the_list):

    '''这个函数去一个位置参数，名为'the_list',这可以是任何python列表（也可以是包含嵌套列表的列表）。
    所指定的列表中的每个数据项会递归地输入到屏幕上，每个数据项一行'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

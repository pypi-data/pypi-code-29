'''这是一个名为nester.py的模块，包含一个名为print_lol函数，这个函数的作用是打印
列表，其中有可能包含（也可能不包含）嵌套列表'''

def print_lol(the_list,level):

    '''这个函数去一个位置参数，名为'the_list',这可以是任何python列表（也可以是包含嵌套列表的列表）。
        所指定的列表中的每个数据项会递归地输入到屏幕上，每个数据项一行
        第二个参数用来在遇到嵌套列表时插入制表符'''
    
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end = "")
            print(each_item)




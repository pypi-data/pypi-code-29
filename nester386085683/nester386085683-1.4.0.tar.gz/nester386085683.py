'''此模块定义了一个递归函数，打印出列表中所有的元素'''
def print_lol(the_list,indent=False,level=0):
    '''此处开始为循环递归，当发现列表中还有列表时，继续递归遍历这个列表中的元素,
level表示缩进'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent==True:
                for i in range(level):
                    print('\t',end='')
            print(each_item)

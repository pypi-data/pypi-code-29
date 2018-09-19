
movies=["The Holy Grail",1975,
        "The Life of Brian",91,
        "The Meaning of Life",1971,
        ["Graham Chapman",
         ["Michael Palin","Terry Jones",
          "Terry Gilliam","Eric Idle","Terry Jones"
        ]],
        "The Blac Hero",147
        ]

"""
定义一个打印函数，打印列表中所有项
每个列表打印一行
the_list是需要打印的列表
flag是表示是否需要进行缩进,即每个列表是否进行缩进表示是一个列表
num表示缩进的量
flag和num都是用缺省设置
"""
def print_lot(the_list,flag=True,num=4):

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lot(each_item,flag,num+num)
        else:
             if flag:
                 for i in range(num):
                     print(' ',end='')
             print(each_item)
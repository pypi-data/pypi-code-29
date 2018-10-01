def TA(value, activate=False, New_line=True, seperater=':'):
    """有些人可能想要在LovU 之前添加上对方的名字,这样更加的暖,也更加的好玩儿.
    比如说,本函数默认情况下是不启用的, 那么这个时候,只是会输出例如: 我爱你 ,这样的简单语句.如果激活本函数,那么可以添加上 TA 的名字,比如说 xxx, 我爱你! ,或者是 xxx 我爱你!
    :param str value:
    :param bool activate: If set to True, receiver's name will be added to the message.If False, then the program will not add anything.
    :param bool New_line: If set to True, the message itself will be writen in the new line after the receiver's name. if False, the message and the receiver's name will be written in the same line.
    :param str seperater: you can choose use what to seperate the receiver's name and the message. for example ,you can use : , or any other marks that you would like to use.
    :return str:
    """
    if activate is False:
        TA = ''
        return TA
    if activate is True and New_line is True:
        name = value
        TA = name + seperater + "\n"
        return TA
    if activate is True and New_line is False:
        name = value
        TA = name + seperater 
        return TA
def sender(value, activate=False):
    """ 定义信息的发送者.
    :param str value:
    :param bool activate: If set to True, the sender name will be added to the message. 
    :return str:
    """
    if activate is True:
        sender = value
        Sender = "\n--:"+sender
        return Sender
from .getName import TA
from .me import sender
from .message import(
	show_all_langs_available,
    message
)

def LovU(TA='',TA=False, New_line=False, default_lang=False, seperater=':', sender=False, sender_name=''):
    """ This is the  main part of the functions.
    :param str TA: The person who you want to send this message?
    :param bool TA: If set to FALSE ,message just ignores the name of TA
    :param bool New_line: if set to True, message will be written in new line.
    :param bool default_lang: If set to True, you will be able to choose your message language.
    :param str seperater: you can have your own seperater between the message receiver and your message.
    :param bool sender: If set to yes, you can have your sender name.
    :param str sender_name: If you have set the sender param to True, please provide a sender name to the sender_name param.
    """
    if TA is False and sender is False and default_lang is False:
        message(default_lang=False)
        
    if TA is False and sender is False and default_lang is True: 
        message(default_lang=True)
        
    if TA is False and sender is True and default_lang is False:
        message=message(default_lang=False)
        Sender=sender(sender_name, activate=True)
        print(message+Sender)
        
    if TA is False and sender is True and default_lang is True:
        message=message(default_lang=True)
        Sender=sender(sender_name, activate=True)
        print(message+Sender)
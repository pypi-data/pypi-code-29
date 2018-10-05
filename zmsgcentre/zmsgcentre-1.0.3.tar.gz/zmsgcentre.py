# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    zmsgcentre.py
   Author :       Zhang Fan
   date：         2018/10/2
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import threading

message_list = {}

main_lock = threading.Lock()
tag_lock_list = {}


def add_listen(tag, callback, new_thread=False):
    if new_thread:
        threading.Thread(target=__add_listen, args=(tag, callback)).start()
    else:
        __add_listen(tag, callback)


def __add_listen(tag, callback):
    with main_lock:
        if tag not in message_list:
            message_list[tag] = [callback]  # callback_list
            tag_lock_list[tag] = threading.Lock()
            return

        callback_list = message_list[tag]  # type:list
        tag_lock = tag_lock_list[tag]

    with tag_lock:
        if callback not in callback_list:
            callback_list.append(callback)


def remove_listen(tag, callback, new_thread=False):
    if new_thread:
        threading.Thread(target=__remove_listen, args=(tag, callback)).start()
    else:
        __remove_listen(tag, callback)


def __remove_listen(tag, callback):
    with main_lock:
        if tag not in message_list:
            return

        callback_list = message_list[tag]
        tag_lock = tag_lock_list[tag]

    with tag_lock:
        if callback in callback_list:
            callback_list.remove(callback)


def clear_tag(tag, new_thread=False):
    if new_thread:
        threading.Thread(target=__clear_tag, args=(tag,)).start()
    else:
        __clear_tag(tag)


def __clear_tag(tag):
    with main_lock:
        if tag in message_list:
            del message_list[tag]
            del tag_lock_list[tag]


def clear_all_tag(new_thread=False):
    if new_thread:
        threading.Thread(target=__clear_all_tag).start()
    else:
        __clear_all_tag()


def __clear_all_tag():
    with main_lock:
        message_list.clear()
        tag_lock_list.clear()


def send(msg_tag, *args, **kwargs):
    with main_lock:
        if msg_tag not in message_list:
            return

        callback_list = message_list[msg_tag]
        tag_lock = tag_lock_list[msg_tag]

    with tag_lock:
        for callback in callback_list:
            callback(*args, **kwargs)


def trigger(tag):
    def decorator(func):
        def new_func(*args, **kwargs):
            send(tag, *args, **kwargs)

        return new_func

    return decorator


def receiver(tag):
    def decorator(func):
        add_listen(tag, func)
        return func

    return decorator


if __name__ == '__main__':
    @trigger('test')
    def fun_send(a, b, c):
        pass


    @receiver('test')
    def fun_callback_1(a, b, c):
        print('fun_1', a, b, c)


    @receiver('test')
    def fun_callback_2(a, b, c):
        print('fun_2', a, b, c)


    fun_send(1, 2, 3)

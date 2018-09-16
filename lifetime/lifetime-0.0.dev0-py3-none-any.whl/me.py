# Message Queue
import queue
activities = queue.Queue()

# Upload message
from requests import put, get
import threading, os
def upload():
    print("Uploading Thread Start")
    while(True):
        item = activities.get()
        print("upload item {0}".format(item))
#        threading.Thread(target=put, args=('/cheer',), kwargs={'json':item}).start()

def upload_thread():
    t = threading.Thread(target=upload)
    t.start()

# Capture inputs
from pynput import keyboard, mouse
from datetime import datetime
import json

data = {}

def add_item(func):
    def wrapper(*args, **kwargs):
        data['time'] = str(datetime.now())
        func(*args, **kwargs)
        json_data = json.dumps(data)
        activities.put(json_data)
    return wrapper

@add_item
def on_press(key):
    data['event'] = 'press'
    try:
        data['inner'] = str(key.char)
    except AttributeError:
        data['inner'] = str(key)
    if key == keyboard.Key.esc:
        os._exit(1)

@add_item
def on_release(key):
    data['event'] = 'release'
    try:
        data['inner'] = str(key.char)
    except AttributeError:
        data['inner'] = str(key)

@add_item
def on_click(x, y, button, pressed):
    data['event'] = 'click'
    data['inner'] = (x, y, str(button), pressed)

@add_item
def on_move(x, y):
    data['event'] = 'move'
    data['inner'] = (x, y)

@add_item
def on_scroll(x, y, dx, dy):
    data['event'] = 'scroll'
    data['inner'] = (x, y, dx, dy)

def listen_keyboard():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def listen_mouse():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

def listen_threads():
    t_key = threading.Thread(target=listen_keyboard)
    t_mou = threading.Thread(target=listen_mouse)
    t_key.start()
    t_mou.start()
    t_key.join()
    t_mou.join()

def main():
    upload_thread()
    listen_threads()

if __name__ == "__main__":
    main()
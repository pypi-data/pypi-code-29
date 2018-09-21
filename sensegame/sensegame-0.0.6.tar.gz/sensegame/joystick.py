import enum
import evdev
import threading

def _get_input_device():
    for k in [evdev.InputDevice(fn) for fn in evdev.list_devices()]:
        if k.name == "Raspberry Pi Sense HAT Joystick":
            return k

    raise RuntimeError("Unable to find Pi Sense HAT joystick!")

class Joystick(object):
    _code_to_key = {
        evdev.ecodes.KEY_UP: "UP",
        evdev.ecodes.KEY_DOWN: "DOWN",
        evdev.ecodes.KEY_LEFT: "LEFT",
        evdev.ecodes.KEY_RIGHT: "RIGHT",
        evdev.ecodes.KEY_ENTER: "CENTER"
    }

    def __init__(self):
        self._device = _get_input_device()
        self._current_key = None
        self._key_states = {m: False for m in self._code_to_key.values()}
        self._last_key_pressed = None

        self._key_callbacks = []
        self._key_press_callbacks = []
        self._key_release_callbacks = []

        self._thread = threading.Thread(target=self)
        self._thread.daemon = True
        self._thread.start()

    def register_key_callback(self, callback):
        self._key_callbacks.append(callback)

    def register_key_press_callback(self, callback):
        self._key_press_callbacks.append(callback)

    def register_key_release_callback(self, callback):
        self._key_release_callbacks.append(callback)

    @property
    def current_key(self):
        return self._current_key

    @property
    def key_states(self):
        return self._key_states

    @property
    def last_key_pressed(self):
        return self._last_key_pressed

    def pop_last_key_pressed(self):
        key = self._last_key_pressed
        self._last_key_pressed = None
        return key

    def __call__(self):
        for event in self._device.read_loop():
            if not event.type == evdev.ecodes.EV_KEY or not event.code in self._code_to_key:
                continue
            
            key = self._code_to_key[event.code]
            pressed = event.value != 0

            # Update current state of the key
            self._key_states[key] = pressed

            if pressed:
                self._last_key_pressed = key

            # Update latest key press
            if key == self._current_key and not pressed:
                self._current_key = None
            elif key != self._current_key and pressed:
                self._current_key = key

            # Handle all callbacks
            for callback in self._key_callbacks:
                callback(key)
            if pressed:
                for callback in self._key_press_callbacks:
                    callback(key)
            else:
                for callback in self._key_release_callbacks:
                    callback(key)

    def __getitem__(self, key):
        return self._key_states[key]

if __name__=="__main__":
    import time

    j = Joystick()
    while True:
        print("> %s" % j.current_key)
        print("> %s" % j.key_states)
        print("> %s" % j["CENTER"])
        time.sleep(0.1)

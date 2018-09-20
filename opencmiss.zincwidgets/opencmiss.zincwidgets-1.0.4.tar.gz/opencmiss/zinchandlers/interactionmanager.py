

class InteractionManager(object):

    def __init__(self):
        self._handlers = {}
        self._key_listeners = {}
        self._key_code_handler_map = {}
        self._active_handler = None
        self._fallback_handler = None

    def register_handler(self, handler):
        handler.set_scene_viewer(self)
        self._handlers[handler.get_mode()] = handler

        if hasattr(handler, 'get_key_code'):
            key_code = handler.get_key_code()
            self._key_code_handler_map[key_code] = handler

        if self._fallback_handler is None:
            self._fallback_handler = handler
            self._active_handler = handler

    def unregister_handler(self, handler):
        if handler != self._fallback_handler:
            self._handlers.pop(handler.get_mode())

            if hasattr(handler, 'get_key_code'):
                key_code = handler.get_key_code()
                self._key_code_handler_map.pop(key_code)

            if self._active_handler == handler:
                self._active_handler = self._fallback_handler

    def register_key_listener(self, key_code, listener):
        """
        Register a callback function 'listener' to be called when the key described by 'key_code' is released.
        Handler key codes take precedence over key listeners.
        :param key_code:
        :param listener: A callable that takes no parameters.
        :return:
        """
        self._key_listeners[key_code] = listener

    def unregister_key_listener(self, key_code):
        self._key_listeners.pop(key_code)

    def set_fallback_handler(self, fallback_handler):
        self._fallback_handler = fallback_handler

    def _change_handler_to(self, new_handler):
        if new_handler != self._active_handler:
            self._active_handler.leave()
            self._active_handler = new_handler
            self._active_handler.enter()

    def key_press_event(self, event):
        if event.key() in self._key_code_handler_map and not event.isAutoRepeat():
            event.accept()
            self._change_handler_to(self._key_code_handler_map[event.key()])
        elif event.key() in self._key_listeners:
            pass
        else:
            self._active_handler.key_press_event(event)

    def key_release_event(self, event):
        if event.key() in self._key_code_handler_map and not event.isAutoRepeat():
            event.accept()
            self._change_handler_to(self._fallback_handler)
        elif event.key() in self._key_listeners:
            self._key_listeners[event.key()]()
        else:
            self._active_handler.key_release_event(event)

    def mouse_enter_event(self, event):
        if self._active_handler is not None:
            self._active_handler.mouse_enter_event(event)

    def mouse_leave_event(self, event):
        if self._active_handler is not None:
            self._active_handler.mouse_leave_event(event)

    def mouse_press_event(self, event):
        """
        Handle a mouse press event in the scene viewer.
        """
        if self._active_handler is not None:
            self._active_handler.mouse_press_event(event)

    def mouse_release_event(self, event):
        if self._active_handler is not None:
            self._active_handler.mouse_release_event(event)

    def mouse_move_event(self, event):
        if self._active_handler is not None:
            self._active_handler.mouse_move_event(event)

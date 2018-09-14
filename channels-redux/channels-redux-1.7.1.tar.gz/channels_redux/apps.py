from django.apps import AppConfig


class ChannelsReduxConfig(AppConfig):
    name = 'channels_redux'

    def ready(self):
        from channels_redux import signals
        self.load_default_settings()
        super(ChannelsReduxConfig, self).ready()

    def load_default_settings(self):
        from channels_redux import app_settings as defaults
        from django.conf import settings

        for name in dir(defaults):
            if name.isupper() and not hasattr(settings, name):
                setattr(settings, name, getattr(defaults, name))

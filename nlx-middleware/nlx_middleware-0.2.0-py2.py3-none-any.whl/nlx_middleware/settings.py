import appsettings


class NLxMiddlewareSettings(appsettings.AppSettings):
    # inway configuration
    service = appsettings.StringSetting(required=True)
    inway_address = appsettings.StringSetting(required=True)
    organisation = appsettings.StringSetting(required=True)

    # outway config
    outway_address = appsettings.StringSetting(default='http://localhost:2018')

    # runtime flags to facilitate testing
    url_rewrite_enabled = appsettings.BooleanSetting(default=True)

    class Meta:
        setting_prefix = 'nlx_'


app_settings = NLxMiddlewareSettings()

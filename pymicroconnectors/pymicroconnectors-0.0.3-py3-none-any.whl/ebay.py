from ebaysdk.trading import Connection as Trading
import pymicroconnectors.config as config

api = None

def init():
    global api
    api = Trading(
        debug=config.get_value('ebay.debug'),
        token=config.get_value('ebay.token'),
        devid=config.get_value('ebay.devid'),
        appid=config.get_value('ebay.appid'),
        certid=config.get_value('ebay.certid'),
        domain=config.get_value('ebay.domain'),
        siteid=config.get_value('ebay.siteid'),
        config_file=None,
        warnings=True,
        timeout=20)
from flask import current_app as app, jsonify, abort, request
from arachne.scrapy_utils import start_crawler


def get_package(location):
    package = filter(lambda p: p != 'spiders', location.split('.')[1:-1])
    if len(package):
        return package[0]
    return None


def list_spiders_endpoint():
    """It returns a list of spiders available in the SPIDER_SETTINGS dict

    .. version 0.4.0:
        endpoint returns the spidername and endpoint to run the spider from
    """
    spiders = {}
    for item in app.config['SPIDER_SETTINGS']:
        package = get_package(item['location'])
        url = request.url_root + 'run-spider/' + item['endpoint']
        if package and package not in spiders:
            spiders[package] = {}

        if package:
            spiders[package][item['endpoint']] = url
        else:
            spiders[item['endpoint']] = url
    return jsonify(endpoints=spiders)


def run_spider_endpoint(spider_name):
    """Search for the spider_name in the SPIDER_SETTINGS dict and
    start running the spider with the Scrapy API

    .. version 0.4.0:
        endpoint returns the `status` as `running` and a way to go back to `home` endpoint
    """

    for item in app.config['SPIDER_SETTINGS']:
        if spider_name in item['endpoint']:
            spider_loc = '%s.%s' % (item['location'], item['spider'])
            start_crawler(spider_loc, app.config, item.get('scrapy_settings'))
            return jsonify(home=request.url_root, status='running', spider_name=spider_name)
    return abort(404)

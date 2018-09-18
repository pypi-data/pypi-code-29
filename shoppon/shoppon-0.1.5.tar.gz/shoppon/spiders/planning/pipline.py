from scrapy.item import Field
from scrapy.item import Item
from scrapy.pipelines.images import ImagesPipeline

from shoppon.logs import my_syslog

LOG = my_syslog.get_logger()


class ImgItem(Item):
    image_urls = Field()
    images = Field()


class ImgPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        super(ImagesPipeline, self).item_completed(results, item, info)

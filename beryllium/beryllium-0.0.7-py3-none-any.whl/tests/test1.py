# -*- coding: utf-8 -*-

from beryllium.beryllium import Beryllium
import time
from selenium.webdriver.common.touch_actions import TouchActions

if __name__ == "__main__":
    bery = Beryllium(is_open_devtools=True)
    bery.fast_get_page(url="https://m.fliggy.com")

    el = bery.until_presence_of_element_located_by_css_selector(
        css_selector="body > div > div:nth-child(2) > div > div > a > span")
    TouchActions(bery.get_driver()).tap(el).perform()

    time.sleep(10)

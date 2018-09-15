#!/usr/bin/env python
#coding:utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='scrapy-proxies-tool',
  version='0.4.0',
  keywords = ("Scrapy", "scrapy-proxies","proxies", "IPProxyTool"),
  description='Scrapy Proxies: random proxy middleware for Scrapy(support load proxies from IPProxyTool)',
  license = "MIT Licence",
  author='AnJia',
  author_email='anjia0532@gmail.com',
  url='https://github.com/anjia0532/scrapy-proxies',
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
)
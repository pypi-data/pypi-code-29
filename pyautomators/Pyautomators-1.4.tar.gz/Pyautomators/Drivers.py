# -*- coding: utf-8 -*-
'''
Created on 24 de ago de 2018

@author: koliveirab
'''
from selenium.webdriver import ChromeOptions


class Navegador():
    CHROME='Chrome'
    FIREFOX='Firefox'
    IE='Ie'
    EDGE='Edge'

    
class Options_Chrome():
    
    def __init__(self):
        self.options=ChromeOptions()
        
    def private(self):
        self.options.add_argument("--incognito")
    
    def backgroud(self):
        self.options.add_argument("--headless")
    
    def get_options(self):
        return self.options
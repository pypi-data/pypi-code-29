# -*- coding: utf-8 -*-
'''
Created on 24 de ago de 2018

@author: koliveirab
'''
from selenium.webdriver import ChromeOptions
from pytractor import webdriver as protactor
from selenium import webdriver
from .Error import Driver_erro

class Instancia_driver():
    def get_driver(self,drive,path_driver,options):
        if(type(drive)==str):
            driver=drive
            self.drive=drive
        else:
            driver=drive.valor
            self.drive=drive.valor
          
        if(driver == 'Chrome'):
            if(path_driver==None):
                path_driver="chromedriver"
            self.__driver=webdriver.Chrome(executable_path=path_driver,chrome_options=options)    
            
        elif(driver == 'Firefox'):  
            if(path_driver==None):
                path_driver="geckodriver"          
            self.__driver=webdriver.Firefox(executable_path=path_driver,firefox_options=options)
            
            
        elif(driver == 'Ie'):    
            if(path_driver==None):
                path_driver="IEDriverServer.exe"          
            self.driver=webdriver.Ie(executable_path=path_driver,ie_options=options)
        elif(driver == 'Edge'):    
            if(path_driver==None):
                path_driver="MicrosoftWebDriver.exe"          
            self.__driver=webdriver.Edge(executable_path=path_driver)
        else:
            Erro="""
                Não é um driver de servidor valido!
                Digite um driver valido:
                
                Ie
                Firefox
                Chrome    
                Edge 
                    """
            raise Driver_erro(Erro) 
        
        return self.__driver

class Instancia_driver_Angular():
    def get_driver(self,drive,path_driver,options):
        if(type(drive)==str):
            driver=drive
            self.drive=drive
        else:
            driver=drive.valor
            self.drive=drive.valor
        
        if(driver == 'Chrome'):
            if(path_driver==None):
                path_driver="chromedriver"
            self.__driver=protactor.Chrome(executable_path=path_driver,chrome_options=options)
            
                
        elif(driver == 'Firefox'):  
            if(path_driver==None):
                path_driver="geckodriver"          
            self.__driver=protactor.Firefox(str(path_driver),firefox_options=options)
            
            
        elif(driver == 'Ie'):    
            if(path_driver==None):
                path_driver="IEDriverServer.exe"          
            self.__driver=protactor.Ie(str(path_driver),ie_options=options)
        else:
            Erro="""
                Não é um driver de servidor valido!
                Digite um driver valido:
                
                Ie
                Firefox
                Chrome    
                    
                    """
            raise Driver_erro(Erro)

    
class Options_Chrome():
    
    def __init__(self):
        self.options=ChromeOptions()
        
    def private(self):
        self.options.add_argument("--incognito")
    
    def backgroud(self):
        self.options.add_argument("--headless")
    
    def get_options(self):
        return self.options
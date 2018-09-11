'''
Created on 24 de ago de 2018

@author: koliveirab
'''
import os 
from behave.__main__ import main
class Model_Runner_Container():
    
    @staticmethod
    def preparar_Web(parametros,path):
        STRING=[]
        #STRING.append("paths="+path)
        def _limpar(string):
            return string.replace('[','').replace(']','').replace('"','').replace("'",'')
        for parametro in parametros:
            if(parametro =="stdout_capture"):
                STRING.append("--capture")
            elif(parametro=="stderr_capture"):
                STRING.append("--capture-stderr")
            elif(parametro=="verbose" and parametros[parametro]==True):
                STRING.append("-v")
            elif(parametro=="summary"):
                STRING.append("--summary")
            elif(parametro=="color"):
                STRING.append("--color")
            elif(parametro=="log_capture"):
                STRING.append('--logcapture')
            elif(parametro=="junit"):
                STRING.append("--"+str("junit"))
            elif(parametro=="format"or parametro=='formato'):
                STRING.append('--format='+_limpar(str(parametros[parametro])))
            elif(parametro=="outline"or parametro=="saida"):
                STRING.append('-o='+_limpar(str(parametros[parametro])))
            elif(parametro=="tags"):
                string=_limpar(str(parametros[parametro]))
                STRING.append("--tags="+string)        
            
        
        return STRING
        
    @staticmethod
    def runner(List_parameter,tipo):
        if(tipo=="Funcional-web"):
            main(List_parameter)
        
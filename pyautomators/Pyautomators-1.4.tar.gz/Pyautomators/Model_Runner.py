'''
Created on 24 de ago de 2018

@author: koliveirab
'''
from behave.__main__ import main

import threading

        
class Modelador_Funcional():
    
    @staticmethod
    def Run_Pyautomators(dicionario_yaml,navegador):
        
        lista_de_execucao=["--capture",'-d','--junit','--junit-diretory=docs/reports/','--steps-catalog','--snippets','--multiline','--logcapture','--summary','--show-source','--show-timings','-v']
        for item in dicionario_yaml:
            if(item=='tags'):
                tag_string=str(",").join(item)
                lista_de_execucao.append("--tags="+tag_string)
            if(item=='args'):
                for arg in item:
                    lista_de_execucao.append('-D'+str(arg)+'='+str(item[arg]))
            if(item=='saida'):
                if(str(dicionario_yaml[item]).find('.json')==-1):
                    lista_de_execucao.append('--format=json.pretty')
                    lista_de_execucao.append('-o='+str(navegador).upper()+dicionario_yaml[item])
        return lista_de_execucao
    
class Thread_Run(threading.Thread):
    def __init__(self,Navegador,list_exec):
        threading.Thread.__init__(self)
        self.navegador=Navegador
        self.list_exec=list_exec
    def run(self):        
        main(Modelador_Funcional.Run_Pyautomators(self.list_exec, self.navegador))
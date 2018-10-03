'''
Created on 24 de ago de 2018

@author: koliveirab
'''
from behave.__main__ import main

import threading

        
class Modelador_Funcional():
    
    @staticmethod
    def Run_Pyautomators(dicionario_yaml,navegador):
        
        lista_de_execucao=["--capture",'--logcapture','-v','--no-junit','--capture','--capture-stderr']
        for item in dicionario_yaml:
            if(item=='tags'):
                for arg in dicionario_yaml[item]:
                    tag_string=str(",").join(dicionario_yaml[item])
                lista_de_execucao.append("--tags="+tag_string)
            if(item=='args'):
                for arg in dicionario_yaml[item]:
                    lista_de_execucao.append('-D'+str(arg)+'='+str(dicionario_yaml[item][arg]))
            if(item=='saida'):
                lista_de_execucao.append('--format=json.pretty')
                lista_de_execucao.append('-o='+str(navegador).upper()+dicionario_yaml[item])
        lista_de_execucao.append('-Dnavegador='+navegador)
        return lista_de_execucao
    
class Thread_Run(threading.Thread):
    def __init__(self,Navegador,list_exec):
        threading.Thread.__init__(self)
        self.navegador=Navegador
        self.list_exec=list_exec
    def run(self):   
        valor=Modelador_Funcional.Run_Pyautomators(self.list_exec, self.navegador) 
        main(valor)
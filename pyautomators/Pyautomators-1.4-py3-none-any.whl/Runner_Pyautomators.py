'''
Created on 26 de set de 2018

@author: koliveirab
'''
import argparse
from .Model_Runner import Thread_Run
import ast
   
if('__main__'==__name__):

    ARG=argparse.ArgumentParser()
    ARG.add_argument("-D",'--Dict_valor',required=True,help="Dicionario para a Execucao")
    ARG.add_argument("-d",'--diretorio_execucao',required=False,help="diretorio")
    
    valores=dict(vars(ARG.parse_args()))
    
    dicionario_de_execucao=ast.literal_eval(valores["Dict_valor"])
    for Navegador in dicionario_de_execucao['navegadores']:
        Thread_Run(Navegador,dicionario_de_execucao)
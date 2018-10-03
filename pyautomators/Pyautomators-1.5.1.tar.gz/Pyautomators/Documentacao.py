# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''
import pyautogui
import json
import behave2cucumber
from .Ambiente import _tratar_path
''' Este modulo tem o intuito de trabalhar a geração de artefatos, 
trabalhando com a entrada dos dados para o teste'''

def printarTela(NomeArquivo):
    '''Esta função retira prints da tela 
    parametros:
    NomeArquivo(obrigatorio): Nome do arquivo 
    
    Exemplo:
    printarTela("valor.png")''' 
    nome=_tratar_path(NomeArquivo)
    pyautogui.screenshot(nome) 

def print_local(xi,yi,xf,yf,NomeArquivo):
    '''Esta função retira prints da tela apartir de coordenadas pré estabelecidas
    parametros:
    xi,yi,xf,yf(obrigatorio):Coordenadas iniciais e finais para enquadrar o print
    NomeArquivo(obrigatorio): Nome do arquivo 
    
    Exemplo:
    print_local(10,200,100,1000"valor.png")''' 
    result= lambda a,b:b-a 
    xd=result(xi,xf)
    yd=result(yi,yf)
    nome=_tratar_path(NomeArquivo)
    return pyautogui.screenshot(nome,region=(xi,yi, xd, yd))
   
def tranforma_cucumber(NomeArquivo,novo=None):
    '''Esta função transforma o padrão de report json do Behave, em um padrão compativel com o Cucumber
    parametros:
    NomeArquivo(obrigatorio): Nome do arquivo 
    novo:Nome de um novo arquivo caso necessario gerar os dois, sendo o segundo o padrão json do Cucumber
    
    Exemplo:
    tranforma_cucumber("teste.json","teste2.json")'''
    nome=_tratar_path(NomeArquivo)
    valor=""
    with open(nome) as behave_json:
        cucumber_json = behave2cucumber.convert(json.load(behave_json))
        for element in cucumber_json:
            elemento=element["elements"]
            for lista in elemento:
                listaa=lista["steps"]
                for lis in listaa:
                    li=lis["result"]["duration"]
                    lis["result"]["duration"]=int(li*1000000000)
        valor=str(cucumber_json).replace("'",'"')
    if(novo is None):
        novo=nome
    arquivo = open(novo,'w')  
    conteudo=json.loads(valor)
    conteudo=json.dumps(conteudo,indent=4)         
    arquivo.write(conteudo)
    arquivo.close()
    return valor
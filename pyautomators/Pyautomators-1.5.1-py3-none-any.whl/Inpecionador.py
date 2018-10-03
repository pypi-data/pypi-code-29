# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''

''' Este modulo tem o intuito de trabalhar com a descoberta de elementos dinamicos ou de imagens dinamicas, 
inpeção de tela e de HTML'''
import pyautogui
from  urllib import request
from bs4 import BeautifulSoup
import re
from .Error import Elemento_erro

def tamanhoTela():
    '''Esta função retorna o tamanho da tela grafica
        Exemplo:
        VALOR=tamanhoTela()
        print(VALOR)
        >>>1225,1600'''
    return pyautogui.size()
 

def localizacao_imagem(imagem,centro=False):
    '''Esta função retorna o valor real na localicação da imagem passada       
        
        Exemplo:
        VALOR=localizacao_imagem("imagem.png")
        print(VALOR)
        >>>1000,200,1225,1600
        VALOR=localizacao_imagem("imagem.png",True)
        print(VALOR)
        >>>1000,200,1225,1600,'''
    valor=pyautogui.locateOnScreen(imagem)
    if(centro):
        valor=centralizar_pontos(valor)
    return valor

def localiza_todas_imagens(imagem,centro:bool=False):
    '''Esta função retorna o valor real na localicação de todas as encontradas pela imagem passada imagem passada        
        Exemplo:
        VALOR=localiza_todas_imagens("imagem.png")
        print(VALOR)
        >>>[(77, 601, 71, 52), (527, 601, 71, 52)]
        VALOR=localiza_todas_imagens("imagem.png",True)
        print(VALOR)
        >>>[(112, 627), (562, 627)]'''
    valor=list(pyautogui.locateAllOnScreen(imagem))
    if(centro):
        novo=[]
        for v in valor:
            v=centralizar_pontos(v)
            novo.append(v)
        valor=novo
    return valor

def centralizar_pontos(localizacao:tuple):
    '''Esta função gera o centro de pontos passados dentro de uma tupla       
        Exemplo:
        VALOR=localiza_todas_imagens("imagem.png")
        print(VALOR)
        >>>[(77, 601, 71, 52), (527, 601, 71, 52)]
        VALOR=localiza_todas_imagens("imagem.png",True)
        print(VALOR)
        >>>[(112, 627), (562, 627)]'''
    if(type(localizacao)==tuple):
        x,y=pyautogui.center(localizacao)
    else:
        Erro=r'''
        Para usar a centralicação use em forma de tupla
        Exemplo:
        
        centralizar_pontos((1416, 562, 50, 41))
        centraliar_pontos(localizacao_imagem("imagem.png"))'''
        raise Elemento_erro(Erro)
    return x,y
    
def get_html(url):
    '''Esta retorna o html de uma pagina especificada       
        Exemplo:
        
        get_html("http://pyautogui.readthedocs.io/en/latest/cheatsheet.html")
        '''
    response=request.urlopen(url)
    valor=response.read()
    soup=BeautifulSoup(valor,'html.parser')
    return soup

def valor_tag(url,tag,atributo):
    '''Esta retorna o uma tag de uma pagina html com o valor de um atributo da tag
        Exemplo:
        
        valor_tag("http://pyautogui.readthedocs.io/en/latest/cheatsheet.html","input","value")
        '''
    dicionario=[]
    tamanho=len(atributo)
    response=request.urlopen(url)
    valor=response.read()    
    soup=BeautifulSoup(valor,'html.parser')
    for line in soup.find_all(tag):
        if(re.search(str(atributo)+'="', str(line)) is not None):
            comeco=tamanho+2+int(str(line).find(str(atributo)+'="'))
            fim=int(str(line).find('"',comeco))
            dicionario.append((str(line)[comeco:fim],line))
    return dicionario     
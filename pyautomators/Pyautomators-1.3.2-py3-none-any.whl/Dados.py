# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''
import yaml
import json
import pytesseract as ocr
from PIL import Image
import pyautogui
import pandas
import os
from .Error import Dado_erro
''' Este modulo tem o intuito de trabalhar com dados de entrada para teste, 
trabalhando com a entrada dos dados para o teste'''

def receber_texto_usuario(descricao):
    '''Esta função abre um prompt com a descrição para a entrada de texto para a execução dos testes
    parametros:
    descricao(obrigatorio):Decrição que aparecera no prompt de entrada
    
    Exemplo:
    receber_texto("Entrar com valor de entrada:")'''    
    return pyautogui.prompt(text=descricao, title='prompt' , default='')

def tela_texto(xi:int, yi:int, xf:int, yf:int,renderizacao=False,x=500,y=100,limpar=True)->str:
    '''Esta função retira de um ponto expecifico da tela um valor apartir dos pontos inicias xi:yi, traçado um contorno ate xf:yf
    em uma tela, 
    a mesma retira um print podendo renderizar o tamanho da informação para melhorar a captura do dado
    
    parametros:
    xi,yi,xf,yf(obrigatorio):pontos para retangular o local que sera retirado a informação
    renderizacao:Se o valor for True e pode renderizar a imagem para um tamannho de leitura melhor do Tesseract
    x:y:Tamanho da foto Renderizada
    limpar:Exclui a imagem apos utilização
    
    Exemplo:
    tela_texto(1,100,50,200,True,200,300,False)'''
    language="eng"
    result=lambda a,b:b-a 
    xd=result(xi,xf)
    yd=result(yi,yf)
    if((type(xd) is float) or (type(yd) is float) or xd<=0 or yd<=0):
        Erro="""
                Os Valores de xi:yi e xf:yf estão errados
                tente seguir este padrão e contruir com valores inteiros:
                xf>xi
                Yf>yi"""
        raise Dado_erro(Erro)
    nome="teste.png"
    xd=xf-xi
    yd=yf-yi
    pyautogui.screenshot(nome,region=(xi,yi,xd,yd))
    if(renderizacao==True ):
        if(y<=0 or x<=0):
            Erro="""
                    Os Valores de x:y estão errados
                    tente seguir e contruir com valores inteiros
                    """
            raise Dado_erro(Erro)
        else:
            im = Image.open(nome)
            ims=im.resize((x, y),Image.ANTIALIAS)
            ims.save(nome,'png')
    im=Image.open(nome)    
    valor=ocr.image_to_string(im,lang=language)
    if(limpar):
        os.remove(nome)
    return valor
    
def pegarConteudoJson(NomeArquivo):
    '''Esta função retira o conteudo de um json e retorna um Dicionario
    
    parametros:
    NomeArquivo(obrigatorio):Nome do arquivo Json
    
    Exemplo:
    pegarConteudoJson("valor.json")'''
    arquivo = open(NomeArquivo.replace("\\","/"), 'r')
    lista = arquivo.read()
    arquivo.close()    
    jso=json.loads(lista)  
    return dict(jso)


def pegarConteudoCSV(NomeArquivo:str):
    '''Esta função retira o conteudo de um CSV e retorna um DataFrame
    
    parametros:
    NomeArquivo(obrigatorio):Nome do arquivo CSV
    
    Exemplo:
    pegarConteudoCSV("valor.csv")'''
    valor=pandas.read_csv(NomeArquivo)
    valor=pandas.DataFrame(valor)
    return valor
    
def pegarConteudoXLS(NomeArquivo:str,Planilha:str):
    '''Esta função retira o conteudo de um Excel e retorna um DataFrame
    
    parametros:
    NomeArquivo(obrigatorio):Nome do arquivo XLS
    Planilha: Qual planilha deve ser retirado o conteudo
    
    Exemplo:
    pegarConteudoXLS("valor.xls","Planilha1")'''
    valor=pandas.read_excel(NomeArquivo,sheet_name=Planilha)
    valor=pandas.DataFrame(valor)
    return valor

def pegarConteudoYAML(NomeArquivo):
    arquivo=open(NomeArquivo,"r")
    
    return yaml.load(arquivo)
    
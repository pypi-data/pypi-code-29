# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''

''' Esta modulo tem o intuito de trabalhar em conjunto do sistema operacional, 
trabalhando com diretorios, arquivos(Nao seus conteudos) e partes do sistema'''
import os
import time
from collections import deque
import shutil
from .Error import Ambiente_erro
 
def _tratar_path(diretorio):
    '''Esta função trata uma path, deixando ela sempre no mesmo padrão para o entendimento do sistema operacional'''
    if(type(diretorio)==list):
        for arquivo in diretorio:
            arquivo=arquivo.replace("\\", "/")
        dir=diretorio
    else:
        dir=diretorio.replace("\\", "/")
    return dir

def irDiretorio(diretorio):
    r'''Esta função muda seu diretorio na sua linha de comando para outro diretorio
        Exemplo:
        irDiretorio("C:/User/cafe")
        irDiretorio("C:\User\cade")'''
    os.chdir(_tratar_path(diretorio))

def criarPasta(nomePasta):
    '''Esta função cria um diretorio
        Exemplo:
        criarPasta("C:/User/NovaPasta")
        criarPasta("NovaPasta")<- Não ha necessidade de passar o caminho, ou pode se criar outros diretorios dentro de diretorios'''
    os.mkdir('./'+nomePasta)

def abrirPrograma(programa):
    r'''Esta função execulta um programa(que for execultavel como permissao)
    Exemplo:
    abrirPrograma("C:\Program Files (x86)\Notepad++\notepad++.exe")'''
    return os.startfile(_tratar_path(programa))

def comandLine(command):
    '''Esta função execulta uma instrução na linha de comando, dentro do seu ditorio atual
    Exemplo:
       comandLine("mkdir novaPasta") '''
    os.system(command)

def dia_mes_ano():
    '''Esta função retorna o dia, mes e ano da sua maquina
    Exemplo:
    valor=dia_mes_ano()
    print(valor)
    >>>[16,7,2018]
    '''
    line=time.localtime()
    line=list(line)
    lis=deque()
    for h in line:
        lis.appendleft(int(h))
        if(line.index(h) == 2):
            break
    return list(lis)

def path_atual(Com_seu_diretorio=True):
    '''Esta função retorna o caminho ate o seu diretorio, por parametro você pode retirar 
    com False a sua pasta atual da path, retornando somente o caminho
    Exemplos:
    path=path_atual()
    print(path)
    >>>C:/User/administrador/[pastaAtual]/
    Ou
    path=path_atual(False)
    print(path)
    >>>C:/User/administrador/
    '''
    diretorio=None
    if(Com_seu_diretorio):
        diretorio=_tratar_path(str(os.getcwd()))
    elif(not Com_seu_diretorio):
        diretorio=_tratar_path(str(os.path.dirname(os.getcwd())))
        
    return diretorio+"/"

def copiar_aquivos_diretorio(path_arquivo1:str,path_arquivo2:str):
    r'''Esta função copia o conteudo de um arquico para outro arquivo, passando o caminho conseguimos colocar em outro
    diretorio
    Exemplo::
    copiar_aquivos_diretorio(r"C:\Users\administrador\Desktop\Cenarios.txt", "Features/Cenario.txt")'''
    Erro=r'''
        Para copiar um arquivo de diretorio, passe uma String do arquivo que deseja copiar e uma String do arquivo alvo
        Exemplo:
        copiar_aquivos_diretorio(r"C:\Users\administrador\Desktop\Cenarios.txt", "Features/Cenario.txt")'''
    path_arquivo1=_tratar_path(path_arquivo1)
    path_arquivo2=_tratar_path(path_arquivo2)
    if(type(path_arquivo1) == str and type(path_arquivo2) == str):
        try:
            shutil.copyfile(path_arquivo1, path_arquivo2)
        except:
            raise Ambiente_erro(Erro)
    else:
        
        raise Ambiente_erro(Erro)
    
    
def mover_arquivos_diretorio(path_arquivo1:str,path_2:str):
    r'''Esta função mode o conteudo de um arquico para outro diretorio
    Exemplo::
    mover_arquivos_diretorio(r"C:\Users\administrador\Desktop\Cenarios.txt", "Features/")'''
    Erro=r'''
        Para mover um arquivo de diretorio, passe uma String do arquivo que deseja copiar e uma String do diretorio alvo
        Exemplo:
        mover_arquivos_diretorio(r"C:\Users\administrador\Desktop\Cenarios.txt", "Features/")'''
    path_arquivo1=_tratar_path(path_arquivo1)
    path_arquivo2=_tratar_path(path_2)
    if(type(path_arquivo1) == str and type(path_2) == str):
        try:
            shutil.move(path_arquivo1, path_arquivo2)
        except:
            raise Ambiente_erro(Erro)
    else:
        
        raise Ambiente_erro(Erro)
        
def remover_arquivo(NomeArquivo:str):
    '''Esta função exclui um arquivo'''
    NomeArquivo=_tratar_path(NomeArquivo)
    os.remove(NomeArquivo)
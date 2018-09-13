# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''

import threading
import docker

from .Run import Modelador_Funcional

class Esvalavel(threading.Thread):
            def __init__(self,Image,Runner):
                '''Super Classe Thread'''
                threading.Thread.__init__(self)
                '''Recebendo um agente docker'''
                self.client=docker.from_env()
                '''Recebendo um atributo Imagem'''
                self.Image=Image
                '''Recebendo o comando para rodar'''
                self.Runner=Runner
                
            def run(self):    
                '''Rodando o container '''   
                self.client.containers.run(image=self.Image, command=self.Runner,remove=True)
                
class Runner_Container():
    
    def Runner_line(self,Imagem,Folder):
        lista=[]
        for f in Folder:
            '''Verificando se é funcional web'''
            if(Folder[f]["tipo"]=="Funcional-Web"):
                lista.append(Esvalavel(Imagem,Modelador_Funcional.preparar_comand_line(f)))
        
        for l in lista:
            '''start dos testes no container '''
            l.start()



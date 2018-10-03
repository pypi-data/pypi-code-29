# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''

import threading
import docker
class Escalavel_web(threading.Thread):
    def __init__(self,Image,volume,command):
        '''Super Classe Thread'''
        threading.Thread.__init__(self)
        '''Recebendo um agente docker'''
        self.client=docker.from_env()
        '''Recebendo um atributo Imagem'''
        self.Image=Image
        self.volume=volume
        self.command=command
        
    def run(self):    
        '''Rodando o container '''   
        self.client.containers.run(image=self.Image,command="python3 -m Pyautomators.Runner_Pyautomators -D={}".format(self.command),volumes=self.volume,remove=True)
        
class Runner_Container:
    
    def Runner_line(self,Folder,Image,volume):
        for container in Folder:
            if(Folder[container]['tipo']=='TESTE - WEB'):
                Escalavel_web(Image,volume,str(Folder[container]).replace(' ','')).start()
                
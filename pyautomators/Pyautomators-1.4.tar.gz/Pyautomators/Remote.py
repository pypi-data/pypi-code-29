'''
Created on 12 de set de 2018

@author: koliveirab
'''
import http.server
import socketserver
import socket
import ast
from .Runner_Pyautomators import Thread_Run
''' Esta modulo tem o intuito de trabalhar em conjunto comunica��o entre sistemas e gera��o de Threads, 
trabalhando com cloud, processos e sistemas provedores de servi�os de nuvem e docker'''
def servidor_http(endereco:str,porta:int):
    '''Esta fun��o tem como principio gerar um servidor http'''
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((endereco, porta), Handler)
    httpd.serve_forever()

class Runner_Client():
    def __init__(self,Server):
        self.Client=socket.socket()
        host,port=Server, 9000
        self.Client.connect((host,port))
        """Conectando ao servidor"""
        valor=self.Client.recv(1024).decode("utf8")
        jsons=ast.literal_eval(valor)
        """ Aguardando resposta da conexao com o valor para rodar o teste"""
        if(jsons["tipo"]=="Funcional-web"):
            for navegador in jsons['navegadores']:
                Thread_Run(navegador,jsons)
        
        
class Controler_Remote_Runner():
    
    def __init__(self,Folder):
        self.Server=socket.socket()
        self.parameter=Folder
        self.Instancias=len(Folder) 
        """ Preparando """   
        def Preper(self):
            self.Endereco=(socket.gethostbyname(socket.gethostname()),9000)
            self.Server.bind(self.Endereco)
            self.Server.listen(self.Instancias)
            print('Server:{}\nQuanditade de acessiveis:{}'.format(self.Endereco,self.Instancias))
        Preper(self)
        
    def Runner(self):    
        lista=[]             
        def iniciar():
            for paramete in self.parameter:
                c,addr =self.Server.accept()          
                print(addr)
                lista.append(addr)
                print(paramete)
                c.send(str(self.parameter[paramete]).encode('utf_8'))
        iniciar()
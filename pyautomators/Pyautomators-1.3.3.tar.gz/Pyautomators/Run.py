'''
Created on 24 de ago de 2018

@author: koliveirab
'''
import os 
from behave.__main__ import main
import threading
import docker

class Model_Runner_Main():
    
    @staticmethod
    def preparar_main(parametros,path):
        STRING=[]
        #STRING.append("paths="+path)
        def _limpar(string):
            return string.replace('[','').replace(']','').replace('"','').replace("'",'')
        for parametro in parametros:
            if(parametro =="stdout_capture"):
                STRING.append("--capture")
            elif(parametro=="stderr_capture"):
                STRING.append("--capture-stderr")
            elif(parametro=="verbose" and parametros[parametro]==True):
                STRING.append("-v")
            elif(parametro=="summary"):
                STRING.append("--summary")
            elif(parametro=="color"):
                STRING.append("--color")
            elif(parametro=="log_capture"):
                STRING.append('--logcapture')
            elif(parametro=="junit"):
                STRING.append("--"+str("junit"))
            elif(parametro=="format"or parametro=='formato'):
                STRING.append('--format='+_limpar(str(parametros[parametro])))
            elif(parametro=="outline"or parametro=="saida"):
                STRING.append('-o='+_limpar(str(parametros[parametro])))
            elif(parametro=="tags"):
                string=_limpar(str(parametros[parametro]))
                STRING.append("--tags="+string)        
            
        
        return STRING
        
    @staticmethod   
    def preparar_comand_line(List_parameter):
        STRING="behave"
        def _limpar(string):
            return string.replace('[','').replace(']','').replace('"','').replace("'",'')
        for parametro in List_parameter:
            if(parametro =="stdout_capture"):
                STRING+=" --capture"
            elif(parametro=="stderr_capture"):
                STRING+=" --capture-stderr"
            elif(parametro=="verbose" and List_parameter[parametro]==True):
                STRING+=" -v"
            elif(parametro=="summary"):
                STRING+=" --summary"
            elif(parametro=="color"):
                STRING+=" --color"
            elif(parametro=="log_capture"):
                STRING+=' --logcapture'
            elif(parametro=="junit"):
                STRING+=" --junit"
            elif(parametro=="format"or parametro=='formato'):
                STRING+=str(' --format='+_limpar(str(List_parameter[parametro])))
            elif(parametro=="outline"or parametro=="saida"):
                STRING+=str(' -o='+_limpar(str(List_parameter[parametro])))
            elif(parametro=="tags"):
                string=_limpar(str(List_parameter[parametro]))
                STRING.append(" --tags="+string)        
        return STRING
    @staticmethod
    def runner(List_parameter,tipo):
        if(tipo=="Funcional-web"):
            main(List_parameter)
            
class Model_Runner_Funcional_Web():
    
    def __init__(self,Imagem,Folder):
        class Thread (threading.Thread):
            def __init__(self,Image,Runner):
                threading.Thread.__init__(self)
                self.client=docker.from_env()
                self.Image=Image
                self.Runner=Runner
            def run(self):       
                self.client.containers.run(image=self.Image, command=self.Runner,remove=True)
        for f in Folder:
            if(f["tipo"]=="Funcional-web"):
                path=os.getcwd()
                for jsos in f:
                    if jsos=='path':
                        path=f[jsos]
                modelo=Model_Runner_Main.preparar_comand_line(f,path=path)
            self.container=Thread(Imagem,modelo)
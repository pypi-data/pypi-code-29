# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''
import os 
from selenium import webdriver 
from .mouse_teclado import Teclado
from .mouse_teclado import Mouse
from .Verifica import Valida
from .Error import Elemento_erro

''' Este arquivo tem o intuito dos metodos em selenium para Desktop,
    na qual os passamos um elemento chave e seu tipo e ele executa a acao descrita'''

class Desk(Teclado,Mouse,Valida):
    ''' Esta classe tem o intuito de prover conexão com selenium em Desktop'''
    def __init__(self,Driver_Winium,aplicacao:str):
        '''No construtor temos dois parametros sendo um obrigatorio
        
        Driver_Winium(obrigatorio):Local Aonde esta o Driver do Winium
        aplicacao(obrigatorio): Qual Aplicação será Testada
        '''
        os.startfile(Driver_Winium)
        self.driver= webdriver.Remote(command_executor="http://localhost:9999",desired_capabilities={"app": aplicacao})
        self.tipo='desk'
    def fechar_programa(self):
        '''Este metodo fecha conexão com o driver. Exemplo: fechar()'''
        self.driver.close()
        os.system("TASKKILL /IM Winium.Desktop.Driver.exe")
        
    @staticmethod
    def Open_comandLine(Comand):
        '''Este metodo abre a aplicação apartir de uma linha de comando
        Exemplo:
        Open_comandLine("C:/APP/main_interface.exe")'''
        os.system(Comand)
        
    def elemento(self,elemento,tipo,implicit=None):
        r'''Esta procura um elemento e retorna o objeto do elemento
        parametros:
        elemento(obrigatorio):elemento que deve ser procurado
        tipo(obrigatorio): tipo do elemento que sera procurado
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        
        Exemplos:
        elemento("id.user","id",10)
        elemento("class_user_login","class",1)
        elemento("login","name")
        
       lista de elementos:
        
        id:    Desk    <form id="loginForm"> = 'loginForm'
        
        name:    Desk    <input name="username" type="text" /> = 'username'
        
        class:    Desk     <p class="content">Site content goes here.</p> = 'content'
        
        xpath:    Desk <html>                    =    '/html/body/form[1]' ou '//form[1]' ou '//form[@id='loginForm']'
                                     <body>
                                      <form id="loginForm">
                                          
        '''
        if(implicit!=None):
            self.driver.implicitly_wait(implicit)
        if(tipo == 'id'):
            element=self.driver.find_element_by_id(elemento)
        elif(tipo == 'name'):
            element=self.driver.find_element_by_name(elemento) 
        elif(tipo == 'class'):            
            element=self.driver.find_element_by_class_name(elemento) 
        elif(tipo == 'xpath'):            
            element=self.driver.find_element_by_xpath(elemento) 
        
        
        else:
            Erro="""
                Escolha um valor de elemento Valido
                lista de elementos:
                id:    Desk
                name:    Desk
                class:    Desk
                xpath:    Desk
                               
                """
            raise Elemento_erro(Erro)
        return element
      
    def elemento_list(self,elemento,tipo,indice_lista):
        '''Esta procura um elemento  dentro de uma lista de elementos com o mesmo parametro
        parametros:
        elemento(obrigatorio):elemento que deve ser procurado
        tipo(obrigatorio): tipo do elemento que sera procurado
        indice_lista(obrigatorio):Indice de ordem do elemento na lista
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        
        Exemplos:
        elemento_list("id.user","id",0,10)
        elemento_list("class_user_login","class",3,1)
        elemento_list("login","name",2)
        
        lista de elementos:
        
        id:    Desk    <form id="loginForm"> = 'loginForm'
        
        name:    Desk    <input name="username" type="text" /> = 'username'
        
        class:    Desk     <p class="content">Site content goes here.</p> = 'content'
        
        xpath:    Desk <html>                    =    '/html/body/form[1]' ou '//form[1]' ou '//form[@id='loginForm']'
                                     <body>
                                      <form id="loginForm">
                                      
        
        '''
        elements=self.elementos_list(elemento, tipo)
        element=elements[indice_lista]
        return element
    
    def elementos_list(self,elemento,tipo):
        '''Esta procura todos os elementos de elementos com o mesmo parametro
        parametros:
        elemento(obrigatorio):elemento que deve ser procurado
        tipo(obrigatorio): tipo do elemento que sera procurado
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        
        Exemplos:
        elementos_list("id.user","id",10)
        elementos_list("class_user_login","class",1)
        elementos_list("login","name")
        
        lista de elementos:
        
        id:    Desk    <form id="loginForm"> = 'loginForm'
        
        name:    Desk    <input name="username" type="text" /> = 'username'
        
        class:    Desk     <p class="content">Site content goes here.</p> = 'content'
        
        xpath:    Desk <html>                    =    '/html/body/form[1]' ou '//form[1]' ou '//form[@id='loginForm']'
                                     <body>
                                      <form id="loginForm">
                                      
         
        '''
        if(tipo == 'id'):           
            elements=self.driver.find_elements_by_id(elemento)  
        elif(tipo == 'name'):
            elements=self.driver.find_elements_by_name(elemento)
        elif(tipo == 'class'):            
            elements=self.driver.find_elements_by_class_name(elemento)
        elif(tipo == 'xpath'):            
            elements=self.driver.find_elements_by_xpath(elemento)
        
        else:
            Erro="""
                Escolha um valor de elemento Valido
                lista de elementos:
                id:    Desk
                name:    Desk
                class:    Desk
                xpath:    Desk
               
                
                """
            raise Elemento_erro(Erro)
        return elements
    
    def escreve(self,elemento,conteudo,tipo,implicit=None):
        '''Este metodo escreve em um elemento, na qual temos cinco parametros
        
        elemento(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        conteudo(obrigatorio): Conteudo na qual queremos inserir naquele elemento
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        tempo:É o tempo que leva para escrever cada tecla.
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <input class="gsfi" id="lst-ib" maxlength="2048" name="q" autocomplete="off" title="Pesquisar" >
                
                 escreve("gsfi","QUALQUER TEXTO","class",10,0.1)
        '''
        
        element=self.elemento(elemento,tipo,implicit) 
        element.send_keys(conteudo)
        return element
    
           
    def clica(self,elemento,tipo,implicit=None):
        '''Este metodo clica em um elemento, na qual temos tres parametros
        
        elemento(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <input class="gsfi" id="lst-ib" maxlength="2048" name="q" autocomplete="off" title="Pesquisar" >
                
                clica("gsfi","class",10)
        '''
        
        element=self.elemento(elemento,tipo,implicit) 
        element.click()
        return element
             
    
    
                
    def escrever_elemento_lista(self,elemento,conteudo,tipo,indice_lista:int):
        '''Este metodo escreve em um elemento de uma lista de elementos com o mesmo tipo e elemento, na qual temos seis parametros
        
        elemento(obrigatorio): Qual é o elemento que iremos buscar para realizar a busca na lista de elementos com a mesma descricao
        conteudo(obrigatorio): Conteudo na qual queremos inserir naquele elemento
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        indice_lista(obrigatorio): Qual dos itens que achamos queremos usar, este sempre retorna uma lista na ordem que foi achado 
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        tempo:É o tempo que leva para escrever cada tecla.
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <input name="btn" type="submit" jsaction="sf.lck">
                <input name="btn" type="submit" jsaction="sf.chk">
                
                escrever_elemento_lista("input","QUAL QUER TEXTO","tag",2,10,0.1)
        '''
        element=self.elemento_list(elemento,tipo,indice_lista)
        element.send_keys(conteudo)     
            
    def clica_elemento_lista(self,elemento,tipo,indice_lista:int):
        '''Este metodo clica em um elemento de uma lista de elementos com o mesmo tipo e elemento. na qual temos quatro parametros
        
        elemento(obrigatorio): Qual é o elemento que iremos buscar para realizar a busca na lista de elementos com a mesma descricao
        indice_lista(obrigatorio): Qual dos itens que achamos queremos usar, este sempre retorna uma lista na ordem que foi achado
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <input name="btn" type="submit" jsaction="sf.lck">
                <input name="btn" type="submit" jsaction="sf.chk">
                
                clica_elemento_lista("input","tag",1,10)
        '''
        element=self.elemento_list(elemento,tipo,indice_lista)
        element.click()
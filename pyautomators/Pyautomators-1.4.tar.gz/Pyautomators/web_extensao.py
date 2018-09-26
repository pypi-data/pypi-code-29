# -*- coding: utf-8 -*-
'''
Created on 24 de ago de 2018

@author: koliveirab
'''
import logging
from selenium.webdriver.support.events import AbstractEventListener
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from .Error import Dado_erro 
from .Error import Elemento_erro

class Js_Script():
    
    def __init__(self,drive):
        self.driver=drive
        
    def execute_script(self,script):
        '''Este metodo executa comando javascript no console do navegador
        
            parametros:
            script(obrigatorio):o script a ser executado
           Exemplo:
        ("window.scrollTo(0, document.body.scrollHeight);")'''
        self.driver.execute_script(script)   
        

'''Este Modulo trabalha com as esperas feitas pelo WebDriverWait'''
class Aguarde_elemento():
    ''' Esta classe tem o intuito de prover conexao com o WevDriverWait'''
    
    
    
    def __condition(self,condicao,**parametro):
        ''' Este metodo trabalha com as especificacao das esperas'''
        if(condicao is 'visivel'):
            return expected_conditions.visibility_of_element_located((self.__condition(parametro['tipo']),parametro['elemento']))
        elif(condicao is 'clicavel'):
            return expected_conditions.element_to_be_clickable((self.__condition(parametro['tipo']),parametro['elemento']))
        elif(condicao is 'alerta_presente'):
            return expected_conditions.alert_is_present(parametro['driver'])
        elif(condicao is 'nova_janela_aberta'):
            return expected_conditions.new_window_is_opened(parametro['janela'])
        elif(condicao is 'titulo_ser_igual_a'):
            return expected_conditions.title_is(parametro['texto'])
        elif(condicao is 'url_contem'):
            return expected_conditions.url_contains(parametro['texto'])
        elif(condicao is 'titulo_ser_igual_a'):
            return expected_conditions.text_to_be_present_in_element((self.__condition(parametro['tipo']),parametro['elemento']),parametro['texto'])
        else:
            Erro='''Coloque uma condição valida:
                    
                    visivel:elemento visivel na tela
                    clicavel:é possivel clicar neste elemento
            '''
            raise Dado_erro(Erro)
        
        
    def __definir_by(self,elemento):
        if(elemento=='id'):
            return By.ID
        elif(elemento=='class'):
            return By.CLASS_NAME
        elif(elemento=='xpath'):
            return By.XPATH
        elif(elemento=='name'):
            return By.NAME
        elif(elemento=='tag'):
            return By.TAG_NAME
        elif(elemento=='partial_link'):
            return By.PARTIAL_LINK_TEXT
        elif(elemento=='link'):
            return By.LINK_TEXT
        elif(elemento=='css'):
            return By.CSS_SELECTOR
        else:
            Erro="""
            Escolha um valor de elemento Valido
            lista de elementos:
            id:    Desk,Web,Mobile
            name:    Desk,Web,Mobile
            class:    Desk,Web,Mobile
            xpath:    Desk,Web,Mobile
            link:    Web
            tag:    Web,Mobile
            css:    Web,Mobile
            partial_link:    Web
            
            
            """
            raise Elemento_erro(Erro)
        
    def aguarde_condicao(self,condicao,tempo=10,intervalo=0.5,menssagem_exception='',**parametros):
        ''' Este metodo trabalha com o aguarde trazendo uma condicao para o aguarde explicito
        retorna o elemento
        parametros:
            elemento(obrigatorio):Valor do elemento que sera esperado
            tipo(obrigatorio):Tipo de elemento que sera gerado
            condicao(obrigatorio):Condicao de espera
            tempo: valor de tentativas
            intervalo:intervalo em cada tentativa
            menssagem_exception:mensagem que sera gerada caso de erro
        Exemplo:
            aguarde_condicao('user.login','id','visivel',15,2)
            aguarde_condicao('user.login','id','clicavel')'''
        
        
        wait=WebDriverWait(self.driver,tempo,intervalo)
        
        return wait.until(self.condicao(condicao,parametros),menssagem_exception)



class Simula():
    
    def mover_mouse(self,elemento,tipo,implicit=0):
        self.ActionChains.move_to_element(self.elemento(elemento,tipo,implicit)).perform()
        
    def duplo_clique(self,elemento,tipo,implicit):
        self.ActionsChains.double_click(self.elemento(elemento,tipo,implicit)).perform()
        
    def clique(self,elemento,tipo,implicit,Botao='left'):
        if(Botao=="left"):
            self.ActionsChains.click(self.elemento(elemento,tipo,implicit)).perform()
        elif(Botao=='rigth'):
            self.ActionsChains.context_click(self.elemento(elemento,tipo,implicit)).perform()
        else:
            Erro="""
                Escolha um valor Valido
                Os Valores são:
                left ou rigth
                
                """
            raise Elemento_erro(Erro)
        
    def clique_arraste(self,elemento1,tipo1,implicit1,elemento2,tipo2,implicit2):
        self.ActionsChains.drag_and_drop(self.elemento(elemento1,tipo1,implicit1),self.elemento(elemento2,tipo2,implicit2)).perform()
        
    def digitos(self,elemento,tipo,implicit,lista_de_chaves):
        self.ActionsChains.send_keys_to_element(self.app.elemento(elemento,tipo,implicit),*lista_de_chaves).perform()
        
class Alerta():
    def __init__(self,driver):
        self.alert=Alert(driver)
        
    def aceitar(self):
        self.alert.accept()
        
    def rejeitar(self):
        self.alert.dismiss()
        
    def inserir_texto(self,texto):
        self.alert.send_keys(texto)
        
    def get_texto(self):
        return self.alert.text
    
class select_model():
    
    def deselect(self,elemento,tipo,tipo_selecao,valores_de_manipulacao):
            '''Este metodo trabalha com listas <Select> para preenchimento 
            parametros:
            elemento(obrigatorio): elemento do select
            valores_manipulacao: lista de elementos a ser selecionados ou deselecionados, se ele nao for passado ele seleciona todos
            tipo_selecao: tipos de selecao para ser usado que pode ser:valor,index e texto, ele nao selecionada todos 
            deselect:se True ele retira ao invez de selecionar
            
            Exemplo:
            
            deselect(app.elemento('user.select.list','id'),['masculino','São Paulo'],'texto')
            
            '''
            Erro="""
                                Não é um tipo de seleção valido
                                Digite um tipo valido:
                                
                                index
                                valor
                                texto    
                                    
                                    """
            select=Select(self.elemento(elemento,tipo))
            
                
            for valor in valores_de_manipulacao:
                if(tipo_selecao=='index'):
                    select.deselect_by_index(int(valor))
                elif(tipo_selecao=='valor'):
                    select.deselect_by_value(valor)
                elif(tipo_selecao=='texto'):
                    select.deselect_by_visible_text(valor)
                else:                        
                    raise Elemento_erro(Erro)  
            
                        
    def select(self,elemento,tipo,tipo_selecao,valores_de_manipulacao):
            '''Este metodo trabalha com listas <Select> para preenchimento 
            parametros:
            elemento(obrigatorio): elemento do select
            valores_manipulacao: lista de elementos a ser selecionados ou deselecionados, se ele nao for passado ele seleciona todos
            tipo_selecao: tipos de selecao para ser usado que pode ser:valor,index e texto, ele nao selecionada todos 
            deselect:se True ele retira ao invez de selecionar
            
            Exemplo:
            
            select(app.elemento('user.select.list','id'),['masculino','São Paulo'],'texto')
            
            '''
            Erro="""
                                Não é um tipo de seleção valido
                                Digite um tipo valido:
                                
                                index
                                valor
                                texto    
                                    
                                    """
            select=Select(self.elemento(elemento,tipo))
            
            for valor in valores_de_manipulacao:
                if(tipo_selecao=='index'):
                    select.select_by_index(int(valor))
                elif(tipo_selecao=='valor'):
                    select.select_by_value(valor)
                elif(tipo_selecao=='texto'):
                    select.select_by_visible_text(valor)
                else:
                    raise Elemento_erro(Erro)
                
    def deselect_all(self,elemento,tipo):
            
            select=Select(self.elemento(elemento,tipo))
            
            select.deselect_all()
            

class MyListener(AbstractEventListener):
    def __init__(self,Log):
        self.Log=Log
        logging.basicConfig(filename=Log,level=logging.INFO)
    
    def before_navigate_to(self, url, driver):
        log="Navegando Para {}".format(url)
        logging.info(str(log))
        
    def after_navigate_to(self, url, driver):
        log="Sucesso para a url: {}".format(url)
        logging.critical(log)
        

    def before_navigate_back(self, driver):
        pass

    def after_navigate_back(self, driver):
        pass

    def before_navigate_forward(self, driver):
        pass

    def after_navigate_forward(self, driver):
        pass

    def before_find(self, by, value, driver):
        pass

    def after_find(self, by, value, driver):
        pass

    def before_click(self, element, driver):
        pass

    def after_click(self, element, driver):
        pass

    def before_change_value_of(self, element, driver):
        pass

    def after_change_value_of(self, element, driver):
        pass

    def before_execute_script(self, script, driver):
        pass

    def after_execute_script(self, script, driver):
        pass

    def before_close(self, driver):
        pass

    def after_close(self, driver):
        pass

    def before_quit(self, driver):
        pass

    def after_quit(self, driver):
        pass

    def on_exception(self, exception, driver):
        pass
# -*- coding: utf-8 -*-

'''

@author: KaueBonfim
'''

from selenium.webdriver.support.events import EventFiringWebDriver
from pytractor import webdriver as protactor
from selenium import webdriver
from Pyautomators.Error import Driver_erro
from Pyautomators.acoes_no_elemento import Acoes
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
from Pyautomators.Error import Elemento_erro
from Pyautomators.web_extensao import Aguarde_elemento,Js_Script,Simula,Alerta,MyListener
from selenium.webdriver import ActionChains


''' Este arquivo prove os metodos em selenium para web,
    na qual os passamos um elemento chave e seu tipo e ele executa a acao descrita'''


class Web(Acoes,Teclado,Mouse,Valida,Aguarde_elemento,Js_Script,Simula):
    ''' Esta classe tem o intuito de prover conexão com selenium em web'''
    def __init__(self,drive,path_driver=None,Angular=False,options=None,log_name=None):
        '''No construtor temos um parametros sendo um obrigatorio
        driver(obrigatorio):Qual dos drivers a serem usados
        path_driver:Local Aonde esta o Driver web usado
        options:as configurações passadas pelo options do driver
        Angular:Vai ser caso o site for feito inteiramente em angular
        '''
        class _Instancia_driver():
            def get_driver(self,drive,path_driver,options):
                if(type(drive)==str):
                    driver=drive
                    self.drive=drive
                else:
                    driver=drive.valor
                    self.drive=drive.valor
                  
                if(driver == 'Chrome'):
                    if(path_driver==None):
                        path_driver="chromedriver"
                    self.__driver=webdriver.Chrome(executable_path=path_driver,chrome_options=options)    
                    
                elif(driver == 'Firefox'):  
                    if(path_driver==None):
                        path_driver="geckodriver"          
                    self.__driver=webdriver.Firefox(executable_path=path_driver,firefox_options=options)
                    
                    
                elif(driver == 'Ie'):    
                    if(path_driver==None):
                        path_driver="IEDriverServer.exe"          
                    self.driver=webdriver.Ie(executable_path=path_driver,ie_options=options)
                elif(driver == 'Edge'):    
                    if(path_driver==None):
                        path_driver="MicrosoftWebDriver.exe"          
                    self.__driver=webdriver.Edge(executable_path=path_driver)
                else:
                    Erro="""
                        Não é um driver de servidor valido!
                        Digite um driver valido:
                        
                        Ie
                        Firefox
                        Chrome    
                        Edge 
                            """
                    raise Driver_erro(Erro) 
                
                return self.__driver
        
        class _Instancia_driver_Angular():
            def get_driver(self,drive,path_driver,options):
                if(type(drive)==str):
                    driver=drive
                    self.drive=drive
                else:
                    driver=drive.valor
                    self.drive=drive.valor
                
                if(driver == 'Chrome'):
                    if(path_driver==None):
                        path_driver="chromedriver"
                    self.__driver=protactor.Chrome(executable_path=path_driver,chrome_options=options)
                    
                        
                elif(driver == 'Firefox'):  
                    if(path_driver==None):
                        path_driver="geckodriver"          
                    self.__driver=protactor.Firefox(str(path_driver),firefox_options=options)
                    
                    
                elif(driver == 'Ie'):    
                    if(path_driver==None):
                        path_driver="IEDriverServer.exe"          
                    self.__driver=protactor.Ie(str(path_driver),ie_options=options)
                else:
                    Erro="""
                        Não é um driver de servidor valido!
                        Digite um driver valido:
                        
                        Ie
                        Firefox
                        Chrome    
                            
                            """
                    raise Driver_erro(Erro)
        self.drive=drive
        if(Angular==False):
            self.drivin=_Instancia_driver().get_driver(drive,path_driver,options)
            if(log_name != None):
                self.driver=EventFiringWebDriver(self.drivin,MyListener(log_name))
            else:
                self.driver=self.drivin
            self.angular=Angular
        else:
            
            self.driver=_Instancia_driver_Angular().get_driver(drive,path_driver,options)
           
            self.angular=Angular
        self.alert=Alerta(self.driver)
        self.ActionChains=ActionChains(self.driver)
        
                
       
        
    def print_janela(self,path_imagem):
        '''Este metodo tira um print do conteudo atual da janela sendo usada
        
            parametros:
            path_imagem(obrigatorio):nome a imagem mais o caminho dela caso seja em outro diretorio
           Exemplo:
        print_janela('c:/teste.png')
        print_janela('teste.png')'''
        
        self.driver.get_screenshot_as_file(path_imagem)
        
        
    def fechar_programa(self):
        '''Este metodo fecha o driver web
        Exemplo:
        fechar_programa()''' 
        self.driver.quit()  
          
    def get_url(self):
        '''Este metodo retorna a Url atual
           Exemplo:
        get_url()''' 
        return self.driver.current_url
        
    def pagina(self,url):
        '''Este metodo vai a pagina passada para a url
           Exemplo:
        pagina('http://google.com.br')''' 
        self.driver.get(url)
        
    def maximiza(self):
        '''Este metodo maximiza a janela do driver utilizado
           Exemplo:
        maximiza()''' 
        self.driver.maximize_window()
    
    
    def preencher_tela(self):
        '''Este metodo preenche a tela inteira com a pagina
           Exemplo:
        preencher_tela()'''
        self.driver.fullscreen_window()
            
    def atualizar(self):
        '''Este metodo atualiza a pagina atual
           Exemplo:
        atualizar()'''
        self.driver.refresh()
        
    def voltar(self):
        '''Este metodo retorna a pagina anterior
           Exemplo:
        voltar()'''
        self.driver.back()
    
    def frente(self):
        '''Este metodo segue para a proxima pagina em sequencia
           Exemplo:
        frente()'''
        self.driver.forward()
    
    def limpar(self):
        '''Este metodo limpa o campo de um input de texto
           Exemplo:
        limpar()'''
        self.driver.clear()
        
    def get_titulo(self):
        '''Este metodo retorna o titulo atual da pagina
           Exemplo:
        get_titulo()'''
        return self.driver.title
    
    def get_html(self):
        return self.driver.page_source
    
    def get_navegador(self):
        '''Este metodo retorna o navegador que esta sendo usado no driver
           Exemplo:
        get_navegador()'''
        return self.driver.name
    
    def elemento(self,elemento,tipo,implicit=0):
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
        
        id:    Web    <form id="loginForm"> = 'loginForm'
        
        name:    Web    <input name="username" type="text" /> = 'username'
        
        class:    Web     <p class="content">Site content goes here.</p> = 'content'
        
        xpath:    Web <html>                    =    '/html/body/form[1]' ou '//form[1]' ou '//form[@id='loginForm']'
                                     <body>
                                      <form id="loginForm">
                                      
        link:    Web        <a href="continue.html">Continue</a> = 'Continue'
        
        tag:    Web    <h1>Welcome</h1> = 'h1'
        
        css:    Web    <p class="content">Site content goes here.</p> = 'p.content'
        
        partial_link:    Web    <a href="continue.html">Continue</a> = 'Conti'
        
        android:    Mobile 
        
        ios:    Mobile
        
        binding:    Web(Angular) <span>{{person.name}}</span> = 'person.name' ou <span ng-bind="person.email"></span> = 'person.email'
        
        model:    Web(Angular) <input type="text" ng-model="person.name"/> = 'person.name'       
        '''    
        self.driver.implicitly_wait(implicit)
        if(tipo == 'id'):
            element=self.driver.find_element_by_id(elemento)
        elif(tipo == 'name'):
            element=self.driver.find_element_by_name(elemento) 
        elif(tipo == 'class'):            
            element=self.driver.find_element_by_class_name(elemento) 
        elif(tipo == 'xpath'):            
            element=self.driver.find_element_by_xpath(elemento) 
        elif(tipo == 'link'):            
            element=self.driver.find_element_by_link_text(elemento) 
        elif(tipo == 'tag'):            
            element=self.driver.find_element_by_tag_name(elemento) 
        elif(tipo == 'css'):            
            element=self.driver.find_element_by_css_selector(elemento) 
        elif(tipo == 'partial_link'):            
            element=self.driver.find_element_by_partial_link_text(elemento) 
        elif(self.angular==False):
            if(tipo=='binding'):
                element=self.driver.find_element_by_binding(elemento)
            elif(tipo=='model'):
                element=self.driver.find_element_by_model(elemento)
            elif(tipo=='accessibility_id'):
                element=self.driver.find_element_by_accessibility_id(elemento)
            else:
                Erro="""
                    Escolha um valor de elemento Valido
                    lista de elementos:
                    id:    Web
                    name:    Web
                    class:    Web
                    xpath:    Web
                    link:    Web
                    tag:    Web
                    css:    Web
                    partial_link:    Web
                    binding:    Web(Angular)
                    model:    Web(Angular)
                    
                    """
                raise Elemento_erro(Erro)
        else:
            Erro="""
                Escolha um valor de elemento Valido
                lista de elementos:
                id:    Web
                name:    Web
                class:    Web
                xpath:    Web
                link:    Web
                tag:    Web
                css:    Web
                partial_link:    Web
                andorid:    Mobile
                ios:    Mobile
                binding:    Web(Angular)
                model:    Web(Angular)
                
                """
            raise Elemento_erro(Erro)
        return element
      
    def elemento_list(self,elemento,tipo,indice_lista,implicit=0):
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
        
        id:    Web    <form id="loginForm"> = 'loginForm'
        
        name:    Web    <input name="username" type="text" /> = 'username'
        
        class:    Web     <p class="content">Site content goes here.</p> = 'content'
        
        xpath:    Web <html>                    =    '/html/body/form[1]' ou '//form[1]' ou '//form[@id='loginForm']'
                                     <body>
                                      <form id="loginForm">
                                      
        link:    Web        <a href="continue.html">Continue</a> = 'Continue'
        
        tag:    Web    <h1>Welcome</h1> = 'h1'
        
        css:    Web    <p class="content">Site content goes here.</p> = 'p.content'
        
        partial_link:    Web    <a href="continue.html">Continue</a> = 'Conti'
       
        
        binding:    Web(Angular) <span>{{person.name}}</span> = 'person.name' ou <span ng-bind="person.email"></span> = 'person.email'
        
        model:    Web(Angular) <input type="text" ng-model="person.name"/> = 'person.name'
         
        '''
        self.driver.implicitly_wait(implicit)
        elements=self.elementos_list(elemento, tipo, implicit)
        element=elements[indice_lista]
        return element
    
    def elementos_list(self,elemento,tipo,implicit=0):
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
        
        id:    Web    <form id="loginForm"> = 'loginForm'
        
        name:    Web    <input name="username" type="text" /> = 'username'
        
        class:    Web     <p class="content">Site content goes here.</p> = 'content'
        
        xpath:    Web <html>                    =    '/html/body/form[1]' ou '//form[1]' ou '//form[@id='loginForm']'
                                     <body>
                                      <form id="loginForm">
                                      
        link:    Web        <a href="continue.html">Continue</a> = 'Continue'
        
        tag:    Web    <h1>Welcome</h1> = 'h1'
        
        css:    Web    <p class="content">Site content goes here.</p> = 'p.content'
        
        partial_link:    Web    <a href="continue.html">Continue</a> = 'Conti'
        
        binding:    Web(Angular) <span>{{person.name}}</span> = 'person.name' ou <span ng-bind="person.email"></span> = 'person.email'
        
        model:    Web(Angular) <input type="text" ng-model="person.name"/> = 'person.name'
         
        '''
        self.driver.implicitly_wait(implicit)
        if(tipo == 'id'):           
            elements=self.driver.find_elements_by_id(elemento)  
        elif(tipo == 'name'):
            elements=self.driver.find_elements_by_name(elemento)
        elif(tipo == 'class'):            
            elements=self.driver.find_elements_by_class_name(elemento)
        elif(tipo == 'xpath'):            
            elements=self.driver.find_elements_by_xpath(elemento)
        elif(tipo == 'link'):            
            elements=self.driver.find_elements_by_link_text(elemento)
        elif(tipo == 'tag'):            
            elements=self.driver.find_elements_by_tag_name(elemento)
        elif(tipo == 'text'):            
            elements=self.driver.find_elements_by_partial_link_text(elemento)
        elif(tipo == 'css'):            
            elements=self.driver.find_elements_by_css_selector(elemento)
        elif(self.angular==False):
            if(tipo=='binding'):
                elements=self.driver.find_elements_by_binding(elemento)
            elif(tipo=='model'):
                elements=self.driver.find_elements_by_model(elemento)
            elif(tipo=='accessibility_id'):
                elements=self.driver.find_elements_by_accessibility_id(elemento)
            else:
                Erro="""
                    Escolha um valor de elemento Valido
                    lista de elementos:
                    id:    Web
                    name:    Web
                    class:    Web
                    xpath:    Web
                    link:    Web
                    tag:    Web
                    css:    Web
                    partial_link:    Web
                    binding:    Web(Angular)
                    model:    Web(Angular)
                    
                    """
                raise Elemento_erro(Erro)
        else:
            Erro="""
                Escolha um valor de elemento Valido
                lista de elementos:
                id:    Web
                name:    Web
                class:    Web
                xpath:    Web
                link:    Web
                tag:    Web
                css:    Web
                partial_link:    Web
                """
            raise Elemento_erro(Erro)
        return elements
    
    def elemento_por_texto(self,elemento_base,tipo,texto_referencia):
        '''Este metodo retorna em um elemento, baseado no texto referencia 
        na qual temos 3 parametros
        
        elemento_base(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        texto_referencia(obrigatorio): escolhe qual elemento da lista, baseado no texto
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        
        
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <a href='http://algumacoisa.com.br'>texto valor</a>
                
                 elemento_por_texto("gsfi","class",'texto valor')
        '''
        elemento=None
        elements=self.elementos_list(elemento_base, tipo)
        for element in elements:
            if(element.text==texto_referencia):
                elemento=element
        return elemento
    
    
    def elemento_por_atributo(self,elemento_base,tipo,atributo_referencia,valor):
        '''Este metodo retorna em um elemento, baseado no atributto referencia 
        na qual temos 3 parametros
        
        elemento_base(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        texto_referencia(obrigatorio): escolhe qual elemento da lista, baseado no texto
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        
        
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <a href='http://algumacoisa.com.br'>texto valor</a>
                
                 elemento_por_texto("gsfi","class",'texto valor')
        '''
        elemento=None
        elements=self.elementos_list(elemento_base, tipo)
        for element in elements:
            if(element.get_attribute(atributo_referencia)==valor):
                elemento=element
        return elemento
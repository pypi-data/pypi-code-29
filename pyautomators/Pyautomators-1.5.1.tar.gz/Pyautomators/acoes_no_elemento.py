# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''

import time


class Acoes():
    ''' Esta classe tem o intuito de promover acoes que são comuns em testes baseados em Selenium,
    na qual os passamos um elemento chave e seu tipo e ele executa a acao descrita'''
    
     
    def escreve(self,elemento,conteudo,tipo,implicit=0,tempo=None):
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
        if(tempo is not None):
            for char in conteudo:
                element.send_keys(char) 
                time.sleep(tempo)
        else:
            element.send_keys(conteudo)
            
        return element
        
    def escreve_por_texto(self,elemento_base,tipo,conteudo,texto_referencia):
        '''Este metodo escreve em um elemento, na qual temos cinco parametros
        
        elemento_base(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        texto_referencia(obrigatorio): escolhe qual elemento da lista, baseado no texto
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        conteudo(obrigatorio): Conteudo na qual queremos inserir naquele elemento
        
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <a href='http://algumacoisa.com.br'>texto valor</a>
                
                 escreve_por_texto("gsfi","class",'Valor','texto valor')
        '''
       
        elemento=self.elemento_por_texto(elemento_base, tipo, texto_referencia)    
        elemento.send_keys(conteudo)
        return elemento
    
    def clica_por_text(self,elemento_base,tipo,texto_referencia):
        '''Este metodo escreve em um elemento, na qual temos cinco parametros
        
        elemento_base(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu elemento pela descricao.
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        texto_referencia(obrigatorio): escolhe qual elemento da lista, baseado no texto

        
        Exemplos:
        
            dado um trecho de HTML:
            
                <a href='http://algumacoisa.com.br'>texto valor</a>
                
                 clica_por_text("gsfi","class",'texto valor')
        '''
        elemento=self.elemento_por_texto(elemento_base, tipo, texto_referencia)
        elemento.click()
        return elemento
           
    def clica(self,elemento,tipo,implicit=0):
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
             
    
    def pegar_texto(self,elemento,tipo,implicit=0):
        '''Este metodo retorna o texto de um elemento, na qual temos tres parametros
        
        retornara o texto que estiver no elemento
        
        elemento(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        Exemplos:
        
            dado um trecho de HTML:
            
                <input class="gsfi" id="lst-ib" maxlength="2048" name="q" autocomplete="off" title="Pesquisar" >Textooo</input>
                
                valor=pegar_textto("lst-ib","id",10)
                print(valor)
                >>>Textooo
        '''
        element=self.elemento(elemento,tipo,implicit) 
        return element.text,element
                
    def escrever_elemento_lista(self,elemento,conteudo,tipo,indice_lista:int,implicit=0,tempo:int=None):
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
        element=self.elemento_list(elemento,tipo,indice_lista,implicit)
        if(tempo is not None):
            for char in conteudo:
                element.send_keys(char) 
                time.sleep(tempo)
        else:
            element.send_keys(conteudo)
        return element      
            
    def clica_elemento_lista(self,elemento,tipo,indice_lista:int,implicit=0):
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
        element=self.elemento_list(elemento,tipo,indice_lista,implicit)
        element.click()
        return element 
    
    def pegar_texto_list(self,elemento,tipo,indice_lista:int,implicit=0):
        '''Este metodo retorna o texto de um elemento de uma lista de elementos com o mesmo tipo e elemento. na qual temos quatro parametros
        
        retornara o texto que estiver no elemento
        
        elemento(obrigatorio): Qual é o elemento que iremos buscar para realizar a escrita, necessariamente oque invididualiza seu ekemento pela descricao.
        indice_lista(obrigatorio): Qual dos itens que achamos queremos usar, este sempre retorna uma lista na ordem que foi achado
        tipo(obrigatorio): O tipo para do elemento que iremos usar(id ,class, name, xpath ...)
        implicit: É o tempo que devemos esoerar o elemento aparecer, caso não apareça e gerado um erro
        
        Exemplos:
        
            dado um trecho de HTML:
            
                <input name="btn" type="submit" jsaction="sf.lck">
                <input name="btn" type="submit" jsaction="sf.chk">
                
                pegar_texto_list("input","tag",1,10)
        '''
        element=self.elementos_list(elemento,tipo,indice_lista,implicit)
        return element.text
    
    
                    
    def clica_elemento_atributo(self,elemento_base,tipo,atributo_referencia,valor):
        self.elemento_por_atributo(elemento_base, tipo, atributo_referencia, valor).click()
        
# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''
import pyautogui
from time import sleep
from .Error import Valida_erro
''' Este modulo trabalha com o conjunto de validações,
    pode conter valor valores e imagens para ser verificadas'''

class Valida():
    ''' Esta classe tem o intuito de gerar um conjunto de validações que auxiliem testes'''
    
    @staticmethod
    def verifica_tela(imagem,tentativa=1,tempo=0.1,valida=False,acao=None,valor:tuple=None):
        '''Verifica em tela se uma imagem esta , caso não estiver ela pode gerar um erro ou fazer alguma ação
            e retorna o valor das coordenadas para uso
        parametros:
        imagem(obrigatorio):Verifica se a imagem esta visivel
        tentativa:fala quantos ciclos de tentativa ele tentara achar a foto
        tempo:intervalo entre um ciclo e outro
        valida:se True, caso o ciclo passe e a imagem não for achada, levanta um erro
        acao: acao que sera feita durante o ciclo, sendo passada um valor de um metodo para o argumento
        valor:caso a açao tenha valores passados por parametros, colocar os parametros dentro de uma tupla
        Exemplo:
        verifica_tela("Capturar.PNG", 3, 2, acao=Teclado.digitos,valor=("tab","tab"))
        verifica_tela("Capturar.PNG", 3, 2, true,Teclado.clica,(120,1200))
        '''
        validador=False
        for ponto in range(tentativa):
            
            result=pyautogui.locateOnScreen(imagem)
            if(result  is not None):
                validador=True
                break
                        
            if(acao is not None):
                if(valor is not None):
                    acao(*valor)
                
                elif(valor is None):
                    acao()
                    
            sleep(tempo)
        if(valida):
            if(validador):
                pass
            else:
                Erro='\n\n\tImagem não foi encontrada!!'
                raise Valida_erro(Erro)
        return result
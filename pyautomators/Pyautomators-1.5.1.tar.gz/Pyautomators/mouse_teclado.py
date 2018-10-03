# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''
'''

Este Modulo Trabalha ações do mouse e teclado

'''
import pyautogui
class Teclado():
    ''' Esta classe tem o intuito de prover ações do Teclado'''
    
    ##################################################################################
    #                                  TECLAS                                        #
    ##################################################################################
    r"""'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
     ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
     '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
     'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
     'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
     'browserback', 'browserfavorites', 'browserforward', 'browserhome',
     'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
     'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
     'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
     'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
     'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
     'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
     'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
     'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
     'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
     'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
     'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
     'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
     'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
     'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
     'command', 'option', 'optionleft', 'optionright'"""
    @staticmethod
    def digitos(*digito):
        r'''Este metodo trabalha com digitos do caracter e a repetição dos digitos atribuidos em uma tupla
        
        Exemplo:
        
        digitos("b","o",("m",10),'tab','d','i','a')
        >>>bommmmmmmmmm    dia
        
        '''
        lista=[]
        if(type(digito)==tuple):
            for d in digito:
                if(type(d)==tuple):
                    for b in range(d[1]):
                        lista.append(d[0])
                else:
                    lista.append(d)
        pyautogui.press(lista,interval=0.5)
        
    @staticmethod
    def mantenha_e_digite(mantenha,digite):        
        r'''Este metodo mantem uma tecla pressionada enquanto digita uma lista de digitos
        
        Exemplo:
        
        mantenha_e_digite('capslock',['a','b','c'])
        >>>ABC
        
        '''
        pyautogui.keyDown(mantenha)
        for digito in digite:
            pyautogui.press(digito)
        pyautogui.keyUp(mantenha)
        
    @staticmethod
    def combo_digitos(*teclas):
        r'''Este metodo falta digita diversas teclas ao mesmo tempo de acordo com a ordem
        
        Exemplo:
        
        combo_digitos('alt',"f4")
        
        
        '''
        pyautogui.hotkey(*teclas)
        
    @staticmethod    
    def escrever_direto(conteudo):
        r'''Este metodo escreve um texto com base no alfabeto
        
        Exemplo:
        
        escrever_direto('Bom dia pessoal')
        >>>Bom dia pessoal
        
        '''
        pyautogui.typewrite(conteudo)
        
class Mouse():
    ''' Esta classe tem o intuito de prover ações do Mouse'''
    
    
    
    
    @staticmethod
    def clica_coordenada(x,y,cliques=1,botao='left'):
        r'''Este metodo clica em uma coordenada passada na tela
        
        Exemplo:
        
        clica_coordenada(216,114)
        clica_coordenada(216,114,1,'rigth')
        clica_coordenada(localizacao_imagem("teste.png",True),2)
        '''
        pyautogui.click(x,y,clicks=cliques,button=botao)
    
    @staticmethod
    def arraste_coordenada(xi,yi,xf,yf,botao="left",duracao=0.0):
        r'''Este metodo arrasta algo de uma coordenada inicial para a final
         
        
        Exemplo:
        
        arraste_coordenada(216,114,1000,800)
        arraste_coordenada(216,114,1000,800,duracao=1.5)
        arraste_coordenada(localizacao_imagem("teste.png",True),localizacao_imagem("teste2.png",True))
        '''
        pyautogui.moveTo(x=xi,y=yi,duration=duracao)
        pyautogui.dragTo(x=xf,y=yf,button=botao,duration=duracao)
    
    @staticmethod
    def rolagemMouse(valor,x=None,y=None):
        r'''Este metodo arrasta algo de uma coordenada inicial para a final
         
        
        Exemplo:
        
        rolagemMouse(100)
        '''
        pyautogui.moveTo(x, y)
        pyautogui.scroll(valor)
        
    @staticmethod
    def clica_imagem(path_imagem,clicks=1,botao='left'):
        r'''Este metodo arrasta algo de uma coordenada inicial para a final
         
        
        Exemplo:
        
        clica_imagem("teste.png",2)
        clica_imagem("teste.png")
        '''
        x,y=pyautogui.locateCenterOnScreen(path_imagem)
        pyautogui.click(x,y,clicks=clicks,button=botao)
    
    @staticmethod    
    def moverMouse(x,y,duracao=0.0):
        r'''Este metodo arrasta algo de uma coordenada inicial para a final
         
        
        Exemplo:
        
        arraste_coordenada(216,114)
        arraste_coordenada(216,114,1.5)
        arraste_coordenada(localizacao_imagem("teste.png",True))
        '''
        pyautogui.moveTo(x,y,duration=duracao)    
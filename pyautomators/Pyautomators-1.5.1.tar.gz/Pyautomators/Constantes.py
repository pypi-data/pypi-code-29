'''
Created on 24 de ago de 2018

@author: koliveirab
'''
from selenium.webdriver.common.keys import Keys

class Tipos_de_navegadores():
    CHROME='Chrome'
    FIREFOX='Firefox'
    IE='Ie'
    EDGE='Edge'
    
class Condicoes_de_aguarde():
    VISIVEL="visivel"
    
class Tipos_de_elemento():
  
    ID='id'
    CLASS_NAME='class'
    XPATH='xpath'
    NAME='name'
    TAG_NAME='tag'
    PARTIAL_LINK='partial_link'
    LINK_TEXT='link'
    CSS_SELECTOR='css'
    
  
class Teclas_para_driver(Keys):
    pass
    
class Teclas_para_mouse():
    EXCLAMACAO, ASPAS_DUPLAS, JOGO_DA_VELHA, CIFRAO, PORCENTAGEM, E_COMERCIAL, ASPAS_SIMPLES, ABERTURA_PARENTESES,\
    FECHAMENTO_PARENTESES, ASTERISCO, SOMA, VIRGULA, TRACO, PONTO, BARRA, NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7,\
    NUM_8, NUM_9, DOIS_PONTOS, PONTO_VIRGULA, SINAL_MENOR_QUE, IGUAL, SINAL_MAIOR_QUE, INTERROGACAO, ARROBA, ABERTURA_COLCHETE, BARRA_INTERTIDA, FECHAMENTO_COLCHETE, ACENTO_CIRCUNFLEXO, UNDERLINE, ACENTO_AGUDO,\
    A, B, C, D, E,F, G, H, I, J, K, L, M, N, O,\
    P, Q, R, S, T, U, V, W, X, Y, Z, ABERTURA_CHAVE, PIPE,FECHAMENTO_CHAVE, TI,\
    ACCEPT, ADD, ALT, ALTLEFT, ALTRIGHT, APPS, BACKSPACE,\
    BROWSERBACK, BROWSERFAVORITES, BROWSERFORWARD, BROWSERHOME,\
    BROWSERREFRESH, BROWSERSEARCH, BROWSERSTOP, CAPSLOCK, CLEAR,\
    CONVERT, CTRL, CTRLLEFT, CTRLRIGHT, DECIMAL, DEL, DELETE,\
    DIVIDE, DOWN, END, ENTER, ESC, ESCAPE, EXECUTE, F1, F10,\
    F11, F12, F13, F14, F15, F16, F17, F18, F19, F2, F20,\
    F21, F22, F23, F24, F3, F4, F5, F6, F7, F8, F9,\
    FINAL, FN, HANGUEL, HANGUL, HANJA, HELP, HOME, INSERT, JUNJA,\
    KANA, KANJI, LAUNCHAPP1, LAUNCHAPP2, LAUNCHMAIL,\
    LAUNCHMEDIASELECT, LEFT, MODECHANGE, MULTIPLY, NEXTTRACK,\
    NONCONVERT, NUMLOCK, PAGEDOWN, PAGEUP, PAUSE, PGDN,\
    PGUP, PLAYPAUSE, PREVTRACK, PRINT, PRINTSCREEN, PRNTSCRN,\
    PRTSC, PRTSCR, RETURN, RIGHT, SCROLLLOCK, SELECT, SEPARATOR,\
    SHIFT, SHIFTLEFT, SHIFTRIGHT, SLEEP, SPACE, STOP, SUBTRACT, TAB,\
    UP, VOLUMEDOWN, VOLUMEMUTE, VOLUMEUP, WIN, WINLEFT, WINRIGHT, YEN,\
    COMMAND, OPTION, OPTIONLEFT, OPTIONRIGTH=\
    '!', '"', '#', '$', '%', '&', "'", '(',\
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',\
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',\
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',\
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',\
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',\
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',\
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',\
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',\
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',\
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',\
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',\
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',\
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',\
    'nonconvert','numlock', 'pagedown', 'pageup', 'pause', 'pgdn',\
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',\
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',\
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',\
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',\
    'command', 'option', 'optionleft', 'optionright'

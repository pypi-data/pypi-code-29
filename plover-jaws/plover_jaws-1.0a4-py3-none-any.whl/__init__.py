import string
from pythoncom import CoInitialize
from win32com.client import Dispatch
from plover.engine import StenoEngine
class TypedChars:
    def __init__(self,maxCharsToKeep=512):
        self.maxCharsToKeep = maxCharsToKeep
        self.text = ''
        self.unspokenNewText = ''
        self.unspokenRemovedText = ''
        self.haveAddedNewTextSinceRemove = False

    def add(self,text):
        #print('adding {}, {}'.format(self.haveAddedNewTextSinceRemove,text))
        self.ensureUnspokenNewTextContainsBeginningOfWord(text)
        #print('done')
        self.text += text
        self.unspokenNewText += text
        self.unspokenRemovedText = ''
        if len(text.strip()) > 0:
            self.haveAddedNewTextSinceRemove = True
        
    def remove (self,count,shouldSpeak):
        self.haveAddedNewTextSinceRemove = False
        removed = self.text[-count:]
        self.text = self.text[:-count]
        if shouldSpeak:
            # only gather deleted text if there isn't pending inserted text to be spoken.
            # If there's newly added text that hasn't yet been spoken because there's not been a trailing space,
            # assume that this deletion is removing it. If the number of characters being deleted is greater than the pending unspoken new text,
            # Plover  is likely deleting a string in preparation for inserting a capitalized version.
            self.unspokenRemovedText = removed + self.unspokenRemovedText
        self.unspokenNewText = self.unspokenNewText[:-count]
        return removed

    def ensureUnspokenNewTextContainsBeginningOfWord(self, text):
        # When using this module Plover must be set to append spaces to the end of words rather than
        # append them to the beginning. of words.
        # This function andles the situation where a complete word has been inserted and spoken. Then an suffix is typed
        # resulting in backspace being sent followed by the suffix itself and a trailing space.
        # In this situation, the user should hear the complete word. We check for that here and if detected,
# prime unspokenNewText with the  beginning of the word.
        # The above applies if the suffix is alphabetic. If punctuation or digits are being added then only the newly  typed text is spoken.
        if len(text.strip()) == 0: return
        if self.haveAddedNewTextSinceRemove or self.unspokenNewText: return
        if not self.text: return
        if self.text[-1].isspace(): return
        if self.endsWithPunctuationOrDigit():
            return
        if self.isAppendingDigitsOrPunctuation(text): return
        self.unspokenNewText = self.getLastWord()
        #print('setting unspoken to {}'.format(self.unspokenNewText))

    def getAndClearUnspokenNewText(self):
        text = self.unspokenNewText
        self.unspokenNewText = ''
        return text
    
    def getAndClearUnspokenRemovedText(self):
        text = self.unspokenRemovedText
        self.unspokenRemovedText = ''
        return text

    def getLastWord(self):
        start = self.text.rfind(' ',0,-1)
        if start == -1:
            return self.text
        return self.text[start+1:]

    def isOnWordBoundary(self):
        return not self.text or self.text[-1].isspace()
    
    def isAppendingDigitsOrPunctuation(self,text):
        if self.text is None or not self.text:
            return False
        if text[0].isdigit() or (text[0] in string.punctuation):
            return True
        return False
    
    def endsWithPunctuationOrDigit(self):
        if not self.text: return
        if self.text[-1].isdigit() or (self.text[-1] in string.punctuation):
            return True
        return False

    
class PloverJAWS:
    def __init__(self, engine,jawsApi=None):
        super().__init__()
        self.engine = engine
        global classInstance
        classInstance = self
        self.running = False
        self.isDeletingAsPartOfInsertion = False
        CoInitialize()
        self.jaws = jawsApi if jawsApi is not None else Dispatch("freedomsci.jawsapi")
        self.engine.hook_connect('stroked',self.onStroked)
        self.engine.hook_connect('send_string',self.onSendString)
        self.engine.hook_connect('send_backspaces',self.onSendBackspaces)
        #self.engine.hook_connect('send_key_combination',self.onSendKeyCombination)
        self.engine.hook_connect('translated',self.onTranslated)

        self.chars = TypedChars()
        self.lastSpoken = ''
        
    def start(self):
        self.running = True
        
    def stop(self):
        self.running = False

    def onStroked(self,keys):
        #print('stroked {}'.format(keys))
        pass
    def onTranslated(self,old,new):
        self.isDeletingAsPartOfInsertion = len(old) > 0 and len(new) > 0
        print('old {}, new {}'.format(old,new))
        
    def onSendString(self,text):
        self.chars.add(text)
        if self.chars.isOnWordBoundary():
            self.speakNewText()


    def onSendBackspaces(self,count):
        removedText = self.chars.remove(count,not self.isDeletingAsPartOfInsertion)
        if self.chars.isOnWordBoundary() or self.isAllPunctuationAndDigits(removedText):
            self.speakRemovedText()

    def onSendKeyCombination(self,string):
        pass
    
    def speak(self,text,alwaysSpeak=True):
        if alwaysSpeak or self.lastSpoken != text:
            self.jaws.SayString(text,False)
        self.lastSpoken = text
        
    def speakNewText(self):
        text = self.chars.getAndClearUnspokenNewText()
        if text and len(text.strip()) > 0:
            self.speak('{0}'.format(text))
            
    def speakRemovedText(self):
        text = self.chars.getAndClearUnspokenRemovedText()
        if text and len(text.strip()) > 0:
            self.speak('{0}'.format(text))

    @staticmethod
    def isAllPunctuationAndDigits(text):
        if not text: return False
        if len(text.strip()) == 0:
            return False
        for char in text:
            if char.isspace():
                continue
            if not (char.isdigit() or char in string.punctuation):
                return False
        return True

# Commands that can be bound to keys on the keyboard

def runScript(engine,scriptName):
    if classInstance:
        classInstance.jaws.runScript(scriptName)

def runFunction(engine,functionName):
    if classInstance:
        classInstance.jaws.runFunction(functionName)

        
        


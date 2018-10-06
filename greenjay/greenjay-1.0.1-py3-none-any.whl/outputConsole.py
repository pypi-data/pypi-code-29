from datetime import datetime

class OutputConsole(object):    
    def writeToConsole(self, msg, level):
        date = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
        print(f'Date: {date} - Level: {level} - Message: {msg}')

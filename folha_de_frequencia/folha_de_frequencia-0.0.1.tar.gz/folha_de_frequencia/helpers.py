from datetime import timedelta
from datetime import time
from datetime import datetime

def formatar_hora(data):
    return data.strftime('%H:%M')

def converter_hora_em_texto_para_timedelta(hora):
    HORAS, MINUTOS = map(lambda parte: int(parte), hora.split(':'))
    return timedelta(hours=HORAS, minutes=MINUTOS)

def converter_hora_em_texto_para_time(hora):
    HORAS, MINUTOS = map(lambda parte: int(parte), hora.split(':'))
    return time(hour=HORAS, minute=MINUTOS)

def converter_data(texto):
    return datetime.strptime(texto, '%d/%m/%y')


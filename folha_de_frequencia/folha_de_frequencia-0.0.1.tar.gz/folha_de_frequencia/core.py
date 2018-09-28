from datetime import timedelta
from datetime import datetime
from datetime import date
from datetime import time
import random

def agrupar(iteravel, tamanho_do_grupo):
    return zip(*[iter(iteravel)]*tamanho_do_grupo)

class Registro:

    def __init__(self, dia):
        self.marcacoes = []
        self.dia = dia

    def marcar(self, horario):
        self.marcacoes.append(horario)

    @property
    def eh_fim_de_semana(self):
        return self.dia.weekday() > 4

    @property
    def horario_total(self):
        duracao_dos_periodos = map(lambda periodo: periodo[1] - periodo[0], agrupar(self.marcacoes, 2))
        return sum(duracao_dos_periodos, timedelta(hours=0))

class GeradorDePonto:

    def __init__(self, horario_de_chegada_oficial, carga_horaria, minimo_de_almoco, variacao_maxima, tempo_de_almoco, preencher_fim_de_semana):
        self.carga_horaria = carga_horaria
        self.horario_de_chegada_oficial = horario_de_chegada_oficial
        self.minimo_de_almoco = minimo_de_almoco
        self.tempo_de_almoco = tempo_de_almoco
        self.variacao_maxima = variacao_maxima
        self.preencher_fim_de_semana = preencher_fim_de_semana

    def obter_anotacoes_por_periodo(self, inicio, fim):
        if inicio > fim :
            raise Exception("Início e fim do período devem ser consecutivos")

        dia = inicio
        um_dia = timedelta(days=1)
        while dia <= fim:
            data_da_chegada_oficial = date(dia.year, dia.month, dia.day)
            anotacoes_do_dia = self.__obter_anotacoes_do_dia(data_da_chegada_oficial)
            yield anotacoes_do_dia
            dia += um_dia

    def __obter_anotacoes_do_dia(self, data_da_chegada_oficial):
        registro = Registro(data_da_chegada_oficial)
        
        if registro.eh_fim_de_semana and not self.preencher_fim_de_semana:
            return registro

        metade_do_expediente = timedelta(seconds=self.carga_horaria.total_seconds() / 2)
        duracao_do_almoco = self.__obter_duracao_do_almoco()

        chegada_da_manha = self.__obter_chegada(data_da_chegada_oficial)
        registro.marcar(chegada_da_manha)

        saida_da_manha, variacao_de_permanencia_da_manha = self.__obter_saida_da_manha(metade_do_expediente, chegada_da_manha)
        registro.marcar(saida_da_manha)

        chegada_da_tarde = self.__obter_chegada_da_tarde(saida_da_manha, duracao_do_almoco)
        registro.marcar(chegada_da_tarde)

        saida_da_tarde = self.__obter_saida_da_tarde(chegada_da_tarde, variacao_de_permanencia_da_manha, metade_do_expediente)
        registro.marcar(saida_da_tarde)

        return registro

    def __obter_saida_da_tarde(self, ultima_chegada, variacao_de_permanencia, metade_do_expediente):
        return ultima_chegada - variacao_de_permanencia + metade_do_expediente
    
    def __obter_chegada_da_tarde(self, ultima_saida, duracao_do_almoco):
        return ultima_saida + duracao_do_almoco

    def __obter_saida_da_manha(self, metade_do_expediente, ultima_chegada):
        variacao_de_permanencia = self.__obter_variacao_aleatoria_de_tempo()
        permanencia_da_manha = metade_do_expediente + variacao_de_permanencia
        saida_da_manha = ultima_chegada + permanencia_da_manha
        return saida_da_manha, variacao_de_permanencia

    def __obter_chegada(self, dia):
        variacao_da_chegada = self.__obter_variacao_aleatoria_de_tempo()
        horario_de_chegada = datetime.combine(dia, self.horario_de_chegada_oficial) + variacao_da_chegada
        return horario_de_chegada

    def __obter_duracao_do_almoco(self):
        variacao_do_almoco = self.__obter_atraso_aleatorio()
        duracao_do_almoco = timedelta(seconds=random.randint(self.minimo_de_almoco.total_seconds(), self.tempo_de_almoco.total_seconds() + variacao_do_almoco.total_seconds())) 
        return duracao_do_almoco

    def __obter_variacao_aleatoria_de_tempo(self):
        segundos_da_variacao_maxima = self.variacao_maxima.total_seconds()
        return timedelta(seconds=random.randint(0, segundos_da_variacao_maxima)) * random.choice([-1, 1])

    def __obter_atraso_aleatorio(self):
        segundos_da_variacao_maxima = self.variacao_maxima.total_seconds()
        return timedelta(seconds=random.randint(0, segundos_da_variacao_maxima))
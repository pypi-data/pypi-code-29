import unittest
from core import GeradorDePonto
from core import Registro
from datetime import time
from datetime import datetime
from datetime import timedelta

class TestesDoRegistro(unittest.TestCase):
    dia = datetime(2018, 4, 26, 7, 30).date()
    
    def test_registro_deve_ser_criado_sem_nenhuma_marcacao_de_horario(self):
        marcacoes = Registro(self.dia).marcacoes

        assert marcacoes == []

    def test_registro_deve_adicionar_uma_marcacao_de_horario(self):
        horario = datetime(2018, 4, 26, 7, 30)
        registro = Registro(horario.date())

        registro.marcar(horario)

        assert registro.marcacoes == [horario]

    def test_registro_deve_calcular_o_total_de_tempo_das_marcacoes(self):
        chegada = datetime(2018, 4, 26, 7, 30)
        saida = datetime(2018, 4, 26, 11, 30)        
        registro = Registro(chegada.date())
        registro.marcar(chegada)
        registro.marcar(saida)

        total = registro.horario_total

        assert total == (saida - chegada)

    def test_registro_deve_calcular_o_total_de_tempo_das_marcacoes_com_2_periodos(self):
        chegada = datetime(2018, 4, 26, 7, 30)
        saida = datetime(2018, 4, 26, 11, 30)
        chegada1 = datetime(2018, 4, 26, 12, 30)
        saida1 = datetime(2018, 4, 26, 17, 30)
        registro = Registro(chegada.date())
        registro.marcar(chegada)
        registro.marcar(saida)
        registro.marcar(chegada1)
        registro.marcar(saida1)

        total = registro.horario_total

        assert total == (saida - chegada + saida1 - chegada1)

    def test_deve_verificar_se_um_registro_eh_de_fim_de_semana(self):
        um_sabado = Registro(datetime(2018, 4, 28))
        um_domingo = Registro(datetime(2018, 4, 29))
        uma_segunda = Registro(datetime(2018, 4, 30))

        assert um_sabado.eh_fim_de_semana == True
        assert um_domingo.eh_fim_de_semana == True
        assert uma_segunda.eh_fim_de_semana == False


class TestesDoGerador(unittest.TestCase):
    horario_de_chegada_oficial = time(hour=7, minute=30)
    carga_horaria = timedelta(hours=8)
    minimo_de_minutos_de_almoco = timedelta(hours=1)
    minutos_de_almoco = timedelta(hours=2)
    variacao_maxima = timedelta(minutes=30)
    inicio_do_periodo = datetime(2018, 4, 1)
    fim_do_periodo = datetime(2018, 4, 30)
    eh_fim_de_semana = lambda self, registro: registro.dia.weekday() > 4
    tem_registros = lambda self, registro: any(registro.marcacoes)
    preencher_fim_de_semana = False
    
    def test_nao_deve_gerar_registros_pro_fim_de_semana_quando_setado(self):
        preencher_pro_fds = False
        gerador = GeradorDePonto(self.horario_de_chegada_oficial, self.carga_horaria, self.minimo_de_minutos_de_almoco, self.variacao_maxima, self.minutos_de_almoco, preencher_pro_fds)
        esta_sem_registros = lambda registro: not any(registro.marcacoes)

        registros = gerador.obter_anotacoes_por_periodo(self.inicio_do_periodo, self.fim_do_periodo)
        
        registros_de_fds = filter(self.eh_fim_de_semana, registros)
        assert all(map(esta_sem_registros, registros_de_fds)) 

    def test_deve_gerar_registros_pro_fim_de_semana_quando_setado(self):
        preencher_pro_fds = True        
        gerador = GeradorDePonto(self.horario_de_chegada_oficial, self.carga_horaria, self.minimo_de_minutos_de_almoco, self.variacao_maxima, self.minutos_de_almoco, preencher_pro_fds)

        registros = gerador.obter_anotacoes_por_periodo(self.inicio_do_periodo, self.fim_do_periodo)
        
        assert all(map(self.tem_registros, filter(self.eh_fim_de_semana, registros)))

    def test_deve_gerar_todos_os_dias_dentro_do_periodo(self):
        inicio = datetime(2018, 4, 1)
        fim = datetime(2018, 4, 30)
        gerador = GeradorDePonto(self.horario_de_chegada_oficial, self.carga_horaria, self.minimo_de_minutos_de_almoco, self.variacao_maxima, self.minutos_de_almoco, self.preencher_fim_de_semana)
        esta_dentro_do_periodo = lambda registro: registro.dia >= inicio.date() and registro.dia <= fim.date()

        registros = gerador.obter_anotacoes_por_periodo(inicio, fim)

        assert all(map(esta_dentro_do_periodo, registros))

    def test_todos_os_registros_nao_ultrapassam_a_carga_horaria(self):
        carga_horaria = timedelta(hours=8)
        calcular_duracao_do_expediente = lambda registro: registro.horario_total
        gerador = GeradorDePonto(self.horario_de_chegada_oficial, carga_horaria, self.minimo_de_minutos_de_almoco, self.variacao_maxima, self.minutos_de_almoco, self.preencher_fim_de_semana)

        registros = gerador.obter_anotacoes_por_periodo(self.inicio_do_periodo, self.fim_do_periodo)

        dias_trabalhados = filter(self.tem_registros, registros)
        assert all(map(lambda registro: calcular_duracao_do_expediente(registro) == carga_horaria, dias_trabalhados))

    def test_todos_os_registros_estao_dentro_da_variacao_maxima(self):
        variacao_maxima = timedelta(minutes=30)
        horario_de_chegada_oficial = time(hour=7, minute=30)
        gerador = GeradorDePonto(horario_de_chegada_oficial, self.carga_horaria, self.minimo_de_minutos_de_almoco, variacao_maxima, self.minutos_de_almoco, self.preencher_fim_de_semana)
        
        registros = gerador.obter_anotacoes_por_periodo(self.inicio_do_periodo, self.fim_do_periodo)

        dias_trabalhados = filter(self.tem_registros, registros)
        assert all(map(lambda registro: self.esta_dentro_da_variacao(registro.dia, horario_de_chegada_oficial, registro.marcacoes[0], variacao_maxima), dias_trabalhados))

    def test_todos_os_registros_respeitam_o_minimo_de_almoco(self):
        tempo_de_almoco = timedelta(hours=1)
        gerador = GeradorDePonto(self.horario_de_chegada_oficial, self.carga_horaria, self.minimo_de_minutos_de_almoco, self.variacao_maxima, tempo_de_almoco, self.preencher_fim_de_semana)
        
        registros = gerador.obter_anotacoes_por_periodo(self.inicio_do_periodo, self.fim_do_periodo)

        dias_trabalhados = filter(self.tem_registros, registros)
        assert all(map(lambda registro: self.calcular_tempo_de_almoco(registro) >= tempo_de_almoco, dias_trabalhados))

    def test_inicio_e_fim_devem_ser_consecutivos(self):
        inicio = datetime.now()
        fim = inicio - timedelta(days=2)
        gerador = GeradorDePonto(self.horario_de_chegada_oficial, self.carga_horaria, self.minimo_de_minutos_de_almoco, self.variacao_maxima, self.minutos_de_almoco, self.preencher_fim_de_semana)

        with self.assertRaisesRegex(Exception, "Início e fim do período devem ser consecutivos"):
            list(gerador.obter_anotacoes_por_periodo(inicio, fim))

    @staticmethod
    def esta_dentro_da_variacao(dia, horario_oficial_de_chegada, horario_com_variacao, variacao):
        horario_original = datetime(dia.year, dia.month, dia.day, horario_oficial_de_chegada.hour, horario_oficial_de_chegada.minute)
        variacao_realizada = horario_com_variacao - horario_original
        return abs(variacao_realizada.total_seconds()) <= variacao.total_seconds()

    @staticmethod
    def calcular_tempo_de_almoco(registro):
        return registro.marcacoes[-1] - registro.marcacoes[0] - registro.horario_total

if __name__ == "__main__":
    unittest.main()
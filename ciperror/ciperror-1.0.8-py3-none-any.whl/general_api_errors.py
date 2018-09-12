from ciperror import BaseCipError


class OrchestratorOfflineError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE001",
            message="orquestrador offline: {}".format(message),
            friendly_message="O orquestrador encontra-se indisponível.",
            http_status=500)


class KpiOfflineError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE002",
            message="JobData offline: {}".format(message),
            friendly_message="o JobData encontra-se indisponível.",
            http_status=500)


class MonitoringStatusOfflineError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE003",
            message="MonitoringStatus offline: {}".format(message),
            friendly_message="o MonitoringStatus encontra-se indisponível.",
            http_status=500)


class JobDataOfflineError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE004",
            message="Kpi offline: {}".format(message),
            friendly_message="o Kpi encontra-se indisponível.",
            http_status=500)


class Ingest4KIngestProcessError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE005",
            message='Erro no processo de ingest: {}'.format(message),
            friendly_message="Erro no processo de ingest.",
            http_status=500)


class KpiApiResponseError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE006",
            message="Erro ao consumir a API do KPI: {}".format(message),
            friendly_message="Erro ao consumir a API do KPI.",
            http_status=500)


class JobDataApiRequestError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE007",
            message="Erro no request para a Job Data API: {}".format(message),
            friendly_message="Erro no request para a Job Data API.",
            http_status=500)


class JobDataApiAddJobError(BaseCipError):
    def __init__(self, message, param):
        super().__init__(
            code="GAE008",
            message="Erro ao cadastrar job {0}: {1}".format(param, message),
            friendly_message="Erro ao cadastrar job {0}.".format(param),
            http_status=500)


class JobDataApiUpdateProfileError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE009",
            message="Erro no update do profile: {}".format(message),
            friendly_message="Erro no update do profile.",
            http_status=422)


class JobDataApiUpdateFileError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE0010",
            message="Erro ao atualizar o arquivo: {}".format(message),
            friendly_message="Erro ao atualizar o arquivo.",
            http_status=500)


class JobDataApiDeliveryFileError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE011",
            message="Erro ao entregar o arquivo: {}".format(message),
            friendly_message="Erro ao entregar o arquivo.",
            http_status=500)


class MonitoringApiRequestError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE012",
            message="Erro no request para o Monitoring API: {}".format(message),
            friendly_message="Erro no request para o Monitoring API.",
            http_status=500)


class PublisherApiRequestError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE013",
            message="Erro no request para o PublisherAPI: {}".format(message),
            friendly_message="Erro no request para o publicador na EF.",
            http_status=500)


class EFApiRequestError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE014",
            message="Erro no request para o EF API: {}".format(message),
            friendly_message="Erro no request para o EF API.",
            http_status=500)


class EFApiDeliveryError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE015",
            message="Erro na entrega do profile para EF: {}".format(message),
            friendly_message="Erro na entrega do profile para EF.",
            http_status=500)


class EFApiPublishError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE016",
            message="Erro na publicacao do profile na EF: {}".format(message),
            friendly_message="Erro na publicação do profile na EF.",
            http_status=500)


class JobDataApiUpdateStatusjobError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE017",
            message="Erro no update de job enviado ao Job Data API: URL: {}".format(message),
            friendly_message="Erro no update de job enviado ao Job Data API.",
            http_status=500)


class OrquestratorApiProcessamentoMensagensError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE018",
            message="Erro no loop de processamento de mensagens: {}".format(message),
            friendly_message="Erro no loop de processamento de mensagens.",
            http_status=500)


class MonitoringApiUpdateStatusjobError(BaseCipError):
    def __init__(self, message):
        super().__init__(
            code="GAE019",
            message="Erro no update de job enviado ao Monitoring API: {}".format(message),
            friendly_message="Erro no update de job enviado ao Monitoring API.",
            http_status=500)

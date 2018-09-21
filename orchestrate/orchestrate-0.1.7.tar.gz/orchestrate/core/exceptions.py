class OrchestrateException(Exception):
  pass

class CheckExecutableError(OrchestrateException):
  pass

class CheckConnectionError(OrchestrateException):
  pass

from .error_aplicacion import ErrorAplicacion
class UserException(ErrorAplicacion):
  def __init__(self,mensaje):
    super().__init__(mensaje)
from .error_aplicacion import ErrorAplicacion
class FieldException(ErrorAplicacion):
  def __init__(self,mensaje):
    super().__init__(mensaje)
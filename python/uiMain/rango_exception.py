from .user_exception import UserException
class RangoException(UserException):
  def __init__(self,message="No se puede asignar un rango a este cliente"):
    super().__init__(message)
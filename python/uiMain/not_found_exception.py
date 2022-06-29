from .user_exception import UserException
class NotFoundException(UserException):
  def __init__(self,message='Articulo no encontrado'):
    super().__init__(message)
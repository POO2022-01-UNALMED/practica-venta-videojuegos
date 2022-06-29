from .user_exception import UserException
class   ClienteException(UserException):
  def __init__(self,message='Cliente no encontrado'):
    super().__init__(message)
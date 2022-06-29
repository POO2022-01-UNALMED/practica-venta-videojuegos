from .user_exception import UserException
class CashException(UserException):
  def __init__(self,message="Dinero insuficiente"):
    super().__init__(message)
    
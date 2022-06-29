from .field_exception import FieldException
class NumberException(FieldException):
  def __init__(self,message="se ingresaron valores incorrectos"):
    super().__init__(message)
    
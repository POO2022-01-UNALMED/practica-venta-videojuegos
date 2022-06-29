from .field_exception import FieldException


class NegativeException(FieldException):
    def __init__(self, message="Se ingresaron valores numericos negativos"):
        super().__init__(message)

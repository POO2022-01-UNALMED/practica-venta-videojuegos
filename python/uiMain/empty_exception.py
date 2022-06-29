from .field_exception import FieldException


class EmptyException(FieldException):
    def __init__(self, message="Faltan campos por llenar"):
        super().__init__(message)

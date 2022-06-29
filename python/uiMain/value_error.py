class Value_error(ValueError):
    def __init__(self):
        self.mensaje="Valor no permitido"
        super().__init__(self.mensaje)
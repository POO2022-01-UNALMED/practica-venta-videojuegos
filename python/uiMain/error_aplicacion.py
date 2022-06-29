class ErrorAplicacion(Exception):
    def __init__(self, extra_message="", message="Manejo de errores de la Aplicación: "):
        self.message = message + " " + extra_message
        super().__init__(self.message)

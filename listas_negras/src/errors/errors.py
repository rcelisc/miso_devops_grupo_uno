class ApiError(Exception):
    code = 422
    description = "Default message"

# 1. Errores en la creación de usuarios
class InvalidParams(ApiError):
    code=400
    description="El formato del id de la aplcacion no es UUID."

class EmailExist(ApiError):
    code=412
    description="Email ya existe"

# 403	El token no está en el encabezado de la solicitud.
class NoToken(ApiError):
    code=403
    description="El token no está en el encabezado de la solicitud."

class InvalidToken(ApiError):
    code=404
    description="El token no es valido."
from .base_command import BaseCommand
from ..errors.errors import NoToken, EmailExist, InvalidToken, InvalidParams
from sqlalchemy.exc import IntegrityError
from ..models.database import db_session
from ..models.blacklist import BlackList
import os, requests, uuid, datetime
from psycopg2.errors import UniqueViolation

class CreateMail(BaseCommand):
  def __init__(self, email, appId, description, clientIp, token):
    self.email=email
    self.appId=appId
    self.description=description
    self.clientIp=clientIp
    self.token = token

  def execute(self):
    if self.token == "":
        raise NoToken
    elif self.token != os.environ["SECRET_TOKEN"]:
        raise InvalidToken
    
    def es_formato_uuid(dato):
      try:
          uuid_obj = uuid.UUID(dato)
          return True
      except ValueError:
          return False

    if (es_formato_uuid(self.appId) == False):
       raise InvalidParams

    bl = BlackList(self.email, self.appId, self.description, self.clientIp , datetime.datetime.now())
    db_session.add(bl)
    try:
        db_session.commit()
        response={"Mensaje" : "Registro creado satisfactoriamente."}
        db_session.close()
        return response
    except  IntegrityError as e:
          if isinstance(e.orig, UniqueViolation):
            db_session.close()
            raise EmailExist
          else:
            db_session.close()
            response={"Mensaje" : "Error al crear el registro. -> Detalle -> " + str(e.detail)}
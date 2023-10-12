from .base_command import BaseCommand
from ..errors.errors import NoToken, InvalidToken
from ..models.blacklist import BlackList, BlackListSchema
from ..models.database import db_session
import os

bl_schema=BlackListSchema()

class GetMail(BaseCommand):
    def __init__(self, email,token):
        self.token = token
        self.email = email

    def execute(self):
        if self.token=="":
            raise NoToken
        elif self.token != os.environ["SECRET_TOKEN"]:
            raise InvalidToken
        result = db_session.query(BlackList).filter(BlackList.email == self.email).first()
        if result is None:
            return {"Existe" : False, "Motivo": "No existe el email solicitado."}
        else:
            db_session.close()
            return {"Existe" : True, "Motivo": str(result.blocked_reason)}
        

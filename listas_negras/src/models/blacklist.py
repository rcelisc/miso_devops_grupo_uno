from marshmallow import Schema, fields
from  sqlalchemy  import  Column, String, DateTime
from .database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Extender la clase Model proporcionada
class BlackList(Base):
    __tablename__  =  'blacklist'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email=Column(String, unique=True, nullable=False)
    app_uuid=Column(String)
    blocked_reason=Column(String)
    direccion_ip=Column(String)
    fecha_hora=Column(DateTime)

    def  __init__(self, email, app_uuid, blocked_reason, direccion_ip, fecha_hora):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.direccion_ip = direccion_ip
        self.fecha_hora = fecha_hora

class BlackListSchema(Schema):
    email = fields.Str()
    app_uuid = fields.Str()
    blocked_reason = fields.Str()
    direccion_ip = fields.Str()
    fecha_hora = fields.DateTime()


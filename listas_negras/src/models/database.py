from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

loaded = load_dotenv('.env.development')

if os.environ.get("DATABASE_URL") is None:
    userdb = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    port_db=os.environ["DB_PORT"]
    urldb = 'postgresql://' + userdb + ':' + password + '@' + host+ ':' +port_db + '/' + dbname #+ '?client_encoding=utf8'
else:
    urldb = os.environ.get("DATABASE_URL")
engine = create_engine(urldb)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
def init_db():
    Base.metadata.create_all(bind=engine)
    
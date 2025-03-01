from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app

Base = declarative_base()
engine = None
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False))

def init_db(app):
    global engine
    engine = create_engine(f'sqlite:///{app.config["DATABASE"]}', convert_unicode=True)
    db_session.configure(bind=engine)
    Base.metadata.create_all(bind=engine)

def get_db():
    return db_session

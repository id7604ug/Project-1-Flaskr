from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_sessionmaker(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Import all modules here so they are registered on the metadata properly
    import flaskr.models
    Base.metadata.create_all(bind=engine)

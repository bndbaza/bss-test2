from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = 'mysql+pymysql://root:35739517@192.168.0.51:3307/InOut2'

engine = create_engine(SQL_DATABASE_URL)#, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
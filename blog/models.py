from .database import Base
from sqlalchemy import Column, Integer, String, Date

# class Entry(Base):
#     __tablename__ = 'Entry'
#     Id = Column(Integer, primary_key=True)
#     RegNumber = Column(String(15),)
#     Date = Column(Date)
#     Organ = Column(String(100))
#     Address = Column(String(100))
#     Content = Column(String(500))
#     Sender = Column(String(200))
#     Wey = Column(String(200))

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(String(100))
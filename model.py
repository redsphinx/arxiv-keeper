from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import CONNECTION_STRING

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    arxiv_id = Column(String(32))
    title = Column(String(512))
    authors = Column(String(1024))
    categories = Column(String(512))
    abstract = Column(String(4096))
    read = Column(Boolean(), default=False)
    date = Column(DateTime())
    saved = Column(DateTime())

    def save(self):
        self.saved = datetime.now()
        session.add(self)
        session.commit()

    def mark_read(self):
        pass


engine = create_engine(CONNECTION_STRING)
if __name__ == '__main__':
    Base.metadata.create_all(engine)
else:
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

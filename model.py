from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    id_string = Column(String(32))
    title = Column(String(512))
    authors = Column(String(512))
    abstract = Column(String(2048))
    read = Column(Boolean())

    def save(self):
        session.add(self)
        session.commit()

    def mark_read(self):
        pass


engine = create_engine('mysql://root:@localhost/arxiv_keeper')
if __name__ == '__main__':
    Base.metadata.create_all(engine)
else:
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

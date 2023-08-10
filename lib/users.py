from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)
from texttable import Texttable


Base = declarative_base()
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class UserStorage(Base):
        __tablename__ = 'users'

        id = Column(Integer(), primary_key=True)
        user = Column(String())

        def __repr__(self): 
                return f"ID: {self.id} User: {self.user}"
        
        def showAll():
                engine = create_engine('sqlite:///users.db')
                Base.metadata.create_all(engine)
                Session = sessionmaker(bind=engine)
                session = Session()

                data = session.query(UserStorage).all()

                textTable = Texttable()
                textTable.header(['ID', 'Users'])

                for datum in data:
                        textTable.add_row([datum.id, datum.user])

                print(textTable.draw()) 


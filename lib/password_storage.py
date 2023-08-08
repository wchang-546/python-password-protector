from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)

Base = declarative_base()

class PasswordStorage(Base):
        __tablename__ = 'passwords'

        id = Column(Integer(), primary_key=True)
        username = Column(String())
        password = Column(String()) 
        platform = Column(String())

        def __repr__(self): 
                return f"Username: {self.username} Password: {self.password} Platform: {self.platform}"
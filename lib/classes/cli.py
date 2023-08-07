#!/usr/bin/env python3

# imports
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# data models
class PasswordStorage(Base):
        __tablename__ = 'passwords'

        id = Column(Integer(), primary_key=True)
        username = Column(String())
        password = Column(String()) 

        def __repr__(self): 
                return f"Username: {self.username} Password: {self.password}"

if __name__ == '__main__':
        engine = create_engine('sqlite:///passwords.db')
        Base.metadata.create_all(engine)

        # use our engine to configure a 'Session' class
        Session = sessionmaker(bind=engine)
        # use 'Session' class to create 'session' object 
        session = Session()

        example_password = PasswordStorage(
                username = "wchang",
                password = "efoijs" 
        )

        session.add(example_password)
        session.commit()

        print(example_password)



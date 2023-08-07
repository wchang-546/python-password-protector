#!/usr/bin/env python3

# imports
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)
from password_generator import PasswordGenerator

Base = declarative_base()

# data model
class PasswordStorage(Base):
        __tablename__ = 'passwords'

        id = Column(Integer(), primary_key=True)
        username = Column(String())
        password = Column(String()) 
        platform = Column(String())

        def __repr__(self): 
                return f"Username: {self.username} Password: {self.password} Platform: {self.platform}"
        

if __name__ == '__main__':
        engine = create_engine('sqlite:///passwords.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
def mainMenu(): 
        print('Welcome to the Python Password Protector. What would you like to do?')
        action = input(f"Create or Manage: ")

        if action.lower() == "manage":
                pass
                #Link function here to produce a list of current logins 

        elif action.lower() == "create":
                username = input(f"What will be your username? ")
                platform = input(f"What platform will this login be for? ")
                password = PasswordGenerator().password_gen()

                print(f"Here is a secure password for your {platform} account for username {username}.")
                print(f"{password}")

                
                new_password = PasswordStorage(
                        username = username,
                        password = password,
                        platform = platform
                )

                session.add(new_password)
                session.commit() 
                
                print("... \n"
                      "... \n"
                      "... \n")
                mainMenu()


mainMenu()

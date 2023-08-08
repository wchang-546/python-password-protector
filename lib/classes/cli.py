#!/usr/bin/env python3

# imports
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)
from password_generator import PasswordGenerator

Base = declarative_base()

# data model

if __name__ == '__main__':
        engine = create_engine('sqlite:///passwords.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
def mainMenu(): 
        print('Welcome to the Python Password Protector. What would you like to do?')
        action = input(f"Create or Manage: ")

        if action.lower() == "manage":
                
                #Link function here to produce a list of current logins 

                print("... \n"
                      "... \n"
                      "... \n")
                mainMenu()

        elif action.lower() == "create":
                new_password = PasswordGenerator().password_gen()

                session.add(new_password)
                session.commit() 
                
                print("... \n"
                      "... \n"
                      "... \n")
                mainMenu()


mainMenu()

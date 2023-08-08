#!/usr/bin/env python3

# imports
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)
from password_generator import PasswordGenerator
from password_storage import PasswordStorage

Base = declarative_base()

# data model

if __name__ == '__main__':
        engine = create_engine('sqlite:///passwords.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        
def mainMenu(): 
        print('Welcome to the Python Password Protector. What would you like to do?')
        action = input("Create or Manage: ")

        if action.lower() == "manage":
                print('Would you like to view or update logins?')
                action = input("View or Update:")
                all_logins = session.query(PasswordStorage)
                if action.lower() == "view":
                        print([login for login in all_logins])
                

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
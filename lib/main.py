#!/usr/bin/env python3

# imports
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)
from password_generator import PasswordGenerator
from password_storage import PasswordStorage

Base = declarative_base()


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
                        action = input("View or Update: ")
                        
                        if action.lower() == "view":
                                #Function to print all of the logins
                                PasswordStorage.showAll()
                        
                        if action.lower() == "update":
                                PasswordStorage.showAll()
                                print('Which login would you like to update?')

                                edit_login = input('Enter ID: ')

                                username = session.query(PasswordStorage).filter(PasswordStorage.username)
                                platform = session.query(PasswordStorage).filter(PasswordStorage.platform)
                                print(f'You have selected the login for {username} on {platform}')

                                #Thinking update options will be to Regenerate password or Delete login 
                                if action.lower() == "Regenerate password":
                                        pass

                                if action.lower() == "Delete password":
                                        to_delete = session.query(PasswordStorage).filter(PasswordStorage.id.like({edit_id}))

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
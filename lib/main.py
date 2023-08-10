#!/usr/bin/env python3

# imports
from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.orm import (declarative_base, sessionmaker)
from password_generator import PasswordGenerator
from password_storage import PasswordStorage
from hide_passwords import HidePasswords
from users import UserStorage

Base = declarative_base()


if __name__ == '__main__':
        engine = create_engine('sqlite:///passwords.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        def start_screen():
                UserStorage.showAll()
                print('Welcome to the Python Password Protector.')
        
        def login():
                print('Please enter your password:')
                userpass = "abc"
                action = input("Enter your password: ")
                if action != userpass:  
                        print("Invalid credentials. Your hard drive will now be deleted.")
                if action == userpass:
                        mainMenu()
                

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

                                login = session.query(PasswordStorage).get(edit_login)
                                print(f'You have selected the login for {login.username} on the {login.platform} platform')

                                action = input('Regenerate or Delete: ')
                                if action.lower() == "regenerate":
                                        #Function to regenerate the password 
                                        regenerated_password = PasswordGenerator().password_regenerate(login.username, login.platform)
                                        session.delete(login)
                                        session.add(regenerated_password)
                                        session.commit()
                                        print(f"The new login is username: {login.username}, password: {regenerated_password.password}, platform: {login.platform}")


                                if action.lower() == "delete":
                                        print(f'This login is now deleted: {login}')
                                        session.delete(login)
                                        session.commit()


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

start_screen()
login()
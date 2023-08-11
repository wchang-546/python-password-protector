#!/usr/bin/env python3

# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from password_generator import PasswordGenerator
from password_storage import PasswordStorage
from hide_passwords import HidePasswords
from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey)
from sqlalchemy.orm import (declarative_base, sessionmaker)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    passwords = relationship("Password", back_populates="user")

class Password(Base):
    __tablename__ = 'passwords'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    platform = Column(String, nullable=False)
    password = Column(String, nullable=False)

    user = relationship("User", back_populates="passwords")

PASSWORDS_DATABASE_URL = 'sqlite:///passwords.db'
passwords_engine = create_engine(PASSWORDS_DATABASE_URL)
PasswordsSession = sessionmaker(bind=passwords_engine)
passwords_session = PasswordsSession()

if __name__ == '__main__':
    Base.metadata.create_all(passwords_engine)

    def start_screen():
        HidePasswords.showAll()
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
                # Function to print all of the logins
                PasswordStorage.showAll()

            if action.lower() == "update":
                PasswordStorage.showAll()
                print('Which login would you like to update?')
                edit_login = input('Enter ID: ')

                login = passwords_session.query(Password).get(edit_login)
                print(f'You have selected the login for {login.user.username} on the {login.platform} platform')

                action = input('Regenerate or Delete: ')
                if action.lower() == "regenerate":
                    # Function to regenerate the password 
                    regenerated_password = PasswordGenerator().password_regenerate(login.user.username, login.platform)
                    passwords_session.delete(login)
                    passwords_session.add(regenerated_password)
                    passwords_session.commit()
                    print(f"The new login is username: {login.user.username}, password: {regenerated_password.password}, platform: {login.platform}")

                if action.lower() == "delete":
                    print(f'This login is now deleted: {login}')
                    passwords_session.delete(login)
                    passwords_session.commit()

            print("... \n"
                  "... \n"
                  "... \n")
            mainMenu()

        elif action.lower() == "create":
            new_password = PasswordGenerator().password_gen()

            passwords_session.add(new_password)
            passwords_session.commit()

            print("... \n"
                  "... \n"
                  "... \n")
            mainMenu()

    start_screen()
    login()

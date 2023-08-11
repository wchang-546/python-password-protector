from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import User, Password, Base

# Define the database URL for passwords
PASSWORDS_DATABASE_URL = 'sqlite:///passwords.db'

# Create an engine and session for the password database
passwords_engine = create_engine(PASSWORDS_DATABASE_URL)
PasswordsSession = sessionmaker(bind=passwords_engine)
passwords_session = PasswordsSession()

# Create tables if they don't exist
Base.metadata.create_all(passwords_engine)

# Create sample users
user1 = User(username='user1')
user2 = User(username='user2')

# Add sample users to the password session
passwords_session.add(user1)
passwords_session.add(user2)
passwords_session.commit()

# Create sample passwords
password1 = Password(user=user1, platform='Facebook', password='password123')
password2 = Password(user=user1, platform='Twitter', password='twitterpass')
password3 = Password(user=user2, platform='Instagram', password='instapass')

# Add sample passwords to the password session
passwords_session.add(password1)
passwords_session.add(password2)
passwords_session.add(password3)
passwords_session.commit()

print("Sample data added to the passwords database.")

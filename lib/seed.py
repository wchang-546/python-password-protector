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
wchang = User(username="wchang")
asmith = User(username="asmith")
antonio = User(username="antonio")
DJrulez = User(username="DJ")
josephB = User(username="josephB")

# Add sample users to the password session
passwords_session.add(wchang)
passwords_session.add(asmith)
passwords_session.add(antonio)
passwords_session.add(DJrulez)
passwords_session.add(josephB)
passwords_session.commit()

# Create sample passwords
p1 = Password(user=wchang, password="P1A2pcK2'Yp+", platform="Crunchyroll")
p2 = Password(user=asmith, password="7yWHP%h@@)'Yp+", platform="Github")
p3 = Password(user=antonio, password="rcK/1E@f^R,", platform="Bank of America")
p4 = Password(user=DJrulez, password="8y2GI\\F^Y", platform="FortNite")
p5 = Password(user=josephB, password="/],[\\PKl`0S", platform="Air Force One")

# Add sample passwords to the password session
passwords_session.add(p1)
passwords_session.add(p2)
passwords_session.add(p3)
passwords_session.add(p4)
passwords_session.add(p5)
passwords_session.commit()

print("Sample data added to the passwords database.")
import secrets, string
from password_storage import PasswordStorage

class PasswordGenerator:
    # def init(self, password):
    #     self.password = password 
    # # secure random string
    # secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(8)))
    # print(secure_str)
    # # Output QQkABLyK

    def password_gen(self):
        password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12)))
    
        username = input(f"What will be your username? ")
        platform = input(f"What platform will this login be for? ")
        password = password

        print(f"Here is a secure password for your {platform} account for username {username}. \n"
                f"{password}")

        new_password = PasswordStorage(
                username = username,
                password = password,
                platform = platform
        )

        return new_password

    

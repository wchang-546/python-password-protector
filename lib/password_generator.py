import secrets
import string
from password_storage import PasswordStorage


class PasswordGenerator:

    def password_gen(self):
        password = ''.join((secrets.choice(
            string.ascii_letters + string.digits + string.punctuation) for i in range(12)))

        username = input(f"What will be your username? ")
        platform = input(f"What platform will this login be for? ")
        password = password

        print(f"Here is a secure password for your {platform} account for username {username}: \n"
              f"{password}")

        new_password = PasswordStorage(
            username=username,
            password=password,
            platform=platform
        )

        return new_password

    def password_regenerate(self, uname, pform):
        password = ''.join((secrets.choice(
            string.ascii_letters + string.digits + string.punctuation) for i in range(12)))
        regenerated_password = PasswordStorage(
            username=uname,
            password=password,
            platform=pform
        )
        return regenerated_password
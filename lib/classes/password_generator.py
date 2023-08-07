import secrets
import string

class PasswordGenerator:
    # def init(self, password):
    #     self.password = password 
    # # secure random string
    # secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(8)))
    # print(secure_str)
    # # Output QQkABLyK

    def password_gen(self):
        # print(''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12))))
        return ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12)))
    

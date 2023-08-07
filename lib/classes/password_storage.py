class PasswordStorage:
    def __init__(self, username, password):
        self.username = username
        self.password = password 

    def print(self):
        print (f'Username: {self.username} Password: {self.password}')
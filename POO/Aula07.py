class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        #setter
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection



# servidor = Connection()
servidor = Connection.create_with_auth('gabriel', '123456')

# servidor.set_user('gabriel')
# servidor.set_password('123456')

print(servidor.user) 
print(servidor.password) 

from config.db import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.firstname = data["first_name"]
        self.lastname = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        
    @classmethod
    def insert_usuario(cls, first_name, last_name, email, password):
        query = f"INSERT INTO Usuario (first_name, last_name, email, password) VALUES ('{first_name}', '{last_name}', '{email}', '{password}');"
        results = connectToMySQL("cd_exam3").query_db(query)
        return results
    
    @classmethod
    def select_correo(cls, email):
        query = f"SELECT * FROM Usuario WHERE email = '{email}'"
        results = connectToMySQL("cd_exam3").query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios
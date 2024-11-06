from config.db import connectToMySQL

class Ideas:
    def __init__(self, data):
        self.id = data["id"]
        self.text = data["text"]
        self.usuario_id = data["usuario_id"]
        
    @classmethod
    def insert_texto(cls, text, usuario_id):
        query = f"INSERT INTO usuario (text, usuario_id) VALUES ('{text}', '{usuario_id}');"
        results = connectToMySQL("cd_exam").query_db(query)
        return results
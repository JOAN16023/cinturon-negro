from config.db import connectToMySQL

class Tasks:
    def __init__(self, data):
        self.id = data["user_id"]
        self.name = data["name"]
        self.status = data["status"]
        self.date = data["date"]
        self.usuario_id = data["id"]
        
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM Tasks"
        results = connectToMySQL('cd_exam3').query_db(query)
        tasks = []
        for task in results:
            tasks.append(cls(task))
        return tasks
    
    @classmethod
    def select_one(cls, user_id):
        query = f"SELECT * FROM Tasks WHERE user_id = {user_id}"
        results = connectToMySQL('cd_exam3').query_db(query)
        tasks = []
        for task in results:
            tasks.append(cls(task))
        return tasks
    
    @classmethod
    def insert(cls, name, status, date):
        query = f"INSERT INTO Tasks (name, status, date) VALUES ('{name}', '{status}', '{date}')"
        result = connectToMySQL('cd_exam3').query_db(query)
        return result
    
    @classmethod
    def update(cls, usuario_id, name, status, date):
        query = f"UPDATE Tasks SET name='{name}', status='{status}', date='{date}' WHERE usuario_id={usuario_id}"
        result = connectToMySQL('cd_exam3').query_db(query)
        return result
    
    @classmethod
    def delete_one(cls, usuario_id):
        query = f"DELETE FROM Tasks WHERE usuario_id={usuario_id}"
        result = connectToMySQL('cd_exam3').query_db(query)
        return result
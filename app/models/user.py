from flask_bcrypt import Bcrypt
import uuid
from app import db


bcrypt = Bcrypt()

class User:
    def __init__(self, username, email, password):
        self.user_id = uuid.uuid4()
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        db.users.insert_one({
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "_id": str(self.user_id)
        })

    @staticmethod
    def find_by_username(username):
        return db.users.find_one({"username": username})
    
    @staticmethod
    def find_by_uid(uid):
        return db.users.find_one({"_id": uid})
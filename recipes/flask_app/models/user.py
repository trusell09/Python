from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    db_name = "users_recipes"

    @classmethod
    def add(cls,data):
        query = """INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) 
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,now(),now())"""
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users


    @staticmethod
    def validate(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)
        if len(user["first_name"]) < 2:
            flash("first name too short","register")
            is_valid= False
        if len(user["last_name"]) < 2:
            flash("last name too short","register")
            is_valid= False
        if len(results) >= 1:
            flash("users already exists","register")
            is_valid=False
        if not EMAIL_REGEX.match(user["email"]):
            flash("not an email","register")
            is_valid=False
        if len(user["password"]) < 2:
            flash("password is too short","register")
            is_valid= False
        if user["password"] != user["confirm"] or user["password"] == "":
            flash("passwords does not match","register")
        return is_valid
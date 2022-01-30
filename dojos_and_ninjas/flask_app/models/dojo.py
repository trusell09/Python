from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]

    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        all_dojos=[]
        for dojo in results:
            print(dojo)
            all_dojos.append( cls(dojo) )
        print(all_dojos[0].created_at)
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        dojo=cls(results[0])
        if results[0]['ninjas.id']!=None:
            for row in results:
                row_data={
                    'id':row['ninjas.id'],
                    'dojo':dojo,
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'age':row['age'],
                    'created_at':row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at']
                }
                dojo.ninjas.append(Ninja(row_data))
        return dojo

    @classmethod
    def add_new(cls, data):
        query="INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dojo_name)s, NOW(), NOW());"
        dojo_id=connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return dojo_id
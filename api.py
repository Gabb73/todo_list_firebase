import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import datetime

credential = credentials.Certificate("api_key_api.json")
fireb = firebase_admin.initialize_app(credential)

db = firestore.client()

users_ref = db.collection("users/username")


def leer_users( ):
    docs = users_ref.get()
    for user in docs:
        print(f"ID: {user.id} => DATA:{user.to_dict()}")


def leer_user( ):
    user = users_ref.document("id").get( )
    print(user.to_dict()) 



def crear_user(Username, task):
    users_ref.document().set(Username)
    users_ref.document().set(task)


new_task = {"name": "Gabriela Solorzano", 
            "check": "Realizar tarea",
            "fecha": datetime.datetime.now()
            }

new_user = {"Username": "GabySlrzn7",
            }
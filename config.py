import pymongo
import certifi 

con_str="mongodb+srv://BJakeLando:Doorgunner1!!@cluster0.xgnohsr.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("ArtStore")



me = {
    "name": "Brandon",
    "last_name": "Landers",
    "age": 29

}

def hello():
    print("Hello there")
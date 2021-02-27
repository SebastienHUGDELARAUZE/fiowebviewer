# importing pymongo
from pymongo import MongoClient

database = {"name": "fiowebviewer",
            "host": "localhost",
            "port": 27017,
            "username": "admin",
            "password": "pass"
            }


def insertInMongo(fiojson):
    # establishing connection
    connect = MongoClient(database["host"], database["port"], username=database["username"],
                          password=database["password"])

    # connecting or switching to the
    db = connect[database["name"]]

    # creating or switching to demoCollection
    collection = db[database["name"]]

    collection.insert_one()

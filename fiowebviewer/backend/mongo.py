# importing pymongo
from pymongo import MongoClient

database = {"name": "fiowebviewer",
            "host": "localhost",
            "port": 27017,
            "username": "admin",
            "password": "pass"
            }


def insertInMongo(my_dic):
    """
    Insert a dict object in the mongo

    :param my_dic: dic
    """

    # establishing connection
    connect = MongoClient(database["host"], database["port"], username=database["username"],
                          password=database["password"])

    db = connect[database["name"]]
    collection = db[database["name"]]

    collection.insert_one(my_dic)

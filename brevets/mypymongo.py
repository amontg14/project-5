import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevets
collection = db.lists

def brevet_insert(brevet_dist_km, begin_date, items):
    output = collection.insert_one({
        "brevet_dist_km": brevet_dist_km,
        "begin_date": begin_date,
        "items": items})

    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)

def brevet_find():
    lists = collection.find().sort("_id", -1).limit(1)
    for a_list in lists:
        return a_list["brevet_dist_km"], a_list["begin_date"], a_list["items"]

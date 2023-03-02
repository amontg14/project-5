import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevets
collection = db.lists

def brevet_insert(brevet_dist_km, start_time, items):
    output = collection.insert_one({
        "brevet_dist_km": brevet_dist_km,
        "start_time": start_time,
        "items": items})

    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)

def brevet_find():
    lists = collection.find().sort("_id", -1).limit(1)
    for a_list in lists:
        return a_list["brevet_dist"], a_list["start_time"], a_list["items"]

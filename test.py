import pymongo
client = pymongo.MongoClient("mongodb+srv://chirag04:up65dp2788@cluster1.z0xulk8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
db = client.test
print(db)

d = {
    "name" : "aditya",
    "email" : "aditya@ineuron.ai",
    "surname" : "dubey"
}

d = {
    "name" : "aditya",
    "email" : "aditya@ineuron.ai",
    "surname" : "dubey"
}

d = {
    "name" : "aditya",
    "email" : "aditya@ineuron.ai",
    "surname" : "dubey"
}

d = {
    "name" : "aditya",
    "email" : "aditya@ineuron.ai",
    "surname" : "dubey"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
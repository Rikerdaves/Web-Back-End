from pymongo import MongoClient

client = MongoClient("mongodb+srv://ladydmc:devilmaycry5@apiserver.lcs3qz2.mongodb.net/?retryWrites=true&w=majority")
db = client["apiserver"]



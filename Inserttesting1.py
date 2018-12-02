import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://Sahil:Sahil_742995@ds139844.mlab.com:39844/aqua')
db = client['aqua']

post = {
    "Temperature" : "21",
    "waterLevel" : "2"}

posts = db.posts
posts.insert_one(post) 

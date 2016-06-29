#!/usr/local/bin/python
#coding=utf-8

import pymongo
import datetime

conn = pymongo.Connection('localhost',27017)
db = conn.test_database
collection = db.test_collection

post = {"author": "Mike","text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
print collection.insert(post)

posts = [post] * 3
print collection.insert(posts)

print db.collection_names()

print collection.find_one()
print collection.find()
print collection.find({"author": "Mike"})

collection.remove({'author': 'Mike'})

collection.update({'author': 'Mike'}, {'$set':{'text':'haha'}})
print collection.find()

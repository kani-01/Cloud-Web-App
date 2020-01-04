from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
#print(client)
db = client.restaurant

'''
mydict = { "name": "Kani", "address": "Village on Sixth" }
x = db.docs.insert_one(mydict)

mydoc = db.docs.find({"name":"Kani"})
for x in mydoc:
    print(x)
'''

mykey1 = input("Enter the Key to search for ")
myvalue1 = input("Enter the Value to search for ")

myquery = { mykey1: myvalue1 }
db.docs.delete_one(myquery)

mydoc = db.docs.find({"name":"Kani"})
for x in mydoc:
    print(x)
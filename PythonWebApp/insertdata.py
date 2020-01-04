from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
#print(client)
db = client.restaurant

#mykey1 = input("Enter the Key to search for ")
#myvalue1 = input("Enter the Value to search for ")

mydict = { "name": "Ezhil", "address": "Village on Sixth" }
x = db.docs.insert_one(mydict)

mydoc = db.docs.find_one({"name":"Ezhil"})
print(mydoc)
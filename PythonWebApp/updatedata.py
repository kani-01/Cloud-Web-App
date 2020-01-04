from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
#print(client)
db = client.restaurant

mykey1 = input("Enter the Key to search for ")
myvalue1 = input("Enter the Value to search for ")

mychangekey = input("Enter the Key to Update ")
mychangevalue = input("Enter the New Value to Update ")

myquery = { mykey1: myvalue1 }
newvalues = { "$set": { mychangekey: mychangevalue }}

db.docs.update_many(myquery, newvalues)

mydoc=db.docs.find({"name":"Kayal"})
for x in mydoc:
    print(x)

mydoc1=db.docs.find({"name":"Kani"})
for x in mydoc1:
    print(x)
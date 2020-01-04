from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
#print(client)
db = client.restaurant
#mydict={"":""}
def valuestoinsert():
    status = 'Y'
    mydict={}
    while(status != ('n' or 'N')):
        mykey1 = input("Enter the Key to add : ")
        myvalue1 = input("Enter the Value to add : ")
        mydict[mykey1] = myvalue1
        status = input("Do you want to add more Attributes: Enter 'Y' or 'N' : ")
    print(mydict)
    return mydict


mydict = valuestoinsert()
#mydict = { "name": "Ezhil", "address": "Village on Sixth" }
x = db.docs.insert_one(mydict)

mydoc = db.docs.find_one({"name":"Hafsa"})
print(mydoc)


from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
print(client)
db = client.restaurant
#mydoc = db.docs
count=db.docs.count()
print(count)
onedoc=db.docs.find_one({"borough":"Bronx"})
print(onedoc)

#mydict = { "name": "Kayal", "address": "Village on Sixth" }
#x = db.docs.insert_one(mydict)

manydoc=db.docs.find({"address":"California"})
for x in manydoc:
    print(x)

mydoc=db.docs.find_one({"name":"Kayal"})
print(mydoc)


myquery = { "address": "Village on Sixth" }
newvalues = { "$set": { "address": "California" }}

db.docs.update_many(myquery, newvalues)

mydoc=db.docs.find_one({"name":"Kayal"})
print(mydoc)

mydoc=db.docs.find_one({"name":"Kani"})
print(mydoc)

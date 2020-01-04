from pymodm import connect

#Establish a connection to the database and call the connection my-atlas-app
connect(
'mongodb://kani:Terence04@clustermongodb-shard-00-00-xwcjz.gcp.mongodb.net:27017,clustermongodb-shard-00-01-xwcjz.gcp.mongodb.net:27017,clustermongodb-shard-00-02-xwcjz.gcp.mongodb.net:27017/test?ssl=true&replicaSet=ClusterMongoDB-shard-0&authSource=admin&retryWrites=true', 
    alias='my-atlas-app'
)

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient("mongodb://kani:Terence04@clustermongodb-shard-00-00-xwcjz.gcp.mongodb.net:27017,clustermongodb-shard-00-01-xwcjz.gcp.mongodb.net:27017,clustermongodb-shard-00-02-xwcjz.gcp.mongodb.net:27017/test?ssl=true&replicaSet=ClusterMongoDB-shard-0&authSource=admin&retryWrites=true")
client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")

db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
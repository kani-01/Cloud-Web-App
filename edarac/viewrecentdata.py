from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta

gettime = datetime.now()
#gettime1 = str(gettime)
#print(type(gettime1))
starttime= str(gettime)
print("starttime : ",starttime,"type  : ",type(starttime))

print("My time is",starttime)  
client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
#print(client)
db = client.iotsensordata
#sleep(1)
#gettime1 = datetime.now()
#mytime1= gettime.strftime('%Y-%m-%d %H:%M:%S')
print("My time is",starttime) 
subtime = gettime - timedelta(minutes=5)
endtime= str(subtime)
print ("time is " ,endtime)
print(type(endtime))
#print(type(endtime))
endtime1 = '"'+ endtime + '"'
print("endtime1 : ",endtime1)
print(type(endtime1))
#mykey1 = input("Enter the Key to search for ")
#myvalue1 = input("Enter the Value to search for ")
myquery = {"timestamp":{"$gte": endtime}}
mydocs=db.sensorvalues.find(myquery)
for x in mydocs:
    print(x)

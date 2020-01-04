from pymongo import MongoClient
#from pprint import pprint

client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
#print(client)
db = client.restaurant
d={}
dlist=[]
#for i in xrange(0,100):
    #d['data']=i
    #dlist.append(d.copy())
    #print(d)

mydocs=db.docs.find_one()
i = 0
for x in mydocs:
    print(x)
    d[i] = x
    dlist.append(d.copy())
    i = i + 1

print(dlist)
    


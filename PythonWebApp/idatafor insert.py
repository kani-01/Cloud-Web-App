from datetime import datetime

gettime = datetime.now()
mytime= gettime.strftime('%Y-%m-%d %H:%M:%S')
print(mytime)

mycoord={}
myaddress={}
myentirelist = {}
mygradelist = {}
# Retrieve the HTTP POST request parameter value from 'request.form' dictionary
mybuilding = input("Enter building data : ")  # get(attr) returns None if attr is not present
mycoord0  = float(input("Enter coord0 data : "))
mycoord1  = float(input("Enter coord1 data : "))
mycoord['0']=mycoord0
mycoord['1']=mycoord1
print("mycoord is : ", mycoord)
mystreet = input("Enter street data : ")
myzipcode = input("Enter zipcode data : ")
myborough  = input("Enter borough data : ")
mycuisine  = input("Enter cuisine data : ")
myresname  = input("Enter restaurant name data: ")
myresid = input("Enter restaurant id data : ")
myaddress['building']=mybuilding
myaddress['coord']=mycoord
myaddress['street']=mystreet
myaddress['zipcode']=myzipcode
print("myaddress is : ", myaddress)
gradearray0 = {}
gradearray1 = {}
gradearray2 = {}
gradearray3 = {}
gradearray4 = {}
mygrade0 = input("Enter grade0 data : ")
myscore0 = int(input("Enter score0 data : "))
gradearray0['date']=mytime
gradearray0['grade']=mygrade0
gradearray0['score']=myscore0
mygradelist['0']=gradearray0
mygrade1 = input("Enter grade1 data : ")
myscore1 = int(input("Enter score1 data : "))
gradearray1['date']=mytime
gradearray1['grade']=mygrade1
gradearray1['score']=myscore1
mygradelist['1']=gradearray1
mygrade2 = input("Enter grade2 data : ")
myscore2 = int(input("Enter score2 data : "))
gradearray2['date']=mytime
gradearray2['grade']=mygrade2
gradearray2['score']=myscore2
mygradelist['2']=gradearray2
mygrade3 = input("Enter grade3 data : ")
myscore3 = int(input("Enter grade3 data : "))
gradearray3['date']=mytime
gradearray3['grade']=mygrade3
gradearray3['score']=myscore3
mygradelist['3']=gradearray3
mygrade4 = input("Enter grade4 data : ")
myscore4 = int(input("Enter score4 data : "))
gradearray4['date']=mytime
gradearray4['grade']=mygrade4
gradearray4['score']=myscore4
mygradelist['4']=gradearray4
print("My Grades are: ", mygradelist)
myentirelist['address']=myaddress
myentirelist['borough']=myborough
myentirelist['cuisine']=mycuisine
myentirelist['grades']=mygradelist
myentirelist['name']=myresname
myentirelist['restaurant_id']=myresid
print("My Entire Dictionary is", myentirelist)
from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
from pprint import pprint
import pprintjson


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/signin', methods=['POST'])
def signin():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _username = request.form.get('username')  # get(attr) returns None if attr is not present
    _password = request.form.get('password')

    # Validate and send response
    if _username == 'kani' and _password == 'Terence04':
        return render_template('signin.html', username=_username)
    else:
        return render_template('notauthorized.html')  # 400 Bad Request


@app.route('/search', methods=['POST'])
def search():
    if request.form['search_button'] == 'Search':
        return render_template('search.html')
    else:
        pass


@app.route('/insert', methods=['POST'])
def insert():
    if request.form['insert_button'] == 'Insert':
        return render_template('insert.html')
    else:
        pass


@app.route('/update', methods=['POST'])
def update():
    if request.form['update_button'] == 'Update':
        return render_template('update.html')
    else:
        pass


@app.route('/delete', methods=['POST'])
def delete():
    if request.form['delete_button'] == 'Delete':
        return render_template('delete.html')
    else:
        pass


@app.route('/searching', methods=['POST'])
def searching():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('searchkey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('searchvalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant
    d = {}
    dlist = []
    mydocs = db.docs.find({mykey1:myvalue1})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("searchoutput.html",mydocs=dlist)


@app.route('/inserting', methods=['POST'])
def inserting():
    gettime = datetime.now()
    mytime = gettime.strftime('%Y-%m-%d %H:%M:%S')
    print(mytime)
    mycoord = {}
    myaddress = {}
    myentirelist = {}
    mygradelist = {}
    mybuilding = request.form.get('building')
    mycoord0 = request.form.get('coord0')
    mycoord1 = request.form.get('coord1')
    mycoord['0'] = mycoord0
    mycoord['1'] = mycoord1
    print("mycoord is : ", mycoord)
    mystreet = request.form.get('street')
    myzipcode = request.form.get('zipcode')
    myborough = request.form.get('borough')
    mycuisine = request.form.get('cuisine')
    myresname = request.form.get('resname')
    myresid = request.form.get('resid')
    myaddress['building'] = mybuilding
    myaddress['coord'] = mycoord
    myaddress['street'] = mystreet
    myaddress['zipcode'] = myzipcode
    print("myaddress is : ", myaddress)
    gradearray0 = {}
    gradearray1 = {}
    gradearray2 = {}
    gradearray3 = {}
    gradearray4 = {}
    mygrade0 = request.form.get('grade0')
    myscore0 = request.form.get('score0')
    gradearray0['date'] = mytime
    gradearray0['grade'] = mygrade0
    gradearray0['score'] = myscore0
    mygradelist['0'] = gradearray0
    mygrade1 = request.form.get('grade1')
    myscore1 = request.form.get('score1')
    gradearray1['date'] = mytime
    gradearray1['grade'] = mygrade1
    gradearray1['score'] = myscore1
    mygradelist['1'] = gradearray1
    mygrade2 = request.form.get('grade2')
    myscore2 = request.form.get('score2')
    gradearray2['date'] = mytime
    gradearray2['grade'] = mygrade2
    gradearray2['score'] = myscore2
    mygradelist['2'] = gradearray2
    mygrade3 = request.form.get('grade3')
    myscore3 = request.form.get('score3')
    gradearray3['date'] = mytime
    gradearray3['grade'] = mygrade3
    gradearray3['score'] = myscore3
    mygradelist['3'] = gradearray3
    mygrade4 = request.form.get('grade4')
    myscore4 = request.form.get('score4')
    gradearray4['date'] = mytime
    gradearray4['grade'] = mygrade4
    gradearray4['score'] = myscore4
    mygradelist['4'] = gradearray4
    print("My Grades are: ", mygradelist)
    myentirelist['address'] = myaddress
    myentirelist['borough'] = myborough
    myentirelist['cuisine'] = mycuisine
    myentirelist['grades'] = mygradelist
    myentirelist['name'] = myresname
    myentirelist['restaurant_id'] = myresid
    print("My Entire Dictionary is", myentirelist)

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant
    mydict = myentirelist
    x = db.docs.insert_one(mydict)

    d = {}
    dlist = []
    mydocs = db.docs.find({'restaurant_id': myresid})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("insertoutput.html",mydocs=dlist)


@app.route('/updating', methods=['POST'])
def updating():
        # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('updatekey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('updatevalue')
    mychangekey = request.form.get('newkey')
    mychangevalue = request.form.get('newvalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant
    myquery = {mykey1: myvalue1}
    newvalues = {"$set": {mychangekey: mychangevalue}}

    db.docs.update_many(myquery, newvalues)

    d = {}
    dlist = []
    mydocs = db.docs.find({mychangekey: mychangevalue})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("updateoutput.html", mydocs=dlist)

@app.route('/deleting', methods=['POST'])
def deleting():
        # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('deletekey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('deletevalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant

    myquery = {mykey1: myvalue1}
    db.docs.delete_one(myquery)

    d = {}
    dlist = []
    mydocs = db.docs.find({mykey1: myvalue1})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("deleteoutput.html", mydocs=dlist)

if __name__ == '__main__':
    app.run(debug=True)

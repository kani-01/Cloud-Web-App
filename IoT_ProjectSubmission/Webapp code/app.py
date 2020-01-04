# Author : Kanimozhi Kalaichelvan
# WebApp for Green House Monitoring 

from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta

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


@app.route('/view', methods=['POST'])
def view():
    if request.form['view_button'] == 'View':
        return render_template('view.html')
    else:
        pass

@app.route('/search', methods=['POST'])
def search():
    if request.form['search_button'] == 'Search':
        return render_template('search.html')
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


@app.route('/viewing', methods=['POST'])
def viewing():
#     Retrieve the HTTP POST request parameter value from 'request.form' dictionary
#    mykey1 = request.form.get('searchkey')  # get(attr) returns None if attr is not present
#    myvalue1 = request.form.get('searchvalue')
    client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.iotsensordata
    d = {}
    dlist = []
    mydocs=db.sensorvalues.aggregate([{"$sort":{"timestamp":-1}},{"$limit": 10}])
    for x in mydocs:
    	print(x)
    	d['data'] = x
    	dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("viewingoutput.html",mydocs=dlist)
        
        
@app.route('/viewall', methods=['POST'])
def viewall():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
#    mykey1 = request.form.get('searchkey')  # get(attr) returns None if attr is not present
#    myvalue1 = request.form.get('searchvalue')

    client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.iotsensordata
    d = {}
    dlist = []
    mydocs = db.sensorvalues.find()
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
        dlist = dlist
    print(dlist)

    if request.method == 'POST':
        return render_template("viewoutput.html",mydocs=dlist)
        
@app.route('/searching', methods=['POST'])
def searching():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('searchkey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('searchvalue')

    client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.iotsensordata
    d = {}
    dlist = []
    mydocs = db.sensorvalues.find({mykey1:myvalue1})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("searchoutput.html",mydocs=dlist)

@app.route('/updating', methods=['POST'])
def updating():
        # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('updatekey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('updatevalue')
    mychangekey = request.form.get('newkey')
    mychangevalue = request.form.get('newvalue')

    client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.iotsensordata
    myquery = {mykey1: myvalue1}
    newvalues = {"$set": {mychangekey: mychangevalue}}
    db.sensorvalues.update_many(myquery, newvalues)
    d = {}
    dlist = []
    mydocs = db.sensorvalues.find({mychangekey: mychangevalue})
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
    myoption = request.form.get('option')

    client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.iotsensordata
    
    myquery = {mykey1: myvalue1}
    db.sensorvalues.delete_one(myquery)
    myquery = {mykey1: myvalue1}
    if(myoption=="yes"):
        db.sensorvalues.delete_one(myquery)
        d = {}
        dlist = []
        mydocs = db.sensorvalues.find({mykey1: myvalue1})
        for x in mydocs:
            print(x)
            d['data'] = x
            dlist.append(d.copy())
        print(dlist)

        if request.method == 'POST':
            return render_template("deleteoutput.html", mydocs=dlist)

    if(myoption == "no"):
        if request.method == 'POST':
            return render_template("notdeleted.html")
    
    if request.method == 'POST':
        return render_template("deleteoutput.html", mydocs=dlist)

if __name__ == '__main__':
    app.run(debug=True)

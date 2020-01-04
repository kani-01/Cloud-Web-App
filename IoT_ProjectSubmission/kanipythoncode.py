
# Author 	 : Kanimozhi Kalaichelvan
# Professor : Husnu S. Narman
# paho-mqtt imports
import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
# mongodb imports
from pymongo import MongoClient
#from pprint import pprint
# Timestamp
from datetime import datetime
# Mail import
import smtplib
# Temperature and soil moisture sensor - GPIO17 Pin 11
import Adafruit_DHT #Import DHT Library for sensor
# To read Soil Moisture
import RPi.GPIO as GPIO

connflag = False
sensor_name = Adafruit_DHT.DHT11 #we are using the DHT11 sensor
sensor_pin = 17 #The sensor is connected to GPIO17 on Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
# Get Input from pin GPIO21 Pin 40


def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = "a2bea2ntco4ibe-ats.iot.us-east-2.amazonaws.com"
awsport = 8883
clientId = "sparkle1kani"
thingName = "sparkle"
caPath = "AmazonRootCA1.pem"
certPath = "090a2a5559-certificate.pem.crt"
keyPath = "090a2a5559-private.pem.key"


mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()



while 1==1:
    #sleep(5)
    if connflag == True:
        gettime = datetime.now()
        mytime= gettime.strftime('%Y-%m-%d %H:%M:%S')
        timing = mytime[0:19]
        print("My time is",mytime)        
        tempreading1 = uniform(20.0,25.0)
        tempreading = str(round(tempreading1,2))  
        # Read DHT11 Temperature and Humidity Information from the Sensor
        humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin) #read from sensor and save respective values in temperature and humidity varibale
        temperature = str(temperature)
        humidity = str(humidity)
        mqttc.publish("temperature", temperature, qos=0)
        print("msg sent: temperature " + temperature )
        print("msg sent: humidity " + humidity )
        # Soil Moisture Sensor
        water= GPIO.input(21)#"Water Not Present"
        
        if water == 0:
            waterpresence = "Water Present"
        else:
            waterpresence = "Water Not Present"
        
        
        # Alert Emails : Send an Alert Email from your Raspberry Pi to User : kanimalli22@gmail.com
        if temperature > '20' :
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("kani.msec@gmail.com","Terence@04")
            SUBJECT = "Greenhouse Temperature ALERT!!!"
            temp = str(temperature)
            tempmsg = "\n Message from Your Greenhouse \n Your Temperature is High : " + temp + "\n Please Take Appropriate Action";
            completemsg = 'Subject: {}\n\n {}'.format(SUBJECT, tempmsg)
            server.sendmail("kani.msec@gmail.com","kanimalli22@gmail.com",completemsg)
            server.quit()
            
        if waterpresence == "Water Not Present" :
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("kani.msec@gmail.com","Terence@04")
            SUBJECT = "Greenhouse Watering ALERT!!!"
            #temp = str(tempreading)
            watmsg = "\n Message from Your Greenhouse \n Water in your Greenhouse has dried up\n Soil Moisture Sensor: " + waterpresence + "\n Please Water Your Plants!!!";
            completemsg = 'Subject: {}\n\n {}'.format(SUBJECT, watmsg)
            server.sendmail("kani.msec@gmail.com","kanimalli22@gmail.com",completemsg)
            server.quit()
        
        # Connect to MongoDB Atlas
        client = MongoClient("mongodb+srv://kani:terence04@cluster0-yllav.gcp.mongodb.net/test?retryWrites=true")
        #print(client)
        db = client.iotsensordata
        mydocs = {}
        
        # Put this code above mongoclient to form the Structure of data being sent 
        key = "timestamp"
        mydocs[key] = timing         
        key = "temperature"
        mydocs[key] = temperature
        key = "humidity"
        mydocs[key] = humidity  
        key = "soil moisture"
        mydocs[key] = waterpresence  
        # Insert into MongoDB Atlas : kani , terence04
        x = db.sensorvalues.insert_one(mydocs)
        print(mydocs)
    else:
        print("waiting for connection...")
    sleep(5)
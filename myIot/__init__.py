import paho.mqtt.client as mqtt

import pyrebase

config = {
    "apiKey": "AIzaSyAZFtoOAhpIu1Y96McMpQkxY0eaAhcLWWo",
    "authDomain": "arduino-mqtt99.firebaseapp.com",
    "databaseURL": "https://arduino-mqtt99-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "arduino-mqtt99.appspot.com",
}

firebase = pyrebase.initialize_app(config)


def updateData(data):
    db = firebase.database()
    db.child('report').push({'text':data})

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("report")


def on_message(client, userdata, msg):
    urlServer = "https://arduino-mqtt99.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    data = str(msg.payload.decode("utf-8"))
    print(data)

    if msg.topic=='report':
        print(data)
        updateData(data)

client = mqtt.Client()

from django.shortcuts import render,HttpResponse
from .__init__ import updateData


import pyrebase


# Create your views here.
def testUpdateData(request,data):

    print(data)
    updateData(data)
    # config = {
    #     "apiKey": "AIzaSyAZFtoOAhpIu1Y96McMpQkxY0eaAhcLWWo",
    #     "authDomain": "arduino-mqtt99.firebaseapp.com",
    #     "databaseURL": "https://arduino-mqtt99-default-rtdb.asia-southeast1.firebasedatabase.app",
    #     "storageBucket": "arduino-mqtt99.appspot.com",
    # }
    #
    # firebase = pyrebase.initialize_app(config)
    # db = firebase.database()
    # db.child('report').push({'text': data})

    return  HttpResponse('Done: {}'.format(data))
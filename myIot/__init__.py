import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("report")


def on_message(client, userdata, msg):
    urlServer = "https://arduino-mqtt99.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    data = str(msg.payload.decode("utf-8"))
    print(data)

    if msg.topic=='report':
        print(data)


client = mqtt.Client()

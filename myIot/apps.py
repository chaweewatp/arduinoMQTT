from django.apps import AppConfig
from .__init__ import on_connect, on_message, client


class MyiotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myIot'

    def ready(self):
        print('start MQTT client')
        # client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set("jcomonwc:jcomonwc", password='dN9RgLra7acyfrwM0_WR3S9UGCbspszQ')
        client.connect("toad.rmq.cloudamqp.com", 1883, 60)
        client.loop_start()
        print('MQTT client started')

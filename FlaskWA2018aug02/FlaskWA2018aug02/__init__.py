"""
The flask application package.
"""

from flask import Flask, Response
import time
from azure.servicebus import ServiceBusService, Message, Queue
app = Flask(__name__)

import FlaskWA2018aug02.views

@app.route('/event_stream')
def stream():
    def event_stream():
        while True:
            
            bus_service = ServiceBusService(
                service_namespace='svcbusqueintellidemo',
                shared_access_key_name='RootManageSharedAccessKey',
                shared_access_key_value='aEnrEVeuuAziCIylqxj1yggQ4nZoJULZKxPT5CHgCbU=', 
            )

            iotmsg = bus_service.receive_queue_message('iothubqueuefri27-ns', peek_lock=False)

            #time.sleep(3)
            yield 'data: %s\n\n' % iotmsg.body

    return Response(event_stream(), mimetype="text/event-stream")
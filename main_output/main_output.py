#!/usr/bin/env python
import pika

# when RabbitMQ is running on localhost
#params = pika.ConnectionParameters('localhost')

# when RabbitMQ broker is running on network
params = pika.ConnectionParameters('rabbitmq')

# create the connection to broker
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Receive messages from the queue
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='to_workers', on_message_callback=callback, auto_ack=True)

# start listening
channel.start_consuming()

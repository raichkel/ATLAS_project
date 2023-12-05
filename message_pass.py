import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='to_workers')

# Send a message to the queue
channel.basic_publish(exchange='', routing_key='to_workers', body='Hello, RabbitMQ!')

print(" [x] Sent the fileString")

# Receive messages from the queue
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='to_workers', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
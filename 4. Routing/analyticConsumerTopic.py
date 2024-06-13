import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print("Analytic Received: ", body)

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here

connection = pika.BlockingConnection(connectionParameters)

channel = connection.channel()

# We need an exchage
channel.exchange_declare(exchange='routingTopic', exchange_type=ExchangeType.topic)

# We will let the server decide the queue name and when the connection close the queue will be deleted
queue = channel.queue_declare(queue='', exclusive=True)

# Bind the queue to the exchange with routing key of payment. Only the messages that have routing key
# as peyment will be sent to this queue

# This will consume every message that has routing key of .europe.
channel.queue_bind(exchange='routingTopic', queue=queue.method.queue, routing_key='*.europe.*')

channel.basic_consume(queue=queue.method.queue, on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press Ctrl+C")

channel.start_consuming()

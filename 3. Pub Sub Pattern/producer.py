import pika
from pika.exchange_type import ExchangeType

connectionPara = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connectionPara)

channel = connection.channel()

# In pub sub pattern, we don't need to declare the queue, we just need to declare the exchange. Each consumer will have their own queue binded to the exchange.
# channel.queue_declare(queue='hello')

# Declare the exchange
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "Hello, This is producer broadcasting a message to all the consumers"

# We no longer need to specify the queue name, as we are sending the message to all the queues binded to the exchange
channel.basic_publish(exchange='pubsub', routing_key='', body=message)

print(f" [x] Sent {message}")

connection.close()

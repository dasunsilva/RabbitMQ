import pika 
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" Consumer1 Received {body}" )
    
connectionPara = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connectionPara)

channel = connection.channel()

channel.exchange_declare(exchange = 'pubsub', exchange_type = ExchangeType.fanout)

# This will let the server chose the random queue name and when the consumer connection closed the queue will be deleted because of Exclusive = True
queue = channel.queue_declare(queue = '', exclusive = True)

# Bind the queue to the exchange
channel.queue_bind(exchange = 'pubsub', queue = queue.method.queue)

channel.basic_consume(queue = queue.method.queue, on_message_callback = callback, auto_ack = True)

print('Waiting for messages.')

channel.start_consuming()

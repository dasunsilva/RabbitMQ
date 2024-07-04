import consumer
from pika.exchange_type import ExchangeType
import time

exchange_name = "deviceDataExchange"
message_receiver = consumer.getMessageReceiver()
message_receiver.declare_exchange(exchange_name= exchange_name, exchange_type=ExchangeType.topic)

# Define the routing key
routing_key = '#.smoke'
queue = message_receiver.queue_bind(exchange=exchange_name, routing_key = routing_key)

# Consume the message that was sent.
message_receiver.consume_messages(queue=queue)
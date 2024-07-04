import publisher
from pika.exchange_type import ExchangeType

message_sender = publisher.getMessageSender()

floor_id = "floor1"
sensor_type = "temperature"

#Declare an exchnage
exchange_name = "deviceDataExchange"
message_sender.declare_exchange(exchange_name= exchange_name, exchange_type=ExchangeType.topic)

message = "Hello, This is producer 1 broadcasting a message to all the consumers"
routing_key = f"{floor_id}.{sensor_type}"
message_sender.send_message(exchange=exchange_name, routing_key=routing_key, body=message)

message_sender.close()
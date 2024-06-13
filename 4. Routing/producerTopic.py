import pika
from pika.exchange_type import ExchangeType

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here

connection = pika.BlockingConnection(connectionParameters) 

channel = connection.channel()

# No need to declare quesue becase queue is bound to the consumer
# channel.queue_declare(queue='testQueue')

channel.exchange_declare(exchange='routingTopic', exchange_type=ExchangeType.topic)

messageOfUserPurchaseEU = "User From Europe Purchased"
messageOfBusinessOrder = "European Business Ordered"
messageOfUserPurchaseUSA = "User From USA Purchased"

channel.basic_publish(exchange='routingTopic', routing_key='user.europe.purchase', body=messageOfUserPurchaseEU)
channel.basic_publish(exchange='routingTopic', routing_key='business.europe.order', body=messageOfBusinessOrder)
channel.basic_publish(exchange='routingTopic', routing_key='user.usa.purchase', body=messageOfUserPurchaseUSA)

print("Messages sent")

connection.close()


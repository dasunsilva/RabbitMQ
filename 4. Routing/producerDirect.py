import pika
from pika.exchange_type import ExchangeType

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here

connection = pika.BlockingConnection(connectionParameters) 

channel = connection.channel()

# No need to declare quesue becase queue is bound to the consumer
# channel.queue_declare(queue='testQueue')

channel.exchange_declare(exchange='routingDirect', exchange_type=ExchangeType.direct)

messageToPurchaseConsumer = "Hello from Producer to Purchase Consumer"
messageToAnalyticConsumer = "Hello from Producer to Analytic Consumer"
messageToBothConsumers = "Hello from Producer to Both Consumers"

channel.basic_publish(exchange='routingDirect', routing_key='payment', body=messageToPurchaseConsumer)
channel.basic_publish(exchange='routingDirect', routing_key='analytic', body=messageToAnalyticConsumer)
channel.basic_publish(exchange='routingDirect', routing_key='all', body=messageToBothConsumers)

print("Messages sent")

connection.close()


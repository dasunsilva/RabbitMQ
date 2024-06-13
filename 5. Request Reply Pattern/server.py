import pika
import uuid

# Generate a reply when the server receives a request
def callbackReq(ch, method, properties, body):
    print("Received Request: ", body, " with id: ", properties.correlation_id)
    ch.basic_publish(exchange='', routing_key=properties.reply_to, 
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id), 
                     body=f"Reply to: {body} from server with id: {properties.correlation_id}")

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here

connection = pika.BlockingConnection(connectionParameters)

channel = connection.channel()

# Define the reqruest queue
channel.queue_declare(queue = 'requestQueue')

# Consumes messages from the reply queue
channel.basic_consume(queue='requestQueue', on_message_callback=callbackReq, auto_ack=True)

print("Waiting for messages. To exit press Ctrl+C")

channel.start_consuming()

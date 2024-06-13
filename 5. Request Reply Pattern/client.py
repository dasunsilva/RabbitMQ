import pika
import uuid

def callbackReply(ch, method, properties, body):
    print("Received Reply: ", body, " with id: ", properties.correlation_id)

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here

connection = pika.BlockingConnection(connectionParameters)

channel = connection.channel()

# Define the reply queue
reply_queue = channel.queue_declare(queue='', exclusive=True)

# Consumes messages from the reply queue
channel.basic_consume(queue=reply_queue.method.queue, on_message_callback=callbackReply, auto_ack=True)

# Defines the request queue
channel.queue_declare(queue = 'requestQueue')

message = "Can I get a reply?"

# To generate a random id
corr_id = str(uuid.uuid4())

print(f"Sending request with id: {corr_id}")

# Publish a message to the server
channel.basic_publish(
                        exchange='', 
                        routing_key='requestQueue',
                        properties= pika.BasicProperties(
                            reply_to = reply_queue.method.queue,
                            correlation_id = corr_id
                        ),
                        body=message
                    )

print("Waiting for messages. To exit press Ctrl+C")

channel.start_consuming()

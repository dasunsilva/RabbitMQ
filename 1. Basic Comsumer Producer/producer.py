import pika

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here
connection = pika.BlockingConnection(connectionParameters) 

channel = connection.channel()

channel.queue_declare(queue='testQueue')
message = "Hello from Producer"
channel.basic_publish(exchange='', routing_key='testQueue', body=message)
print("Message sent: ", message)

connection.close()


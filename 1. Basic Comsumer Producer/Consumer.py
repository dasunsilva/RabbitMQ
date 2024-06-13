import pika

def callback(ch, method, properties, body):
    print("Received: ", body)

connectionParameters = pika.ConnectionParameters('localhost') # We can add IP address of the RabbitMQ server here

connection = pika.BlockingConnection(connectionParameters)

channel = connection.channel()

channel.queue_declare(queue='testQueue')

channel.basic_consume(queue='testQueue', on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit press Ctrl+C")

channel.start_consuming()

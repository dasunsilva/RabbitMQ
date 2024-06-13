import pika
import time
import random

def callback(ch, method, properties, body):
    timeNeed = random.randint(1,5)
    print(" [x] Received %r and this will take %d seconds to process" %(body,timeNeed))
    time.sleep(timeNeed)
    print(" [x] Done")
    channel.basic_ack(delivery_tag = method.delivery_tag) # Here the message will be acknowledged after it is processed

connectionPara = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connectionPara)

channel = connection.channel() 

channel.queue_declare(queue='hello') 

channel.basic_qos(prefetch_count=1) # This will make sure that the consumer will only receive one message at a time

channel.basic_consume(queue='hello', on_message_callback=callback) # Removed auto_ack=True because we want to make sure that the message is processed before it is removed from the queue

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()   

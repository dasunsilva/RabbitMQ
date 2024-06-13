import pika
import time
import random
connectionPara = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connectionPara)

channel = connection.channel()

channel.queue_declare(queue='hello')

index = 1; 

while(True):
    # This will generate a new message every 1 to 3 seconds
    
    timeRandom = random.randint(1,3)
    
    # message = f"Hello This is message {index}!"
    message = f"{index}!"

    channel.basic_publish(exchange='', routing_key='hello', body=message)

    print(f"Sent {message}")
    
    index+=1   
    
    time.sleep(timeRandom)  



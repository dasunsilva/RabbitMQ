from basicClient import BasicPikaClient
import cred
import json

def getMessageReceiver():
    return BasicMessageReceiver(
        f"{cred.broker_id}",
        f"{cred.user_name}",
        f"{cred.password}",
        f"{cred.region}"
    )
    
class BasicMessageReceiver(BasicPikaClient):
    
    def consume_messages(self, queue):
        def callback(ch, method, properties, body):
            message = body.decode('utf-8')
            json_message = json.loads(message)
            print(json.dumps(json_message, indent=4))

        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

        print('Waiting for messages.')
        self.channel.start_consuming()
                
    
    def declare_exchange(self, exchange_name, exchange_type):
        print(f"Trying to declare exchange({exchange_name})...")
        self.channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

    def queue_bind(self,exchange, routing_key):
        queue = self.channel.queue_declare(queue = '', exclusive = True)
        self.channel.queue_bind(exchange = exchange, queue = queue.method.queue, routing_key=routing_key)
        return queue.method.queue
        
    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            # print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body
        else:
            # print('No message returned')
            return None, None, None

    def close(self):
        self.channel.close()
        self.connection.close()


   
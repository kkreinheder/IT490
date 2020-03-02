import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='0.0.0.0'))
channel = connection.channel()

#Make sure queue exsist, does not recreate a new queue. 
channel.queue_declare(queue='hello')

#print message on screen, called by Pika 
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
#Assigns callback function to "hello" queue
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

#continous loop to check back for data
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
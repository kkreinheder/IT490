import pika

#Connecting to localhost (batools db 0.0.0.0) 
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0'))

#Create connection object named channel to initiate connection 
channel = connection.channel()

#Naming the queue "hello" 
channel.queue_declare(queue='hello')


#Sends basic message to queue, route_key = queue name 
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

#Should print if successfull
print(" [x] Sent 'Hello World!'")

#Always close connection
connection.close()
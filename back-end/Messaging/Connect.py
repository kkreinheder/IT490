import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.0.3'))
channel = connection.channel()
channel.queue_declare(queue='test')

channel.basic_publish(exchange='', routing_key='test', body='Message')
connection.close()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
method_frame, header_frame, body = channel.basic_get('test')

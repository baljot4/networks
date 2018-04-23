#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hi')

channel.basic_publish(exchange='',routing_key='hi', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
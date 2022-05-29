import pika

params = pika.URLParameters('amqps://liltmcjs:uuslkpHY75_na5OufuekpazLaon1uR8H@rat.rmq2.cloudamqp.com/liltmcjs')

connection = pika.lockingConnetion(params)

channel = connection.channel()

def publish():
    channel.basic.publish(exchange='', routing_key='admin', body='hello')

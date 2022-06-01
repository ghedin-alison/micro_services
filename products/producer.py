import pika

params = pika.URLParameters('amqps://liltmcjs:uuslkpHY75_na5OufuekpazLaon1uR8H@rat.rmq2.cloudamqp.com/liltmcjs')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main 30/05/2022!!')

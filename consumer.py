import pika

params = pika.URLParameters('amqps://liltmcjs:uuslkpHY75_na5OufuekpazLaon1uR8H@rat.rmq2.cloudamqp.com/liltmcjs')

connection = pika.lockingConnetion(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback='callback')

print('Start consuming..')

channel.start_consuming()

channel.close()
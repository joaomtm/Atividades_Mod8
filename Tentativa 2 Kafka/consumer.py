from confluent_kafka import Consumer, KafkaException

conf = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'meu-grupo',  
    'auto.offset.reset': 'earliest'  
}

consumer = Consumer(conf)

S
consumer.subscribe(['meu-topico'])

try:
    while True:
        msg = consumer.poll(1.0)  

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
     
                continue
            else:
                print('Erro ao consumir mensagem: {}'.format(msg.error())) 
                break

        
        mensagem = msg.value().decode('utf-8')
        print('Mensagem recebida: {}'.format(mensagem))  

except KeyboardInterrupt:
    pass

finally:
    consumer.close()


from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092',  
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print('Erro ao entregar a mensagem: {}'.format(err))
    else:
        print('Mensagem entregue ao tópico: {}'.format(msg.topic()))


producer.produce('meu-topico', key='chave-1', value='Ao despertar de sonhos agitados certa manhã, em sua cama, Gregor viu-se transformado em um inseto monstruoso.', callback=delivery_report)

producer.flush()

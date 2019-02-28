from kafka import KafkaConsumer
from json import loads
consumer = KafkaConsumer('naimish', bootstrap_servers=['localhost:9092'], value_deserializer=lambda x:loads(x.decode('utf-8')))
for message in consumer:
    message = message.value
    print('{}'.format(message))

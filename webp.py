import requests as rq
import json
from kafka import KafkaProducer
from time import sleep
req = rq.get('https://jsonplaceholder.typicode.com/todos')
print(req.status_code)
data = json.dumps(req.json())
print(data)
print(req.text)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))
for e in range(5):
    producer.send('naimish',value={e:data})
    sleep(10)

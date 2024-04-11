from time import sleep
from json import dumps
from kafka import KafkaProducer

kafka_topic_name = 'demo-topic' 
kafka_bootstrap_servers = '10.224.0.7.kafka-controller-headless.kafka.svc.cluster.local:9092,10.224.0.14.kafka-controller-headless.kafka.svc.cluster.local:9092,10.224.0.128.kafka-controller-headless.kafka.svc.cluster.local:9092'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,value_serializer=lambda x: dumps(x).encode('utf-8')) 

# Generate sample data and send to the topic
for i in range(100):
    data = {'number' : i}
    print(f"Sending message: {data}")
    producer.send(kafka_topic_name, value=data)
    sleep(5)  # Send a message every 5 seconds

producer.flush()  # Ensure all queued messages are delivered

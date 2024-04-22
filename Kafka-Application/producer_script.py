from time import sleep
from json import dumps
from kafka import KafkaProducer

kafka_topic_name = 'my-topic' 
kafka_bootstrap_servers = 'my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092,my-cluster-kafka-1.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092,my-cluster-kafka-2.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092'
# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,value_serializer=lambda x: dumps(x).encode('utf-8')) 

# Generate sample data and send to the topic
for i in range(100):
    data = {'number' : i}
    print(f"Sending message: {data}")
    producer.send(kafka_topic_name, value=data)
    sleep(5)  # Send a message every 5 seconds

producer.flush()  # Ensure all queued messages are delivered

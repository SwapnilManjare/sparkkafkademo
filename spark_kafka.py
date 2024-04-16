#!/usr/bin/python3

import os
import time
from pyspark.sql import SparkSession
from pyspark.sql.utils import IllegalArgumentException
from kafka import KafkaAdminClient, KafkaConsumer, TopicPartition

kafka_brokers = os.environ.get('KAFKA_BROKERS', 'kafka-controller-0.kafka-controller-headless.kafka.svc.cluster.local:9092,kafka-controller-1.kafka-controller-headless.kafka.svc.cluster.local:9092,kafka-controller-2.kafka-controller-headless.kafka.svc.cluster.local:9092')
kafka_topic = os.environ.get('KAFKA_TOPIC', 'demo-topic')


def create_kafka_topic(topic_name, brokers):
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=brokers)
        topic_list = []
        topic_list.append(TopicPartition(topic_name, 1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except Exception as e:
        print(f"Error creating topic {topic_name}: {e}")

create_kafka_topic(kafka_topic, kafka_brokers)

spark = SparkSession \
    .builder \
    .appName("SparkKafkaDemo") \
    .config("spark.kafka.bootstrap.servers", kafka_brokers) \
    .config("spark.kafka.sasl.jaas.config", 'org.apache.kafka.common.security.plain.PlainLoginModule required username="controller_user" password="VfrVZw9Jb9%";') \
    .config("spark.kafka.security.protocol", "SASL_PLAINTEXT") \
    .config("spark.kafka.security.inter.broker.protocol", "SASL_PLAINTEXT") \
    .config("spark.kafka.sasl.mechanism", "PLAIN") \
    .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_brokers) \
    .option("subscribe", kafka_topic) \
    .load()

# Perform basic word count-like logic
words = df.select(explode(split(df.value.cast("string"), " ")).alias("word"))
word_counts = words.groupBy("word").count()

# Start streaming to console (replace with your desired sink)
query = word_counts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

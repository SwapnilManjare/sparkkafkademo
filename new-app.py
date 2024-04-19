from kafka import KafkaProducer
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# Function to produce messages to Kafka
def produce_messages(topic, message):
    producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092')
    producer.send(topic, message.encode('utf-8'))
    producer.flush()
    producer.close()

# Function to consume messages from Kafka using Spark
def consume_messages(topic):
    spark = SparkSession.builder \
        .appName("KafkaSparkIntegration") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # Define Kafka Consumer properties
    kafka_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092ss") \
        .option("subscribe", topic) \
        .load()

    # Convert the value column to string
    kafka_df = kafka_df.selectExpr("CAST(value AS STRING)")

    # Split the lines into words
    words = kafka_df.select(
        explode(split(kafka_df.value, " ")).alias("word")
    )

    # Start running the query that prints the running counts to the console
    query = words \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    topic = "my-topic"

    # Producing a test message to Kafka
    test_message = "Hello from Kafka!"
    produce_messages(topic, test_message)

    # Consuming messages from Kafka using Spark
    consume_messages(topic)
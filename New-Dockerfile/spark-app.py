from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkIntegration") \
    .getOrCreate()

# Define the Kafka topic to subscribe to
kafka_topic_name = "my-topic"

# Define the Kafka broker(s)
kafka_bootstrap_servers = "my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092"

# Define the schema for the incoming data
schema = StructType([
    StructField("number", IntegerType())
])

# Create a DataFrame representing the stream of input lines from Kafka
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic_name) \
    .load()

# Convert the value column to string and then to JSON format based on the defined schema
parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("data")) \
    .select("data.*")

# Define any processing logic you want to apply to the data
# For example, you can print the incoming numbers
query = parsed_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Start the streaming query
query.awaitTermination()

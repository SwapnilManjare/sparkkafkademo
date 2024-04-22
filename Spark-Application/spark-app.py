import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.2.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 pyspark-shell'

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkStreamingExample") \
    .getOrCreate()

# Define the schema for the incoming Kafka messages
schema = StructType() \
    .add("number", IntegerType())

# Define the Kafka topic to subscribe to
kafka_topic_name = "my-topic"

# Define the Kafka bootstrap servers
kafka_bootstrap_servers = "my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092"

# # Define the Kafka source configuration
# kafka_source_options = {
#     "kafka.bootstrap.servers": kafka_bootstrap_servers,
#     "subscribe": kafka_topic_name,
#     "startingOffsets": "earliest"
# }

# Read data from Kafka into a DataFrame
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092") \
    .option("subscribe", "my-topic") \
#    .options(**kafka_source_options) \
    .load()

# Deserialize the value column from JSON format
parsed_df = kafka_df \
    .selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Perform basic operations (e.g., count, aggregation)
result_df = parsed_df.groupBy().avg("number")

# Write the result to the console
query = result_df \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Wait for the query to terminate
query.awaitTermination()

# Stop the SparkSession
spark.stop()

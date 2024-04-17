#!/bin/bash
python3 producer_script.py
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 spark_kafka.py

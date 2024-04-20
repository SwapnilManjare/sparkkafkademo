FROM apache/spark:latest

WORKDIR /app

#COPY requirements.txt /app
COPY spark-app.py /app/
RUN pip3 install pyspark findspark kafka-python 
#RUN pip3 install -r requirements.txt

RUN chmod +x /app/spark-app.py

ENV KAFKA_BROKERS='my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092'
ENV KAFKA_TOPIC='my-topic'
CMD [ "python3", "/app/spark-app.py" ]
#CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1", "/app/spark_kafka.py"]
#CMD ["bash", "startup.sh"]
FROM debian:buster-slim 

WORKDIR /app

# Install Java and Python
RUN apt-get update && apt-get install -y default-jdk python3 python3-pip procps

COPY requirements.txt /app
COPY spark_kafka.py producer_script.py startup.sh spark-app.py /app/
RUN pip3 install pyspark findspark kafka-python 
#RUN pip3 install -r requirements.txt
RUN export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
RUN export PATH=$PATH:$JAVA_HOME/bin
RUN chmod +x /app/spark_kafka.py 
RUN chmod +x /app/spark-app.py

ENV KAFKA_BROKERS='my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092'
ENV KAFKA_TOPIC='my-topic'
CMD [ "python3", "/app/spark_kafka.py" ]
#CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1", "/app/spark_kafka.py"]
#CMD ["bash", "startup.sh"]

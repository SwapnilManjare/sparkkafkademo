FROM debian:buster-slim 

WORKDIR /app

# Install Java and Python
RUN apt-get update && apt-get install -y default-jdk python3 python3-pip procps

COPY requirements.txt /app
COPY spark_kafka.py producer_script.py startup.sh /app/
RUN pip3 install pyspark findspark kafka-python 
#RUN pip3 install -r requirements.txt
RUN export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
RUN export PATH=$PATH:$JAVA_HOME/bin
RUN chmod +x /app/spark_kafka.py 

ENV KAFKA_BROKERS='kafka-controller-0.kafka-controller-headless.sparkdemo.svc.cluster.local:9092,kafka-controller-1.kafka-controller-headless.sparkdemo.svc.cluster.local:9092,kafka-controller-2.kafka-controller-headless.sparkdemo.svc.cluster.local:9092'
ENV KAFKA_TOPIC=demo-topic
#CMD [ "python3", "/app/spark_kafka.py" ]
#CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1", "/app/spark_kafka.py"]
CMD ["bash", "startup.sh"]


#FROM python:3.8
#WORKDIR /app
#COPY requirements.txt ./
#RUN pip install -r requirements.txt
#COPY spark_kafka.py ./
#ENV KAFKA_BROKERS='10.224.0.7.kafka-controller-headless.kafka.svc.cluster.local:9092,10.224.0.14.kafka-controller-headless.kafka.svc.cluster.local:9092,10.224.0.128.kafka-controller-headless.kafka.svc.cluster.local:9092'
#ENV KAFKA_TOPIC=demo-topic
#CMD [ "python", "spark_kafka.py" ]

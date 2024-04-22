FROM debian:buster-slim 

WORKDIR /app

RUN apt-get update && apt-get install -y default-jdk python3 python3-pip procps

COPY requirements.txt /app

COPY producer_script.py startup.sh /app/

RUN pip3 install pyspark findspark kafka-python 

RUN export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN export PATH=$PATH:$JAVA_HOME/bin

RUN chmod +x /app/producer_script.py

ENV KAFKA_BROKERS='my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092'

ENV KAFKA_TOPIC='my-topic'

#CMD [ "python3", "/app/spark_kafka.py" ]

CMD ["bash", "startup.sh"]

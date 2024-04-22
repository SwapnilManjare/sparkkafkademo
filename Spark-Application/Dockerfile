FROM apache/spark:3.5.1-python3

ARG spark_uid=185

COPY sampleapp.py /opt/spark/examples/src/main/python

COPY spark-sql-kafka-0-10_2.12-3.1.1.jar /opt/spark/examples/src/main/python

COPY spark-streaming-kafka-0-10_2.12-3.5.1.jar /opt/spark/examples/src/main/python

USER root

RUN pip3 install findspark kafka-python

USER ${spark_uid}
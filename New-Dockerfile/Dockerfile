FROM apache/spark:3.5.1-python3

COPY spark-app.py /opt/spark/examples/src/main/python

COPY sampleapp.py /opt/spark/examples/src/main/python

# COPY spark-streaming-kafka-0-10_2.12-3.5.1.jar /opt/spark/examples/src/main/python

USER root

RUN pip3 install findspark kafka-python

USER spark
#RUN chmod +x /opt/spark/examples/src/main/python/spark-application.yaml
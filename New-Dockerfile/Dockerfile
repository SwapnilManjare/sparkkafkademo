FROM apache/spark:3.5.1-python3

ARG spark_uid=185

COPY spark-app.py /opt/spark/examples/src/main/python

COPY sampleapp.py /opt/spark/examples/src/main/python

COPY spark-sql-kafka-0-10_2.12-3.1.1.jar /opt/spark/examples/src/main/python

COPY spark-streaming-kafka-0-10_2.12-3.5.1.jar /opt/spark/examples/src/main/python

USER root

RUN pip3 install findspark kafka-python

USER ${spark_uid}
#RUN chmod +x /opt/spark/examples/src/main/python/spark-application.yaml











# FROM apache/spark-py:v3.3.0

# ARG spark_uid=185

# COPY spark-app.py /opt/spark/examples/src/main/python

# COPY sampleapp.py /opt/spark/examples/src/main/python

# COPY spark-sql-kafka-0-10_2.12-3.1.1.jar /opt/spark/examples/src/main/python

# COPY spark-streaming-kafka-0-10_2.12-3.5.1.jar /opt/spark/examples/src/main/python

# USER 0

# RUN pip3 install findspark kafka-python pycurl

# RUN chown ${spark_uid} -R /opt/spark

# #RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.1.1/spark-sql-kafka-0-10_2.12-3.1.1.jar --output /opt/spark/jars/spark-sql-kafka-0-10_2.12-3.1.1.jar

# USER ${spark_uid}
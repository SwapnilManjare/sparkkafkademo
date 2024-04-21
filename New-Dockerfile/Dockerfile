FROM apache/spark:3.5.1-python3

COPY spark-app.py /opt/spark/examples/src/main/python

ENV PIP_CACHE_DIR /tmp/pip-cache

RUN pip3 install findspark kafka-python
#RUN chmod +x /opt/spark/examples/src/main/python/spark-application.yaml
import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__=="__main__":

    sc=SparkContext(appName="Kafka Spark Demo")

    ssc=StreamingContext(sc,60)

    message=KafkaUtils.createDirectStream(ssc,topics=['my-topic'],kafkaParams= {"metadata.broker.list":"my-cluster-kafka-0.my-cluster-kafka-brokers.sparkdemo02.svc.cluster.local:9092"})

    words=message.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))

    wordcounts=words.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)

    wordcount.pprint()

    ssc.start()
    ssc.awaitTermination()
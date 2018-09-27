from kafka import KafkaConsumer

#connect to Kafka server and pass the topic we want to consume
consumer = KafkaConsumer('my-topic', bootstrap_servers = ['192.168.1.201:9092', '192.168.1.202:9092', '192.168.1.203:9092'])

for msg in consumer:
    print(msg)
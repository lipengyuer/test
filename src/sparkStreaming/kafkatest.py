from kafka import SimpleProducer, KafkaClient
from kafka import KafkaProducer
import time
print("asd")
producer = KafkaProducer(bootstrap_servers = ['192.168.1.201:9092', '192.168.1.202:9092', '192.168.1.203:9092'])
# Assign a topic
topic = 'my-topic'
print("asd")
def test():
    print('begin')
    n = 1
    while (n<=100):
        print(n)
        producer.send(topic, str(n))
        print ("send" + str(n))
        n += 1
        time.sleep(0.5)
    print('done')

if __name__ == '__main__':
    test()
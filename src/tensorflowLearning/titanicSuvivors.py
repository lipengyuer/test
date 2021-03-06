import tensorflow as tf
import pandas as pd
from sklearn import preprocessing
import numpy as np
def preprocessingTrainData(data):
    #保留几个字段，发你别是船舱级别，性别，年龄，船上同辈亲戚数，船上父母子女数，票价，舱位，上传港口
    label = data["Survived"].values.reshape(len(data),1)
    data = data[[ 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',"Embarked"]]
    data['p1'] = np.array(data["Pclass"] == 1).astype(np.int32)
    data['p2'] = np.array(data["Pclass"] == 2).astype(np.int32)
    data['p3'] = np.array(data["Pclass"] == 3).astype(np.int32)
    data['male'] = np.array(data['Sex']=='male').astype(np.int32)
    data['female'] = np.array(data['Sex'] == 'female').astype(np.int32)
    data['es'] = np.array(data["Embarked"] == "S").astype(np.int32)
    data['ec'] = np.array(data["Embarked"] == "C").astype(np.int32)
    data['eq'] = np.array(data["Embarked"] == "Q").astype(np.int32)
    data["Age"] = data["Age"]/100
    data["Fare"] = data["Fare"]/np.max(data["Fare"])
    data = data.fillna(data.mean())
    return label, data.drop(["Pclass","Sex","Embarked"], axis=1).values

trainData = pd.read_csv(r"C:\Users\Administrator\Desktop\自然语言理解学习\train.csv")
testData = pd.read_csv(r"C:\Users\Administrator\Desktop\自然语言理解学习\test.csv")

trainLabel, trainData = preprocessingTrainData(trainData)
print(np.shape(trainLabel),np.shape(trainData))
#print(trainData.columns)
featureNum = len(trainData[0, :])

x = tf.placeholder("float", shape=[None, featureNum])
y = tf.placeholder("float", shape=[None, 1])

weight = tf.Variable(tf.random_normal([featureNum,1]))
bias = tf.Variable(tf.random_normal([1]))

output =tf.sigmoid( tf.matmul(x,weight) + bias)
pred = tf.cast(output > 0.5, tf.float32)

loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y, logits=output))

train_step = tf.train.GradientDescentOptimizer(0.003).minimize(loss)

accuracy = tf.reduce_mean(tf.cast(tf.equal(pred, y), tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
import random
for i in range(20000):
    index = np.random.permutation(len(trainLabel))
    #print(index)
    trainDataTemp = trainData[index,:]
    trainLabelTemp = trainLabel[index,:]
    for j in range(len(index)//100 + 1):
        batch_xs = trainDataTemp[j*100:j*100+100]
        batch_ys = trainLabelTemp[j * 100:j * 100 + 100]
        #print(batch_xs)
        sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    print(i, sess.run(loss, feed_dict={x: batch_xs, y: batch_ys}),sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys}))

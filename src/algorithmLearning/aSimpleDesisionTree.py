#实现一个决策树算法，可以训练，也可以用来分类。

from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
#数据预处理。使用鸢尾花数据集。
def dataPreprocessing():
    iris = datasets.load_iris()
    inputData = iris.data
    inputData = list(map(lambda x: list(map(lambda y: int(y), x)), inputData))
    label = iris.target
    label = list(map(lambda x: int(x), label))
    xTrain, yTrain, xTest, yTest = train_test_split(inputData, label, test_size=0.2, random_state=666)
    labelNameList = iris.feature_names
    xTrain = pd.DataFrame(xTrain, columns=labelNameList)
    yTrain = pd.DataFrame(yTrain, columns=labelNameList)
    return xTrain, yTrain, xTest, yTest

def calEntropy(dataList):
    #计算一个取值序列的熵，要求列表里的元素是离散数字
    N = len(dataList) + 0.0000001
    pDict = {}
    for line in dataList:
        if line in pDict:
            pDict[line] += line / N
        else:
            pDict[line] = line / N
    result = 0
    for key in pDict:
        result -= pDict[key]*np.log(pDict[key] + 0.0000001)
    return result

def chooseBestFeature(xTrain, yTrain):
    #从当前属性中，基于信息增益挑出最好的一个属性
    totalNumOfSample = len(yTrain)
    entropyS = calEntropy(yTrain)
    featureNameList = xTrain.columns
    labelSet = set(yTrain)
    entropyOfFeatureDict = {}
    for f in featureNameList:
        data = xTrain[f]
        sampleDict = {}
        for i in range(len(data)):
            sampleDict[data[i]] = {}
            for label in labelSet:
                sampleDict[data[i]][label] = 0
        for i in range(len(data)):#统计每种属性取值下，各个类别的个数
            sampleDict[data[i]][yTrain[i]] += 1
        #计算各个属性取值的下样本的熵
        entropyOfFeature = 0#存储各个属性取值的熵
        for key in sampleDict:
            data =  sampleDict[key]
            totalNum = sum(data.values())
            anEntropy = 0
            for k in data:
                p = data[k] / totalNum
                anEntropy -= p*np.log(p + 0.0000001)
            entropyOfFeature += anEntropy*totalNum/totalNumOfSample
        entropyOfFeatureDict[f] = entropyOfFeature
    return max(entropyOfFeatureDict)

def trainTree(xTrain, yTrain):
    #训练决策树
    bestFeature = chooseBestFeature(xTrain, yTrain)
    valueSampleDict = {}
    featureNameList = list(xTrain.columns)
    featureNameList.remove(bestFeature)
    print("剩下的特征是",featureNameList)
    xTrainLeft = xTrain[featureNameList].values
    xTrainBest = xTrain[bestFeature]
    for i in range(len(xTrainBest)):
        v = xTrainBest[i]
        if v in valueSampleDict:
            valueSampleDict[v]["xTrain"].append(xTrainLeft[i])
            valueSampleDict[v]["yTrain"].append(yTrain[i])
        else:
            valueSampleDict[v] = {}
            valueSampleDict[v]["xTrain"] = [xTrainLeft[i]]
            valueSampleDict[v]["yTrain"] = [yTrain[i]]
    for k in valueSampleDict:
        valueSampleDict[k]["xTrain"] = pd.DataFrame(valueSampleDict[k]["xTrain"], columns= featureNameList)
        asd = chooseBestFeature(valueSampleDict[k]["xTrain"], valueSampleDict[k]["yTrain"])
        print("最好的裂变特征是", asd, valueSampleDict[k]["yTrain"])

if __name__ == '__main__':
    xTrain, xTest, yTrain, yTest = dataPreprocessing()
    # print(xTrain, yTrain, xTest, yTest)
    # print(calEntropy(yTrain))
    print(chooseBestFeature(xTrain, yTrain))
    trainTree(xTrain, yTrain)

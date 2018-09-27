A = [[0.3,0.3,0.4],
        [0.1,0.4,0.5],
        [0.2,0.6,0.2]]#有3种状态

PI = [0.4,0.3,0.3]#3种状态的初始概率

B = [[0.2, 0.8],
     [0.6,0.4],
     [0.5,0.5]]#有2种观察值,第1列是0的概率，第2列是1的概率

O = [1,0,1,0,1,0,1]#这是观察值序列，我们要求这个观察值序列出现的概率

#使用前向算法计算一个观察序列出现的概率
def countPOfAObservedValues(values, generPs, transPs):
    #输入是观察序列，每种状态下产生观察值的概率，以及状态的转移概率
    forwordVec = PI#前向向量，用于存储到目前为止，观察序列片段出现的概率

    #计算出现第一个观察值的情况，对应各种状态的概率
    value = values[0]
    for j in range(len(forwordVec)):
        print("初始状态概率和观察值出现的概率是",forwordVec[j], generPs[j][value] )
        forwordVec[j] *= generPs[j][value]#初始出现这个状态的概率，
        # 乘以这个状态下出现当前观察值的概率
    print("第一个观察值出现的概率是", forwordVec)
    #开始计算之后的部分
    for i in range(1, len(values)):
        value = values[i]
        print("这是第几个观察值？ ", i, '观察值是', value)
        import copy
        tempVec = copy.deepcopy(forwordVec)
        for j in range(len(forwordVec)):
            pTemp = 0
            for jj in range(len(forwordVec)):
                p = forwordVec[jj]*transPs[jj][j]
                print(p, "之前的状态是Q", jj+1, "当前的状态是Q", j+1,"转移概率是", transPs[jj][j])
                #print("之前的序列出现的概率是", forwordVec)
                pTemp += p
            tempVec[j] = pTemp*generPs[j][value]
            print("到达当前状态", j+1 ,"并且产生当前观察值", value,"的概率是",tempVec[j] )
        forwordVec = list(tempVec)
        print("出现当前序列是", values[:i+1], "概率是", forwordVec)
    print(sum(forwordVec), forwordVec)



def getBestRouteViterbi(init_stat, values, generPs, transPs):
    #停止条件

    #继续递归

    pass
if __name__ == '__main__':
    countPOfAObservedValues(O, B, A)






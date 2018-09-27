import numpy as np
from itertools import permutations

def ifPrime(x):
    for i in range(2,int(np.sqrt(x))):
        if x % i == 0:
            return False
    return True

def ifPrimeSimple(x, primeSet):
    if x in primeSet:
        return True
    else:
        return False

def ifRemarkable(numList, primeSet):
    numList = map(lambda x: str(x), numList)
    numList = list(numList)
    coms = permutations(numList ,2)
    for com in coms:
        s = int(''.join(com))
       # print(s)
        if ifPrimeSimple(s, primeSet)==False:
            return False
    return True

def generatePairs(data , primeSet):
    coms = permutations(data, 2)
    res = []
    count = 0
    for com in coms:
        count += 1
        if count%100000 == 0:
            print(count)
        if com[0] == com[1]:
            continue
        com = com[0] | com[1]
        if ifRemarkable(com, primeSet):
            #print(com)
            res.append(com)
    return res

if __name__ == '__main__':
    primeList = []
    primeSet = set({})
    for i in range(3,1000000):
        if ifPrime(i):
            primeSet.add(i)

    for i in range(3,5000):
        if ifPrime(i):
            primeList.append(set({i}))
    print(primeSet)
    print("这个区间内的素数数量为", len(primeList))
    res1 = generatePairs(primeList, primeSet)
    print(len(res1), res1)
    res2 = generatePairs(res1, primeSet)
    print(len(res2), res2)
    res3 = generatePairs(res2, primeSet)
    print(len(res3), res3)
    res4 = generatePairs(res3, primeSet)
    print(len(res4), res4)

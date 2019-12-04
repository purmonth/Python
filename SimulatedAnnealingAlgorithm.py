import numpy as np
import matplotlib.pyplot as plt 
import pdb
import csv
import pandas as pd

"旅行商問題 ( TSP , Traveling Salesman Problem )"
##在這裡設置變數
## T_{k+1} = alpha * T_k方式更新溫度
## t = (最低溫，最高溫)
## markovlen 每個溫度下迭代的次數
def initpara():
    alpha = 0.99
    t = (1,100)
    markovlen = 1000

    return alpha,t,markovlen

df=pd.read_csv('gr17_d.csv', sep=',',header=None)
print(df.values)


num = 17

solutionnew = np.arange(num)
solutioncurrent = solutionnew.copy()
valuecurrent =99000  
solutionbest = solutionnew.copy()
valuebest = 99000 

alpha,t2,markovlen = initpara()
t = t2[1] ## t 最高溫

result = [] #記錄迭代過程中的最優解
while t > t2[0]:
    for i in np.arange(markovlen):
        if np.random.rand() > 0.5:
            while True:
                loc1 = np.int(np.ceil(np.random.rand()*(num-1)))
                loc2 = np.int(np.ceil(np.random.rand()*(num-1)))
                if loc1 != loc2:
                    break
            solutionnew[loc1],solutionnew[loc2] = solutionnew[loc2],solutionnew[loc1]
        else: 
            while True:
                loc1 = np.int(np.ceil(np.random.rand()*(num-1)))
                loc2 = np.int(np.ceil(np.random.rand()*(num-1))) 
                loc3 = np.int(np.ceil(np.random.rand()*(num-1)))
                if((loc1 != loc2)&(loc2 != loc3)&(loc1 != loc3)):
                    break
            if loc1 > loc2:
                loc1,loc2 = loc2,loc1
            if loc2 > loc3:
                loc2,loc3 = loc3,loc2
            if loc1 > loc2:
                loc1,loc2 = loc2,loc1
            tmplist = solutionnew[loc1:loc2].copy()
            solutionnew[loc1:loc3-loc2+1+loc1] = solutionnew[loc2:loc3+1].copy()
            solutionnew[loc3-loc2+1+loc1:loc3+1] = tmplist.copy()  
        valuenew = 0
        for i in range(num-1):
            valuenew += df.values[solutionnew[i]][solutionnew[i+1]]
        valuenew += df.values[solutionnew[0]][solutionnew[16]]
        if valuenew<valuecurrent: 
            valuecurrent = valuenew
            solutioncurrent = solutionnew.copy()
            if valuenew < valuebest:
                valuebest = valuenew
                solutionbest = solutionnew.copy()
        else:
            if np.random.rand() < np.exp(-(valuenew-valuecurrent)/t):
                valuecurrent = valuenew
                solutioncurrent = solutionnew.copy()
            else:
                solutionnew = solutioncurrent.copy()
    t = alpha*t
    result.append(valuebest)
    print (t) 
#用來顯示結果
plt.plot(np.array(result))
plt.ylabel("bestvalue")
plt.xlabel("t")
plt.show()

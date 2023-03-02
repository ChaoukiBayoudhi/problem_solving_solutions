import random
import time


class Knapsack:
    def __init__(self,P=[],W=[],n=0,capacity=0):
        self.__P = P
        self.W = W
        self.n = n
        self.capacity = capacity
        self.T = [[0 for i in range(capacity+1)] for j in range(n+1)]

    @property
    def P(self):
        return self.__P
    @P.setter
    def P(self,value):
        self.__P = value

    def fillMatrix(self):
        for i in range(1,self.n+1):
            for j in range(1,self.capacity+1):
                if self.W[i-1] > j:
                    self.T[i][j] = self.T[i-1][j]
                else:
                    self.T[i][j] = max(self.T[i-1][j],self.P[i-1]+self.T[i-1][j-self.W[i-1]])


    def solve(self):
        self.fillMatrix()
        i=self.n
        j=self.capacity
        result=[0]*self.n
        while i>0 and j>0:
            if self.T[i][j]!=self.T[i-1][j]:
                result[i-1]=1
                j-=self.W[i-1]
            i-=1
        return result
    def generateProfits(self):
        self.P=[random.randint(1,10) for i in range(self.n)]
    def generateWeights(self):
        self.W=[random.randint(1,10) for i in range(self.n)]
#Test
"""P=[1,2,5,6]
W=[2,3,4,5]
n=4
capacity=20
k=Knapsack(P,W,n,capacity)
"""
k=Knapsack()
k.n=1000
k.capacity=500
k.generateProfits()
k.generateWeights()
k.T = [[0 for i in range(k.capacity+1)] for j in range(k.n+1)]


print('The best solution is ')
t1=time.time_ns()
result=k.solve()
t2=time.time_ns()
print(result)
print('The time taken is ',(t2-t1)/1000,'microseconds')

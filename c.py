import math
import random
import numpy as np
w1 = random.uniform(0,1)
w2 = random.uniform(0,1)
b = random.uniform(0,1)
print w1,w2,b
x = [[0,0],[0,1],[1,0],[1,1]]
y = [0,1,1,0]
pred = [0,0,0,0]

def prediction(w1,w2,b) :
    for i in range(4) :
        pred[i] = x[i][0]*w1 + x[i][1]*w2 + b
#        print pred[i]

costt = [0,0,0,0]

def cost(pred) :
    cost1 = 0
    for i in range(4) :
        costt[i] = np.square(pred[i] - y[i])
        cost1+=costt[i]
#        print costt[i]
    cost1 = cost1/4
    return cost1

def change(pred,y,x) :
    dc_dw1 = 0
    dc_dw2 = 0
    dc_db = 0
    global w1,w2,b
    for j in range(100000) :
        for i in range(4) :
            dc_dw1+=   ( pred[i] - y[i] ) * x[i][0]
            dc_dw2+=   ( pred[i] - y[i] ) * x[i][1]
            dc_db+=  ( pred[i] - y[i] ) * 1
        w1 = w1 - 0.1*dc_dw1
        w2 = w2 - 0.1*dc_dw2
        b = b - 0.1*dc_db
        print w1,w2,b
        prediction(w1,w2,b)

#prediction(w1,w2)
#print (cost(pred))
change(pred,y,x)
#print (cost(pred))

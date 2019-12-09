import numpy as np
import math

input= np.zeros((4,2))
input[1,1] = 1
input[2,0] = 1
input[3,0] = 1
input[3,1] = 1

output= np.zeros((4, 1))
output[1,0]= 1
output[2,0]= 1

rhs= np.zeros((3,3))
lhs= np.zeros((3, 1))

lhs[0]= np.sum(np.multiply(input[:,0], output.T))
lhs[1]= np.sum(np.multiply(input[:,1], output.T))
lhs[2]= np.sum(output)

rhs[0,0]= np.sum(input[:,0]*input[:,0], axis= 0)
rhs[0,1]= np.sum(input[:,0]*input[:,1], axis= 0)
rhs[0,2]= np.sum(input[:,0], axis= 0)
rhs[1,1]= np.sum(input[:,1]*input[:,1], axis= 0)
rhs[1,2]= np.sum(input[:,1], axis= 0)
rhs[2,2]= 4;

param= np.dot(np.linalg.inv(rhs), lhs)

#print(param)

def predict(x_1, x_2):
    return np.dot(np.array([x_1, x_2, 1]), param)

print(predict(1,1))

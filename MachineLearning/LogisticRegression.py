import numpy as np
import matplotlib.pyplot as plt
import math as m
X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]]) # X: 5,2
y = np.array([0, 0, 0, 1, 1, 1])  #y: 1,5

m,n = X.shape # m = 5

w = 0
b = 0

g_arr = np.zeros(m)

def sigmoid(z):
    g = 1/(1+np.exp(-z))
    return g

def CostFunction(X,y,w,b):
    totalsum = 0;
    for i in range(m):
        fwb_xi = np.dot(w,X[i,:]) + b # tra ve 1 gia tri
        fwb_xi = sigmoid(fwb_xi)
        
        loss = (-y[i]*np.log(fwb_xi)) - (1-y[i])*np.log(1-fwb_xi)
        totalsum += loss
        
    return (1/m)*totalsum

def tinhdaoham(X,y,w,b):
    dj_dw_i = 0;
    dj_db_i = 0;
    dj_dw = 0
    dj_db = 0
    for i in range(m):
        fwb_xi = np.dot(w,X[i,:]) + b # tra ve 1 gia tri
        fwb_xi = sigmoid(fwb_xi)
        dj_dw_i = np.dot((fwb_xi - y[i]),X[i,:])
        dj_db_i = fwb_xi - y[i]
        dj_dw += dj_dw_i
        dj_db += dj_db_i
    dj_dw = 1/m * dj_dw
    dj_db =1/m * dj_db
    return dj_dw, dj_db

dj_dw, dj_db = tinhdaoham(X,y,w,b)
NumberOfIteration = 10000
alpha = 0.01
def GradientDescent(X,y,w,b):
    for i in range(NumberOfIteration):
        dj_dw, dj_db = tinhdaoham(X,y,w,b)
        w = w - alpha*dj_dw
        b = b - alpha*dj_db
    return w,b
w_new, b_new = GradientDescent(X,y,w,b)
print(w_new)

        
def LogisticRegression(X,y,w,b):
    for i in range(m):
        fwb_xi = w*X[i][0] + b
        fwb_xi = sigmoid(fwb_xi)
        print(fwb_xi)
    
LogisticRegression(X,y,w_new,b_new)
myidiotarray = np.array([0.17238519,0.326985,0.53123724,0.93499,0.72553311,0.32698523])
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(X[:,0], y)
ax1.plot(X[:,0],myidiotarray)
plt.show()





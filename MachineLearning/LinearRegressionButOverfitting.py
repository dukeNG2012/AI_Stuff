import numpy as np
import matplotlib.pyplot as plt
# x: 20,2
#y: 1,20
X = np.random.randint(1,8,(100,2))
y = np.random.randint(1,8,size=100)
#print(x)
w = np.array([0,0]) # with multiple feature: w1*x1^2 + w2 * x2 + b
b = 0
m = X.shape[0]; # m la so dong trong ma tran x
print(m)

def tinhdaoham(X,y,w,b): # muc dich tim ra w phu hop.
    
    total_sum_w = 0;
    total_sum_b = 0;
    for i in range(m):
        fwb = np.dot(w,X[i,:]) + b 
        #fwb = w[1]*(X[i,0])**2 + w[1]*(X[i,1]) + b
        dj_dw_i = np.dot((fwb - y[i]),X[i])
        dj_db_i = (fwb-y[i])
        total_sum_w = total_sum_w +  dj_dw_i
        total_sum_b = total_sum_b + dj_db_i
    
    total_sum_w = (1/m) * total_sum_w
    total_sum_b = (1/m) * total_sum_b
    
    return total_sum_w, total_sum_b



alpha = 0.01
w_array_length = 100


def gradientdescent(X,y,w,b):
    for i in range(w_array_length):
        dw, db = tinhdaoham(X,y,w,b) #w: (1,2)
        w = np.subtract(w,alpha*dw)
        b = b - alpha*db
        #print(w)
    w_new = w
    b_new = b
    return w_new,b_new

w_new,b_new = gradientdescent(X,y,w,b)


fwb_arr = np.zeros(m)
def LinearRegression(X,y,w_new,b_new):
    for i in range(m):
        fwb_arr[i] = np.dot(w_new,X[i,:]) + b_new
        #fwb_arr[i] = w_new[0]*(X[i,0])**2 + w_new[1]*(X[i,1]) + b_new
LinearRegression(X,y,w_new,b_new)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(X[:,0],y)
ax1.plot(X[:,0],fwb_arr)
plt.show()
    




import numpy as np
import matplotlib.pyplot as plt

x = np.array([[2104.0, 5.0, 1.0, 45.0],[1416.0,3.0,2.0,40.0],[1534.0,3.0,2.0,30.0],[852.0,2.0,1.0,36.0]]);
f = np.array([])
x1 = [2104.0, 5.0, 1.0, 45.0]
w = np.array([0.1 ,4 ,10 ,-2 ]);
b = 80
for i in range(4): # chay tu 0 - 3
    f[i] = np.dot(w,x[i]);


print(f)
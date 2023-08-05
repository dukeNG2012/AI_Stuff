import numpy as np;
import matplotlib.pyplot as plt
import math as m
# de lam van de polymal se co 2 tap thuoc tinh w
# w1 = np.array([1,2,3,4,5]);
# w2 = np.array([4,3,2,3,4]);
w1 = 100;
w2 = 200;

x1 = np.array([1,2,3,4,5,6,7,8,9,10]);
x2 = np.array([11,12,13,14,15,16,17,18,19,20]);

# y = m.sin(x1[i]);
y = [];
for i in range(10):
    y.append(m.sin(x1[i]))

#!//plt.subplot(1,2,1);
plt.plot(x1,y);
plt.plot(x2,y,'r');
plt.show();



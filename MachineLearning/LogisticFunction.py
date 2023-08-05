import matplotlib.pyplot as plt
import math as m
x = [-100,1,2,3,4,5,6,7,8,9,10]
y = []
for i in range(11):
    y.append(1/(1+(m.exp(-x[i])) ))
print(y)

plt.plot(x,y)
plt.show()
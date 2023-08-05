from sympy import *

x,y = symbols("x y")
f = 2*x + 1
g = solve(f,x)
print(g)
print(x)
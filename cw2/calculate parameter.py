import numpy as np
from scipy.linalg import solve
# plane1
a = np.array([[-89,33,46,1],[33,-26,-32,1],[-46,32,40,1],[-1,-1,1,0]])
b = np.array([-1,-1,1,0])
x1,x2,x3,x4 = solve(a,b)
print(x1,x2,x3,x4)

a1 = np.array([[5],[8]])
a2= np.array([[-5],[-1]])
a3= np.array([[6],[2]])
w= -x1* a1-x2* a2 +x3* a3
print(w)

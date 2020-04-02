import random
import numpy as np
import matplotlib.pyplot as plt




class1 =np.array ( [[5,15],[5, 8],[2, 7],[1, 9],[3, 11],[1, 10],[3, 10],[3, 8],[2, 8],[1, 6]] )
class2=np.array ( [[-10,0],[-9, 1],[-8, 1],[-5,-1],[-8, 2],[-9, -2],[-9.5, -3],[-8.5, -1],[-7, -2],[-7.5, -3]] )
class3=np.array ( [[10,0],[6, -7],[7, -1],[8, -3],[9, -6],[7.5, -6],[8, -5],[8.5, -2],[7, -2],[6, 2]])


x=class1+class2+class3
test=x/3
print(test)

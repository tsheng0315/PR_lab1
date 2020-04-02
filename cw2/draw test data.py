import random
import numpy as np
import matplotlib.pyplot as plt

class1=[]
class2=[]
class3=[]


yl = [[-12, 12], [(-12+6)/4*(-0.5)+3, (12+6)/4*(-0.5)+3]]
xl = [[(-12+6)/4, (12+6)/4], [(-12+6)/4, (12+6)/4]] 



for i in range(len(xl)):
  def function2(x):
    return (0.239+0.23*x)/ (-0.0886)
  def function3(x):
    return (-0.0145-0.261*x)/ (-0.29)
     
     
x2=np.arange(-8, 8, 0.01)
y2=function2(x2)
line2,=plt.plot(x2,y2,color='k')


x3=np.arange(-8, 8, 0.01)
y3=function3(x3)
line3,=plt.plot(x3,y3,color='b')

  
    #line1,= plt.plot([8, -6], [4, 4], color='g')
   # line2,= plt.plot([-1, 0.5], [-18, 18], color='k')
    #line3,= plt.plot([10, -2.5], [15, -20], color='b')



line1,=plt.plot([11, -11], [4, 4], color='g')

test=[[ 1.66666667,  5 ],
 [ 0.66666667 , 0.66666667],
 [ 0.33333333  ,2.33333333],
 [ 1.33333333 , 1.66666667],
 [ 1.33333333 , 2.33333333],
 [-0.16666667 , 0.66666667],
 [ 0.5     ,    0.66666667],
 [ 1,         1.66666667],
 [ 0.66666667 , 1.33333333],
 [-0.16666667 , 1.66666667]]
class1 = [[5,15],[5, 8],[2, 7],[1, 9],[3, 11],[1, 10],[3, 10],[3, 8],[2, 8],[1, 6]]
class2=[[-10,0],[-9, 1],[-8, 1],[-5,-1],[-8, 2],[-9, -2],[-9.5, -3],[-8.5, -1],[-7, -2],[-7.5, -3]]
class3= [[10,0],[6, -7],[7, -1],[8, -3],[9, -6],[7.5, -6],[8, -5],[8.5, -2],[7, -2],[6, 2]]

for n in class1:
    dot1, =plt.plot(n[0],n[1],'mx')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'rv')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'go')
for n in test:
    dot4, =plt.plot(n[0],n[1],'cx')

dot1.set_label('class 1')
dot2.set_label('class 2')
dot3.set_label('class 3')
dot4.set_label('test data')
line1.set_label('hyperplane1')
line2.set_label('hyperplane2')
line3.set_label('hyperplane3')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='lower left')
plt.title("Non-separable region")
# for n in range(500):
#     x=random.randint(-2,3)
#     y=random.randint(-10,10)
#     temp1=4*x-6
#     temp2=-0.5*x+3
#     if y>temp1 and y>temp2:
#         if [x,y] not in class1 and len(class1)<10:
#             class1.append([x,y])
#             plt.plot(x,y,'bx')
#     if y>temp1 and y<temp2 and len(class2)<10:
#         if [x,y] not in class3:
#             class2.append([x,y])
#             plt.plot(x,y,'ro')
#     if y<temp1 and y<temp2 and len(class3)<10:
#         if [x,y] not in class3:
#             class3.append([x,y])
#             plt.plot(x,y,'g*')
plt.show()
print("class1:",class1)
print("class2:",class2)
print("class3:",class3)






for n in class1:
    dot1, =plt.plot(n[0],n[1],'mx')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'rv')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'go')

dot1.set_label('class 1')
dot2.set_label('class 2')
dot3.set_label('class 3')

line,=plt.plot([11, -11], [4, 4], color='g')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.title("Class1 and Class2&3")
plt.show()





for n in class2:
    dot2, =plt.plot(n[0],n[1],'rv')
dot2.set_label('class 2')
for n in class3 :
    dot3, =plt.plot(n[0],n[1],'go')
dot3.set_label('class 3')    
for n in class1:
    dot1, =plt.plot(n[0],n[1],'mx')
dot1.set_label('class 1')

def function(x):
    return (-0.2389+0.23*x)/ (-0.0886)
     
x1=np.arange(-8, 8, 0.01)
y1=function(x1)
line4,=plt.plot(x1,y1,color='g')

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='upper left')
plt.title("Class2 and Class1&3")
plt.show()

for n in class1:
    dot1, =plt.plot(n[0],n[1],'mx')
for n in class2:
    dot2, =plt.plot(n[0],n[1],'rv')
for n in class3:
    dot3, =plt.plot(n[0],n[1],'go')
def function(x):
    return (-0.0145-0.261*x)/ (-0.29)
     
x1=np.arange(-8, 8, 0.01)
y1=function(x1)
line4,=plt.plot(x1,y1,color='g')

dot1.set_label('class 1')
dot2.set_label('class 2')
dot3.set_label('class 3')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend(loc='lower left')
plt.title(" Class3 and Class1&2")
plt.show()

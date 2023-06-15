import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

#%matplotlib inline

def plot_vect(x, b, xlim, ylim):
    '''
    function to plot two vectors, 
    x - the original vector
    b - the transformed vector
    xlim - the limit for x
    ylim - the limit for y
    '''
    plt.figure(figsize = (10, 6))
    plt.quiver(0,0,x[0],x[1],\
        color='k',angles='xy',\
        scale_units='xy',scale=1,\
        label='Original vector')
    plt.quiver(0,0,b[0],b[1],\
        color='g',angles='xy',\
        scale_units='xy',scale=1,\
        label ='Transformed vector')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
list=[]
lst2=[]
m=int(input("Enter the row:"))
n=int(input("Enter the column:"))
for i in range(0,m):
    ele = int(input())
    list.append(ele)
for j in range(0, n):
    ele = int(input())
    lst2.append(ele)


A = np.array([list,lst2])
lst = []
# number of elements as input
n = int(input(" Enter the number of eigenvectors: "))
# iterating till the range
d=[]
print("Enter the value of eigenvectors:")
for i in range(0, n):
    ele = int(input())
    d.append(ele)
    lst.append([ele])

x = np.array([lst])
b = np.dot(A, x)
vec1=int(np.linalg.det(A)+1)
vec2=int(vec1-1)
plot_vect(x,b,(0,vec1),(0,vec2))


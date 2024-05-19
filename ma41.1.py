import numpy as np
import matplotlib.pyplot as plt

def mon(n):
    y=[]
    x = []
    x_squard=[]
    y_squard=[]
    for i in range(n):
        x_=np.random.uniform(-1,1)
        y_=np.random.uniform(-1,1)
        d_square=x_**2+y_**2
        if d_square <=1:
            x.append(x_)
            y.append(y_)
        else:
            x_squard.append(x_)
            y_squard.append(y_)
    pi=4*(len(x)/(len(x_squard)+len(x)))
    return pi, x,y,x_squard,y_squard

def main():
    pi,x,y,x_squard,y_squard=mon(100000)

    plt.plot(x_squard,y_squard,'b.',markersize=1)
    plt.plot(x,y,'r.',markersize=1)
    plt.show()
main()
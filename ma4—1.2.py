import numpy as np
import matplotlib.pyplot as plt

def mon(n,d):
    points=[[np.random.uniform(-1,1) for i in range(d)] for _ in range(n)]
    inside_point=lambda point:sum(x**2 for x in point)<=1
    in_points=list(filter(inside_point,points))
    vol=d**2*len(in_points)/n
    return vol,points,inside_point,in_points 

def main():
    for d in {2,11}:
        vol,points,inside_point,in_points=mon(100000,2)
        print (vol)
main()
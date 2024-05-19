#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n): # pure python code
 if n <= 1:
 	return n
 else:
 	return fib_py(n-1) + fib_py(n-2)

@njit
def fib_nu(n): # python code with Numba
 if n <= 1:
 	return n
 else:
 	return fib_nu(n-1) + fib_nu(n-2)


def main():
    f = Person(50)
    print(f"Age: {f.getAge()}")
    print(f"Decades alive: {f.getDecades()}")

    f.setAge(51)
    print(f"Age: {f.getAge()}")
    print(f"Decades alive: {f.getDecades()}")

    # Step 4-5 (see instructions MA4) of exercise 2.2.2
    y_py = []
    y_nu = []
    y_cpp = []
    x = range(20,31) # for step 4
    # when iterating over [30, 45], comment out the fibonacci-calculations via pure python & its plotting code
    #x = range(30,46) # for step 5
    for n in x:
        print(f"n={n}")

        # Pure Python
        start = pc()
        fib_py(n)
        end = pc()
        y_py.append(end-start) # seconds for the pure Python code
        # Python using Numba
        start = pc()
        fib_nu(n)
        end = pc()
        y_nu.append(end-start) # seconds for the Python+numba code
        # C++ code
        start = pc()
        f = Person(n)
        f.fib()
        end = pc()
        y_cpp.append(end-start) # seconds for the C++ code

    # Plotting running time for each code version
    plt.figure()
    plt.plot(x, y_py, label='Pure Python', color='b')
    plt.plot(x, y_nu, label='Python+Numba', color='orange')
    plt.plot(x, y_cpp, label='C++', color='r')
    plt.ylabel('milliseconds (ms)')
    plt.xlabel('n')
    plt.title('Calculation of the fibonacci number using Python vs C++')
    plt.legend(loc='upper right')
    plt.savefig('MA4_2_Plot_n20to30.png')
    #plt.savefig('MA4_2_Plot_n30to45.png')

    # Step 6 (see instructions MA4) of exercise 2.2.2
    n = 47
    print(f"Fibonacci of n=47 with different programming langauges:")
    print(f"    Python+Numba: {fib_nu(n)}")
    print(f"    C++: {Person(n).fib()}")
""" Analysis: fib(47) with python+numba gives the right number 2971215073 while the calculation with C++ gives a wrong answer 
	with a big margin of error: -1323752223. This is most likely beacuse what is called 'integer overflow' in which the int
	datatype can hold a limited range of values. Beacuse fib() uses recursion and for fib(47) gets to a very large value, it
	is exceeding the max value that may be stored in the used datatype. I reckon that the use can be resolved by using a
	datatype with wider range of values? Maybe write 'long int' or 'long long int'
"""
if __name__ == '__main__':
	main()

# Angel Velazquez, Jordan Scott
# solve using green's function
# 1. 𝑦"+4𝑦=𝑥;𝑦(0)=𝑦′(0)=0
# 2. 𝑦"+𝑦=4; 𝑦(0)=𝑦′(0)=0

# 2 DE
# green's function, underdetermined coeff(homogeneous)
# green's function, underdetermined coeff(homogeneous)

# B
# 2 plots: homogeneous (t) and green's function
# 2 plots: homogeneous (t) and green's function

import numpy as np
import matplotlib.pyplot as plt
import cmath
from math import e

def quadratic(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    
    return sol1, sol2

# driver function
if __name__ == "__main__":
    # param for the first DE as homogeneous
    a1 = 1
    b1 = 4
    c1 = 0
    solutionsA = quadratic(a1, b1, c1)

    # param for the second DE as homogeneous
    a2 = 1
    b2 = 1
    c2 = 0
    solutionsB = quadratic(a2, b2, c2)
    
    print(solutionsA[0], solutionsA[1])
    print(solutionsB[0], solutionsB[1])

    # y = c1e^ax cos(bx) + c2e^ax sin(bx)
    y = e**(0) * np.cos(-4)
    print(y)
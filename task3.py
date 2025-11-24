
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

TEAM_NUMBER: int = 3

"""
# <base equation>
x * e(y * (x + a + 1)) + (a + 1) * e(((y * (x + a + 1)))) = x + a

# factoring out e
e**(y * (x + a + 1)) * (x + a + 1) = x + a

# factoring out (x + a)
e**(y * (x + a + 1)) = (x + a) / (x + a + 1)

# removing e by natural log
y * (x + a + 1) = log((x + a) / (x + a + 1))

# solving for y as an equation
y = log((x + a) / (x + a + 1)) / (x + a + 1)
"""

a = TEAM_NUMBER
x = np.linspace(-2 * (a + 1), 2 * (a + 1), 10_000)

# y = log((x + a) / (x + a + 1)) / (x + a + 1)
graph = np.log10((x + a) / (x + a + 1)) / (x + a + 1)

plt.plot(x, graph)

"""
Take the door on the right hand side as the one to the left has a trap to its name
"""
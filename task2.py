
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

TEAM_NUMBER: int = 3

"""
left:
lim(x -> a) a + (x + a)^100 * (-1)/(e^(x+a)^2)
exp / fact
lim = inf

right:
lim(x -> a) (e ^ (x + a)) / (x + a * e ^ (x + a))
exp / exp = 0
"""

x = np.linspace(0, -3, 10_000)
a = TEAM_NUMBER

left = a + (x + a)**100 * np.e**(-1 / (x + a)**2)

right = (np.e**(x + a)) / (x + a * np.e ** (x + a))

plt.plot(x, left, 'r-')
plt.plot(x, right, 'g-')

"""
Use the right-hand door as the left approaches inf hence it will never opens
"""
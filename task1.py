
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

TEAM_NUMBER: int = 3

"""
Real = 0
Imaginary = 2
Number of moves taken = 9
"""

InitialPosition = ((-8)*(1j**(12))*abs((math.sqrt(3)+1j)/((math.sqrt(3)-1j)**3)))
CurrentX=(InitialPosition.real)
CurrentY=(InitialPosition.imag)
CurrentPosition=(InitialPosition)
Increment = ((math.sqrt(3)+1j)/2)
xArray = []
yArray = []
NumberOfMoves = 0
while not (round(CurrentPosition.real,2)==0 and round(CurrentPosition.imag,2)==2):
    CurrentPosition*=Increment
    xArray.append(CurrentPosition.real)
    yArray.append(CurrentPosition.imag)
    NumberOfMoves+=1

print("Real =",round(CurrentPosition.real))
print("Imaginary =",round(CurrentPosition.imag))
print("Number of moves taken =",NumberOfMoves)

plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.plot(xArray,yArray)

"""
The multiplications give the following values:

Real (Horizontal) =  -1.73
Imaginary (vertical) =  -1.0

Real (Horizontal) =  -1.0
Imaginary (vertical) =  -1.73

Real (Horizontal) =  0.0
Imaginary (vertical) =  -2.0

Real (Horizontal) =  1.0
Imaginary (vertical) =  -1.73

Real (Horizontal) =  1.73
Imaginary (vertical) =  -1.0

Real (Horizontal) =  2.0
Imaginary (vertical) =  0.0

Real (Horizontal) =  1.73
Imaginary (vertical) =  1.0

Real (Horizontal) =  1.0
Imaginary (vertical) =  1.73

Real (Horizontal) =  -0.0
Imaginary (vertical) =  2.0

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~                                       ~~
~~    result at 9 repetitions!!!!!!      ~~
~~    Real = 0                           ~~
~~    Imaginary = 2                      ~~
~~                                       ~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 


these follow 2 cos x and 2 sin x where x starts at 210 and oscillates between 330 and 0
"""
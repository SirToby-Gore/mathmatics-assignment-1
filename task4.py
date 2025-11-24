
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

TEAM_NUMBER: int = 3


"""
```
S = {vect[3 2] * j, ∞} ∩ {-∞+1,3j}
Q = 3j/9 ≡j/3
```

```
p: ℘(S) ≡ {∅, {a}, {∞}, {a, ∞}}  TRUE
the intersection of S gives S={a,∞}. The power set P(S)=P({a,∞})={∅,{a},{∞},{a,∞}}. Therefore TRUE

q: s ∩ Q ∩ {+∞} ≡ {∅}  FALSE
simplifying down Q will give j/3. The union of the above 3 is not ∅

r: ¬{¬p}
r: ¬{False}
r: True
```

```
(p → q) = FALSE
FALSE → p = TRUE
TRUE → r = TRUE
```
"""

"""
Therefore the lever that will open the door is the left one
"""

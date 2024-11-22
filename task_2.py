import task_1 as const
import numpy as np
h = 100
a = 35
b = 45
v = np.sqrt(const. g* h * np.tan(b)**2) / (2* np.cos(a)**2 * (1 - np.tan(b)*np.tan(a)))
print(v)

T = 200
o = 300
import numpy as np
from task_1 import k
from task_1 import e 
from task_1 import ht
N = (2 * ht * e**( ( -o) / ( k * T))) * (o**( T / 2)) / (np.sqrt(const.pi) * ( k / o) ** (3/2))
print(N)
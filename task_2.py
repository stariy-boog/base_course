import numpy as np
from task_1 import G 
from task_1 import h 
from task_1 import k 
from task_1 import e 
h = 100
alpha = np.radians(45)
betta = np.radians(35)
v = np.sqrt((G*h*np.tan(betta)**2) / ( 2 * np.cos(alpha)**2 * (1 - np.tan(betta) * np.tan(alpha))))
print(v)
T = 200
ε  = 300
N = (2/np.sqrt(np.pi))*(h / k*T**3/2)*(e-ε/k*T * ε**T/2)
print(N)
from scipy.linalg import norm
import numpy as np
# from utlilities import *

A=np.asarray([[9, 9, 4, 1], [8, 8, 0, 9], [8, 0, 6, 3], [4, 3, 8, 5]])
print(norm(A, 1))
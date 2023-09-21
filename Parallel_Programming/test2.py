import numpy as np
import random

A=np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(A)
# for j in range(3):
#     print(A[:, j])
print(A[:, 0:1])

def replace():
    test_list=[-1, 1]
    random_index=random.randrange(len(test_list))
    randomint=test_list[random_index]
    print(randomint)
    return randomint

S=np.ones([4, 4], dtype="int64")
Sold=np.ones([4, 4], dtype="int64")
# print(randomint)
# comparing with Sold only now-WIP
for j in range(4):
    print(j)
    A=S[:, j]
    parallel=True
    while parallel:
        not_parallel=0
        for k in range(4):
            if ((A==Sold[:, k]).all() or (A == -Sold[:, k]).all()):
                for i in range(4):
                    A[i]=replace()
                    print(S)
            else: not_parallel+=1
        for k in range(4):            
            if k!=j:
                if ((A==S[:, k]).all() or (A == -S[:, k]).all()):
                    for i in range(4):
                        A[i]=replace()
                        print(S)
                else: not_parallel+=1
        if not_parallel!=7:
            continue
        else: parallel=False
        print("-------------------------------------------------")
print(S)
print(Sold)
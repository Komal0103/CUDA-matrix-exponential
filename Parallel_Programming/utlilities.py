import numpy as np
import random

# parallelise
def matmul(a, b, n, t):
    c=np.zeros([n, t], dtype="float64")
    for i in range(n):
        for j in range(t):
            for l in range(n):
                c[i][j]+=a[i][l]*b[l][j]
    return c

# parallelise
def sign(A, n, t):
    s=np.zeros([n, t], dtype="float64")
    for i in range(n):
        for j in range(t):
            if A[i][j]>=0:
                s[i][j]=1
            elif A[i][j]<0:
                s[i][j]=-1
    return s

def identity(n):
    I=np.zeros([n, n], dtype="float64")
    for i in range(n):
        for j in range(n):
            if i==j:
                I[i][j]=1
    return I

# parallelise
# multiply vectors of equal sizes
def vectMul(a, b, n):
    c=0
    for i in range(n):
        c+=a[i]*b[i]
    return c

# the output should be initiliased before passing to this function
# initiliase with np.zeros
def sortArray(input, output):
    temp=input.copy()
    temp.sort()
    output=np.flip(temp)
    return output

def replace(n):
    test_list=[-1/n, 1/n]
    random_index=random.randrange(len(test_list))
    randomint=test_list[random_index]
    return randomint

# to determine whether the columns are parallel or not-replace columns of A with random numbers
def parallelReplace(S, Sold, t, N, denominator, flag):
    number = 0; answer = False
    # n=0
    if id(S) == id(Sold): n=t-1
    else: n=2*t-1
    # print(n)
    for j in range(flag, t):
        # itr=0
        # print(j)
        A=S[:, j]
        parallel=True
        while parallel:
            # itr+=1
            not_parallel=0
            # when S and Sold are not the same
            if id(S) != id(Sold):
                for k in range(t):
                    # print(k)
                    if ((A==Sold[:, k]).all() or (A == -Sold[:, k]).all()):
                        number+=1
                        for i in range(N):
                            S[i][j]=replace(denominator)
                            # print(S)
                    else: not_parallel+=1
                    if number == t**2: answer = True
            # print(not_parallel)
            # the matrix is being compared with itself
            for k in range(t):            
                if k!=j:
                    if ((A==S[:, k]).all() or (A == -S[:, k]).all()):
                        # replace all elements of the column with the random elements from the list
                        for i in range(N):
                            S[i][j]=replace(denominator)
                        # print(A)
                        # print(S)
                    else: not_parallel+=1
            # print(S)
            # print(not_parallel)
            # print("--------------------")
            # if itr == 5: break
            if (not_parallel == n):
                parallel=False
            else: continue
    return S, answer
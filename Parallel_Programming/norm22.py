import numpy as np
import math
from scipy.linalg import norm

def matmul(a, b, m, n, k):
    c=np.zeros([m, k], dtype="float64")
    for i in range(m):
        for j in range(k):
            for l in range(n):
                c[i][j]+=a[i][l]*b[l][j]
    return c

def sign(A):
    s=np.zeros([4, 4], dtype="float64")
    for i in range(4):
        for j in range(4):
            if A[i][j]>=0:
                s[i][j]=1
            elif A[i][j]<0:
                s[i][j]=-1
    return s

def identity():
    I=np.zeros([4, 4], dtype="float64")
    for i in range(4):
        for j in range(4):
            if i==j:
                I[i][j]=1
    return I

# multiply vectors of equal sizes
def vectMul(a, b, n):
    c=0
    for i in range(n):
        c+=a[i]*b[i]
    return c

def sort(input, output):
    temp=input.copy()
    temp.sort()
    output=np.flip(temp)
    return output

A=np.asarray([[9, 9, 4, 1], [8, 8, 0, 9], [8, 0, 6, 3], [4, 3, 8, 5]])
t=3
X=np.asarray([[1/4, 1/4, 1/4], [1/4, 1/4, 1/4], [1/4, 1/4, 1/4], [1/4, 1/4, 1/4]])
g=np.zeros([3], dtype="float64")
h=np.zeros([4], dtype="float64")
l=np.zeros([4], dtype="float64")
norm_A=np.zeros([3], dtype="float64")
ind=np.zeros([4], dtype="float64")
while True:
    Y=matmul(A, X, 4, 4, 3)
    # print(Y)
    for j in range(3):
        norm_A[j]=norm(Y[:, j], 1)
        ind[j]=j
    g=sort(norm_A, g)
    # print(norm_A)
    print(g)
    j=np.where((norm_A==g[0])[0])
    ind_best=ind[j]
    print(ind)
    print(ind_best)
    S=sign(A)
    Z=matmul(np.transpose(A), S, 4, 4, 4)
    # print(Z)
    for i in range(4):
        h[i]=norm(Z[i, :], np.inf)
        ind[i]=i
    # print(h)
    # print(np.transpose(Z[:, int(ind_best)]))
    # print(X[:, ind_best])
    if max(h)<=vectMul(np.transpose(Z[:, int(ind_best)]), X[:, int(ind_best)], 4):
        break
    l=sort(h, l)
    # print(l)
    print(len(h))
    # TODO: reorder ind correspondingly-problem here
    i=0
    while (i<len(h)):
        count=np.count_nonzero(h==l[i])
        # print(count)
        if count>0:
            index=np.where(h==l[i])
            temp=[]
            if count>1:
                for (key, value) in list(enumerate(h)):
                    if value==l[i]:
                        temp.append(key)
                # print(temp)
                for c in range(count):
                    # print(c, i)
                    ind[i+c]=temp[c]
                i+=count
            elif count==1:
                ind[i]=index[0][0]
                i+=1
    print(ind)
    I=identity()
    for j in range(3):
        J=ind[j]
        # print(J)
        X[:, j]=I[int(J)]
    print("--------------------------------------")

print(g)
print(ind)
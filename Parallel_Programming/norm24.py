from scipy.linalg import norm
from utlilities import *
import math
import pdb

A=np.asarray([[9, 9, 4, 1], [8, 8, 0, 9], [8, 0, 6, 3], [4, 3, 8, 5]])
# t=3
itmax=4
n=A.shape[0]
# setting value of t such that only 2 iterations are required - is it needed?
t = math.ceil(n/2+1)
# print(n)
# change the input matrix
x=np.asarray([[1/n, 1/n, 1/n], [1/n, 1/n, 1/n], [1/n, 1/n, 1/n], [1/n, 1/n, 1/n]])
X, ans=parallelReplace(x, x, t, n, n, 1)
print(X)

def norm24(A, X, t, itmax, n, itr):
    ind=np.zeros([n], dtype="int64")
    S=np.zeros([n, t], dtype="int64")
    h=np.zeros([n], dtype="float64")
    l=h.copy()
    ind_hist=[]
    I=identity(n)
    estold = 0
    while True:
        itr += 1
        print("Iteration Number: ", itr)
        # pdb.set_trace()
        Y=matmul(A, X, n, t)
        print(Y)
        norm_Y=[]
        for j in range(3):
            norm_Y.append(norm(Y[:, j], 1))
            ind[j]=j
        ind_hist.extend(ind)
        est=max(*norm_Y)
        index=np.where(norm_Y==est)
        if (est>estold or itr==2):
            ind_best=ind[index]
            w=Y[:, ind_best]
        if (itr>=2 and est<=estold):
            est=estold
            v=I[:, ind_best]
            break
        estold=est
        Sold=S.copy()
        if itr>itmax:
            v=I[:, ind_best]
            break
        print(Sold)
        S=sign(Y, n, t)
        print(S)
        # If every column of S is parallel to column of Sold, break
        S, ans=parallelReplace(S, Sold, t, n, 1, 0)
        if ans == True:
            v=I[:, ind_best]
            break
        Z=matmul(np.transpose(A), S, n, t)
        for i in range(n):
            h[i]=norm(Z[i][:], np.inf)
            ind[i]=i
        if (itr>=2 and max(*h)==h[ind_best]):
            v=I[:, ind_best]
            break
        l=sortArray(h, l)
        # reorder ind correspondingly-problem here
        i=0
        while (i<len(h)):
            # counting the occurrences of the ith element in l
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
        print(h)
        print(l)
        print(ind)
        if t>1:
            if set(ind).issubset(set(ind_hist)):
                v=I[:, ind_best]
                break
            # TODO: replace ind[0:t-1] by the first t indices in ind[0:n-1] that are not in ind_hist
        for j in range(t):
            X[:, j]=I[ind[j]]
        print("**********************")
    v=I[:, ind_best]

    return est, w, v

# driver code
itr = 0
est, w, v = norm24(A, X, t, itmax, n, itr)
print(est)
print(w)
print(v)
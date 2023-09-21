import numpy as np
import random

arr=np.asarray([18, 19, 20, 84, 1, 63, 75])
arr=np.array([29, 20, 18, 18, 20])
temp=arr.copy()
temp.sort()
arr2=np.flip(temp)
# print(arr2)
ind=np.zeros([len(arr2)], dtype="int32")
# print(list(enumerate(arr2)))
i=0
while (i<len(arr)):
    count=np.count_nonzero(arr==arr2[i])
    print(count)
    if count>0:
        index=np.where(arr==arr2[i])
        # print(index[0][0])
        temp=[]
        if count>1:
            for (key, value) in list(enumerate(arr)):
                # print(key, value)
                if value==arr2[i]:
                    temp.append(key)
            # print(temp)
            for c in range(count):
                ind[i+c]=temp[c]
            i+=count
        elif count==1:
            ind[i]=index[0][0]
            i+=1
print(ind)

# find all the occurrences of an element of arr2 in arr

# selecting a random number from a list of numbers-determining whether the columns are parallel or not
# replacing columns if necessary

# print(randomint)

# def replace():
#     test_list=[-1, 1]
#     random_index=random.randrange(len(test_list))
#     randomint=test_list[random_index]
#     print(randomint)
#     return randomint

# S=np.ones([4, 4], dtype="int64")
# Sold=np.ones([4, 4], dtype="int64")
# # print(randomint)
# # comparing with Sold only now-WIP
# for j in range(4):
#     print(j)
#     parallel=True
#     while parallel:
#         not_parallel=0
#         A=S[:, j]
#         print(A)
#         if S is not Sold:
#             for k in range(4):
#                 if ((A==Sold[:, k]).all() or (A == -Sold[:, k]).all()):
#                     for i in range(4):
#                         A[i]=replace()
#                         print(S)
#                 else:
#                     not_parallel+=1
#             if not_parallel!=4:
#                 continue
#             else: parallel=False
#             print("-------------------------------------------------")
# print(S)
# print(Sold)
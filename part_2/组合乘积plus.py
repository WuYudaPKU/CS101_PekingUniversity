import time
from itertools import product
# c=time.time()
T=int(input())
S=list(map(int,input().split()))
S_new=[]
for i in S:
    if T%i==0:
        S_new.append(i)
ans=True
for permutation in product([0,1],repeat=len(S_new)):
    temp=1
    for i in range(len(permutation)):
        if permutation[i]==1:
            temp*=S_new[i]
    if temp==T:
        print("YES")
        ans=False
        break
if ans:
    print("NO")
# d=time.time()
# print(d-c)
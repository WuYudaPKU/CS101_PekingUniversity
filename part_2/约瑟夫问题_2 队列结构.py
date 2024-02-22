from collections import deque
list_nm=[]
while True:
    a=list(map(int,input().split()))
    if a!=[0,0]:
        list_nm.append(a)
    else:
        break

def king(n,m):
    index=0
    monkey=deque(i for i in range(1,n+1))
    while True:
        if len(monkey)!=1:
            if index!=m:
                temp=monkey.popleft()
                index+=1
                monkey.append(temp)
            else:
                monkey.pop()
                index=0
        else:
            return sum(monkey)

for _ in list_nm:
    print(king(_[0],_[1]))



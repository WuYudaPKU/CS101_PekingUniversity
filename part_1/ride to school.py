import math
raw=[]
while True:
    n=int(input())
    if n==0:
        break
    temp=[]
    for _ in range(n):
        v,start=map(int,input().split())
        if start>=0:
            temp.append((v,start))
    raw.append(temp)
def time(v_start):
    return v_start[1]+(4.5/v_start[0])*3600
def arrival(lst):
    lst.sort(key=lambda x:x[1])
    t_limit=math.inf
    for v_start in lst:
        if time(v_start)>=t_limit:
            continue
        else:
            t_limit=time(v_start)
    return t_limit
for i in raw:
    print(math.ceil(arrival(i)))
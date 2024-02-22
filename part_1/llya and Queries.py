raw_lstr=list(input())
lst_judge=[]
t=len(raw_lstr)
flag_pre=raw_lstr.pop(0)
flag_new=raw_lstr.pop(0)
flag_num=0
while flag_num<=t-1:
    try:
        if flag_pre==flag_new:
            lst_judge.append(1)
            flag_num+=1
            flag_pre=flag_new
            flag_new=raw_lstr.pop(0)
        else:
            lst_judge.append(0)
            flag_num+=1
            flag_pre=flag_new
            flag_new=raw_lstr.pop(0)
    except:
        break
m=int(input())

t1 = [0]*(t-1)
t2 = [0] *(t-1)
n = t-1

def lowbit(x):
    return x & (-x)

def add(k, v):
    v1 = k * v
    while k <= n:
        t1[k] = t1[k] + v; t2[k] = t2[k] + v1
        k = k + lowbit(k)

def getsum(t, k):
    ret = 0
    while k:
        ret = ret + t[k]
        k = k - lowbit(k)
    return ret

def add1(l, r, v):
    add(l, v)
    add(r + 1, -v)

def getsum1(l, r):
    return (r) * getsum(t1, r) - l * getsum(t1, l - 1) - \
          (getsum(t2, r) - getsum(t2, l - 1))
for i in range(t-1):
    add(i,lst_judge[i])

for query in range(m):
    start,end=map(int,input().split())
    temp=getsum(start-1,end-1)
    print(temp)
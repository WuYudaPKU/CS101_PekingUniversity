n=int(input())
raw=[]
for _ in range(n):
    id,name,a,b,c=map(str,input().split())
    id=int(id)
    a=int(a)
    b=int(b)
    c=int(c)
    all=a+b+c
    raw.append((all,a,b,c,name,id))
raw.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3],x[4],x[5]))
for i in range(len(raw)):
    print(i+1,raw[i][-1])
n=int(input())
lst=[]
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    lst.append((a,b))

def MinEdges(lst,n):
    if len(set(lst))==1:
        return len(lst)//2
    if len(lst)==1:
        return 0
    if len(lst)==2:
        return 1
    lst.sort()
    a=lst[n//2]         #what the fuck!
    lst_big=[]
    lst_small=[]
    lst_=[]
    for i in lst:
        if i >a:
            lst_big.append(i)
        elif i<a:
            lst_small.append(i)
        else:
            lst_.append(i)
    result=len(lst_big)*len(lst_small)
    result+=max(len(lst_big),len(lst_small))*len(lst_)
    return result
for tuple in lst:
    print(MinEdges(tuple[1],tuple[0]))
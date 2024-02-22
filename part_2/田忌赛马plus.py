from collections import deque
def tian(deque1,deque2):
    n=len(deque1)
    success=0
    lose=0
    while deque1:
        l_tian=deque1.pop()
        l_king=deque2.pop()
        if len(deque1)==0:
            if l_tian>l_king:
                success+=1
                break
            if l_tian<l_king:
                lose+=1
                break
            if l_tian==l_king:
                break
        if l_tian>l_king:
            success+=1
            continue
        else:
            f_tian=deque1.popleft()
            f_king=deque2.popleft()
            if f_tian>f_king:
                success+=1
                if l_tian<l_king:
                    lose+=1
            elif f_tian==f_king:
                deque1.append(l_tian)
                deque2.append(l_king)
            else:
                lose+=1
                deque1.appendleft(f_tian)
                deque2.append(l_king)
    return 200*(success-lose)
res=[]
while True:
    n=int(input())
    if n==0:
        break
    lst_1=list(map(int,input().split()))
    lst_2=list(map(int,input().split()))
    lst_1.sort(reverse=True)
    lst_1.sort(reverse=True)
    deque_1=deque(lst_1)
    deque_2=deque(lst_2)
    res.append(tian(deque_1,deque_2))
for _ in res:
    print(_)
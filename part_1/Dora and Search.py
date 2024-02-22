t=int(input())
lst_1=[]
for _ in range(t):
    a=int(input())
    b=list(map(int,input().split()))
    lst_1.append([a,b])

def SearchPlus(n,lst):
    first_flag=1
    last_flag=n
    lst_copy=lst[::]
    while True:
        a=max(lst_copy[0],lst_copy[-1])
        b=min(lst_copy[0],lst_copy[-1])
        if last_flag-first_flag>2:
            if a!=last_flag and b!=first_flag:
                return [min(lst.index(a),lst.index(b)),max(lst.index(a),lst.index(b))]
            if a==last_flag:
                if lst_copy[0]==last_flag:
                    lst_copy.pop(0)
                    last_flag -= 1
                else:
                    lst_copy.pop()
                    last_flag -= 1
                continue
            if b==first_flag:
                if lst_copy[0]==first_flag:
                    lst_copy.pop(0)
                    first_flag+=1
                else:
                    lst_copy.pop()
                    first_flag+=1
                continue
        else:
            return -1

for i in lst_1:
    temp=SearchPlus(i[0],i[1])
    if temp==-1:
        print(temp)
    else:
        temp_1=[str(i+1) for i in temp]
        print(" ".join(temp_1))
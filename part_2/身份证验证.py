def qualify(x:str):
    sum=0
    for i in range(17,-1,-1):
        if i==17:
            if x[-1]=="X":
                sum+=10*2**0
            else:
                sum+=int(x[-1])*2**0
        else:
            sum+=int(x[i])*2**(17-i)
    return True if sum%11==1 else False
n,lst=int(input()),[]
for _ in range(n):
     lst.append(input())
for i in lst:
    if qualify(i):
        print("YES")
    else:
        print("NO")
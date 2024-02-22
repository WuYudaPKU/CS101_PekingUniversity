a=int(input())
b=0
for m in range(0,a+1):
    for n in range(0,a+1):
        for p in range(0,a+1):
            if (m+n)%2==0 and (n+p)%3==0 and (m+n+p)%5==0:
                b=max(b,m+n+p)
print(b)
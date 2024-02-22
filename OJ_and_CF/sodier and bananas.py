k,n,w =map(int,input().split())
all_in=0
for i in range(1,w+1):
    all_in += k*i
if all_in > n:
    print(all_in-n)
else:
    print(0)
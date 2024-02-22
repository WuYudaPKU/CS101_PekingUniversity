list_1=list(map(int,input().split()))
m,n,a=list_1[0],list_1[1],list_1[2]
if a<=10**9:
    if m%a==0:
        num_1=m/a
    else:
        num_1=m//a+1
    if n%a==0:
        num_2=n/a
    else:
        num_2=n//a+1
print(int(num_1 * num_2))
# 已知0 <= a1, a2, a3 <= n
# 而且a1 + a2是2的倍数，a2 + a3是3的倍数
# a1 + a2 + a3是5的倍数
n= int(input())
list_1=[]

for i in range(n+1):
    for j in range(n+1):
        if (i+j)%2==0:
            list_1.append([i,j])#先考虑前两个数

for _ in list_1:
    for k in range(n+1):
        if (k+_[1])%3==0 and (_[0]+_[1]+k)%5==0:#再考虑第三个数
            _.append(k)

list_2=[]
for _ in list_1:
    if len(_)==3:
        list_2.append(_)#长度筛选

if list_2:
    print(max(x[0]+x[1]+x[2] for x in list_2))
else:
    print(0)


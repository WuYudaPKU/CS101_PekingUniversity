n,a,b,c=map(int,input().split())
d = [-float('inf')] * (n + 1)
d[0] = 0  # 初始化长度为0的绳子能够得到0段
for i in range(1, n + 1):
    for length in (a,b,c):
        if i - length >= 0:
            d[i] = max(d[i], d[i - length] + 1)
print(d[n])
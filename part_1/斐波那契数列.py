def f(i):
    list_1=[1,1]
    while len(list_1)<i:
        for j in range(2,i+1):# 开始运算第3个数和第i个数
            list_1.append(list_1[j-1]+list_1[j-2])
    return list_1[i-1]

list_2=[]
times = int(input())
for _ in range(times):
    list_2.append(int(input()))
for _ in list_2:
    print(f(_))


# 假设现在有一组进程，每个进程 i 需要先累计占用 compute[i] 个 CPU 周期进行计算
# 计算完成后需要 write[i] 个时间周期将结果写文件
# 写的过程可以同步进行
n=int(input())
lst=[]
for _ in range(n):
    lst.append(tuple(map(int,input().split())))
# print(lst)
lst.sort(key=lambda x:x[1],reverse=True)
# print(lst)
time=lst[0][0]+lst[0][1]
prefix=[]
flag=0
temp=0
while True:
    try:
        temp+=lst[flag][0]
        prefix.append(temp)
        flag+=1
    except:
        break
# print(prefix)
for i in range(1,n):
    time=max(time,lst[i][0]+lst[i][1]+prefix[i-1])
print(time)
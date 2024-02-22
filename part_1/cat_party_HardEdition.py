import time

from collections import Counter
n=int(input())
# raw=list(map(int,input().split()))
start_time = time.time()  # 获取程序开始时间
raw=[1]*22222+[2]*33333+[4]*55555
dict_1={}
max_temp=0
def check(dic):
    b=True
    if len(dic)!=1:
        a=False
    else:
        a=True
    for i in dic.values():
        if i!=1:
            b=False
            break
    set_1=set()
    for i in dic.values():
        set_1.add(i)
    if len(set_1)!=2:
        c=d=False
    else:
        lst=list(set_1)
        lst.sort()
        value_counts=Counter(dic.values())
        if 1 in value_counts and value_counts[1]==1:
            d=True
        else:
            d=False
        if lst[1]-lst[0]==1:
            c=True
        else:
            c=False
    return (a or b or c or d)


for i in range(len(raw)):
    if raw[i] in dict_1:
        dict_1[raw[i]]+=1
    else:
        dict_1[raw[i]]=1
    if check(dict_1):
        max_temp=i+1
print(max_temp)
end_time = time.time()  # 获取程序结束时间
execution_time = end_time - start_time  # 计算程序执行时间
print(f"程序执行时间为：{execution_time}秒")
n,m=map(int,input().split())
raw=list(map(int,input().split()))
#原始总区间记为light，值为True表示亮，False表示灭。初始化light。
light=[True for _ in range(m)]
flag=0
switch=True
#对light进行赋值
while flag<=m-1:
    if flag in raw and flag!=0:
        switch=not switch
    light[flag]=switch
    flag+=1

temp,dp_pre_on,dp_rev_on=0,[0]*m,[(0,0)]*m
#dp_pre_on表示在第i位时前面亮灯时间（包含第i位）
#dp_rev_on中存元组，第i位的元组（a,b）中a表示第i位及以后亮灯时间，b表示灭灯时间（包含第i位）。
for index in range(m-1,-1,-1):
    if light[index]:
        temp+=1
    dp_rev_on[index]=(temp,m-index-temp)
temp=0
for index in range(m):
    if light[index]:
        temp+=1
    dp_pre_on[index]=temp

flag=0
# print(dp_preon,dp_on,dp_off)
for index in range(1,m):
    if index not in raw:
        pre_on=dp_pre_on[index-1]
        #on_after_shift表示进行插入操作以后第i位及以后亮灯时间
        on_after_shift=dp_rev_on[index][1]
        res=pre_on+on_after_shift
        if res>flag:
            flag=res
        continue
    if index==0:
        flag=m-index-temp
print(light)
print(max(flag,dp_pre_on[-1]))
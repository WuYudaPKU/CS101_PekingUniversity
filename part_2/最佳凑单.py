n,t=map(int,input().split())
raw=list(map(int,input().split()))
raw.sort()
# 如果总价值凑不够，直接退出
if sum(raw)<t:
    print("0")
    exit()

new_raw=[0]+[i for i in raw if i<t]
temp=[i for i in raw if i>=t]
a,b=sum(new_raw),len(new_raw)-1
dp=[[0 for _ in range(a-t+1)] for _ in range(b+1)]
# 数组分成了两类，一类是不足t的，一类是大于等于t的。显然只需要对不足t的进行操作，因为另一部分不需要凑单。
# a是不足t的数组求和
# 如果a的求和不满足t，则从另一部分中选择最小的。
if a-t<0:
    print(temp[0])
    exit()

# 选的记为selected，不选的记为no，则selected+no==a,selected=a-no,让selected>=t且最小,只需要让no<=a-t且最大。
# 问题转化为no在不超过a-t的时候最大，即01背包问题。
for i in range(1,b+1):
    value=new_raw[i]
    for j in range(1,a-t+1):
        if value>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(value+dp[i-1][j-value],dp[i-1][j])

print(min(a-dp[b][a-t],temp[0]) if temp
  else a-dp[b][a-t])
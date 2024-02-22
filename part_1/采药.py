t,m=map(int,input().split())
lst_tm=[]
#时间，价值
for _ in range(m):
    temp=tuple(map(int,input().split()))
    if temp[0]<=t:
        lst_tm.append(temp)
lst_tm.sort(key=lambda x: x[0])
dp=[[-1]*t for _ in range(len(lst_tm))]
def MaxValue(i,j):
    #行标i是待添加物品下标，列是总时间，i能索引到lst_tm中的元组
    if dp[i][j]!=-1:
        return dp[i][j]
    if i==0:
        if lst_tm[i][0]<=j+1:
            dp[i][j]=lst_tm[i][1]
        else:
            dp[i][j]=0
        return dp[i][j]
    else:
        if lst_tm[i][0]<=j+1:
            if j+1-lst_tm[i][0]>0:
                temp=max(MaxValue(i-1,j),
                         lst_tm[i][1]+MaxValue(i-1,j-lst_tm[i][0]))
            else:
                temp=max(MaxValue(i-1,j),lst_tm[i][1])
            dp[i][j]=temp
            return dp[i][j]
        else:
            dp[i][j]=MaxValue(i-1,j)
            return dp[i][j]
print(MaxValue(len(lst_tm)-1,t-1))
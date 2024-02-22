t,m=map(int,input().split())
lst_tm=[]
for _ in range(m):
    temp=tuple(map(int,input().split()))
    if temp[0]<=t:
        lst_tm.append(temp)
lst_tm.sort(key=lambda x: x[0])
dp=[[0]*(t+1) for _ in range(len(lst_tm)+1)]
print(dp)
#在左上角加了一个保护圈，使横坐标背包的容量从1开始。
def MaxValue(item,time_temp):
    value_item=lst_tm[item-1][1]
    time_per=lst_tm[item-1][0]
    if item==1:
        if time_per<=time_temp:
            dp[item][time_temp]+=value_item
            return dp[item][time_temp]
    else:
        if time_per>time_temp:
            if dp[item-1][time_temp]!=0:
                return dp[item-1][time_temp]
            else:
                dp[item][time_temp]=MaxValue(item-1,time_temp)
                return dp[item][time_temp]
        else:
            if dp[item-1][time_temp-time_per]*\
                    dp[item-1][time_temp]!=0:
                return max(dp[item-1][time_temp-time_per]*\
                    dp[item-1][time_temp])
            else:
                dp[item][time_temp]=max(MaxValue(item-1,time_temp-time_per),
                                        MaxValue(item-1,time_temp))
                return dp[item][time_temp]
print(MaxValue(len(lst_tm),t))

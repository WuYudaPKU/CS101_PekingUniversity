from functools import lru_cache
rows,lst_raw,dp=int(input()),[],[]
for _ in range(rows):
    temp=map(int,input().split())
    lst_raw.append(list(temp))
    dp.append([-1 for i in range(_+1)])
# for i in dp:
#     print(i)
# print(lst_raw)
def MaxSum(lst,i,j):
    #i,j从0开始标记
    length=len(lst)
    if i == length-1:
        dp[i][j] = lst[i][j]
        return dp[i][j]
    if dp[i][j]!=-1:
        return dp[i][j]
    if dp[i][j]==-1:
        dp[i][j]=max(MaxSum(lst,i+1,j),MaxSum(lst,i+1,j+1))+lst[i][j]
        return dp[i][j]
print(MaxSum(lst_raw,0,0))



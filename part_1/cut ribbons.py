n,a,b,c=map(int,input().split())
lst=[a,b,c]
lst.sort()
a1,a2,a3=lst[0],lst[1],lst[2]
dp=[0]*(n+1)
temp=n//a1
for i in range(1,temp+1):
    dp[i*a1]=i
# print(dp)
# if a1!=a2 and a2!=a3:
for j in range(1,n+1):
    if j<a1:
        continue
    if j%a1==0:
        continue
    if j>a1 and j<a2:
        if dp[j-a1]!=0:
            dp[j]=dp[j-a1]+1
    elif j==a2:
        dp[j]=max(1,1+dp[j-a1])
    elif j>a2 and j<a3:
        if dp[j-a1]!=0 or dp[j-a2]!=0:
            dp[j]=max(1+dp[j-a1],1+dp[j-a2])
    elif j==a3:
        dp[j]=max(dp[j-a1]+1,dp[j-a2]+1,1)
    elif j>a3:
        if dp[j-a1]!=0 or dp[j-a2]!=0 or dp[j-a3]!=0:
            dp[j]=max(1+dp[j-a1],1+dp[j-a2],1+dp[j-a3])
            # print(2,j)
# print(dp)
# print(dp[50])
print(dp[-1])
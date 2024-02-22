"""魔法1：对一支玫瑰施加颜色反转咒语
魔法2：对从左数前k支玫瑰同时施加颜色反转咒语（每次施法时的k值可以不同）
RRRRRBR
"""
raw=list(input())
n=len(raw)
r_dp=[0 for _ in range(n)]
b_dp=[0 for _ in range(n)]
if raw[0]=="R":
    b_dp[0]=1
else:
    r_dp[0]=1
for i in range(1,n):
    if raw[i]=="R":
        r_dp[i]=min(r_dp[i-1],b_dp[i-1]+1)
        b_dp[i]=min(r_dp[i-1]+1,b_dp[i-1]+1)
    if raw[i]=="B":
        r_dp[i]=min(r_dp[i-1]+1,b_dp[i-1]+1)
        b_dp[i]=min(r_dp[i-1]+1,b_dp[i-1])
print(r_dp[-1])
def Fplus(x):
    if x<=2:
        return 1
    else:
        if dp[x]!=-1:
            return dp[x]
        else:
            return Fplus(x-1)+Fplus(x-2)

lst_res=[]
for i in range(int(input())):
    n=int(input())
    dp=[-1 for _ in range(n+1)]
    temp=Fplus(n)
    lst_res.append(temp)

for i in lst_res:
    print(i)

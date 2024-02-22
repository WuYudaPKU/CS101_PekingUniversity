T=int(input())
S=list(map(int,input().split()))
S_new=[]
for i in S:
    if T%i==0:
        S_new.append(i)
# now是除到现在剩下的因子，left是待除列表
def dfs(now,left):
    if now==1:
        return True
    if len(left)==1:
        if now%left[0]==0 and now//left[0]==1:
            return True
        return False
    else:
        for i in range(len(left)):
            if now%left[i]!=0:
                continue
            else:
                if dfs(now//left[i],left[i+1:]):
                    return True
                else:
                    continue
    return False
print("YES" if dfs(T,S_new) else "NO")
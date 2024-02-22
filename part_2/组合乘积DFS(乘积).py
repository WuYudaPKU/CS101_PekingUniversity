T=int(input())
S=list(map(int,input().split()))
S_new=[]
for i in S:
    if T%i==0:
        S_new.append(i)
# now是除到现在剩下的因子，left是待除列表
def dfs(now,left):
    if now==T:
        return True
    if len(left)==1:
        if now*left[0]==T:
            return True
        return False
    else:
        for i in range(len(left)):
            if T%(now*left[i])!=0:
                continue
            if dfs(now*left[i],left[i+1:]):
                return True
            continue
    return False
print("YES" if dfs(1,S_new) else "NO")
n,m=map(int,input().split())
raw=[0]+list(map(int,input().split()))+[m]
sum=ans=pre=0
for i in range(1,len(raw),2):
    sum+=raw[i]-raw[i-1]
ans=sum
for j in range(2,len(raw),2):
    pre+=raw[j-1]-raw[j-2]
    if raw[j]>raw[j-1]+1:
        ans=max(ans,pre+raw[j]-(raw[j-1]+1)+m-raw[j]-(sum-pre))
print(ans)
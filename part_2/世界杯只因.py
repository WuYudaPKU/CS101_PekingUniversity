#refer to夏天明，罗景轩
n=int(input())
raw=list(map(int,input().split()))
#index是起点，value是终点
ends=[0]*n
for i in range(n):
    ends[max(i-raw[i],0)]=max(ends[max(i-raw[i],0)],i+raw[i]+1)
start,end,res=-1,0,0
while end<n:
    start,end=end,max(ends[start+1:end+1])
    res+=1
print(res)
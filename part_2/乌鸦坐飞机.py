n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=[0]*4
for i in a:
    cnt[i%4]+=1
add=cnt[1]+cnt[3] # 余1和余3的会造成一个空位
t=cnt[2]-2*n-cnt[1]
if t>0:
    add+=t//3*2
    if t%3==1:
        add+=2
    if t%3==2:
        add+=4
print("YES" if sum(a)+add<=n*8 else 'NO')
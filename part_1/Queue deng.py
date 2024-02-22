n=int(input())
t=list(map(int,input().split()))
t.sort()
not_disappointed=0
addition=0
short_t=list(set(t))#去重
short_t.sort()#升序排列
if n>=2 and t[0]==t[1]:
    short_t.insert(1,t[1])#若原列表前两个元素相等，则不能去重
for i in range(len(short_t)):
    if addition<=short_t[i]:#能够满意
        addition+=short_t[i]
        not_disappointed+=1
    else:
        short_t[i]=0#第i个顾客扔后面去
print(not_disappointed)

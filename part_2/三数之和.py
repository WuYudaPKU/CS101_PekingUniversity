lst=list(map(int,input().split()))
a=[i for i in lst if i>0]
b=[i for i in lst if i<=0]
a.sort()
b.sort()
print(a,b)
cnt_1,cnt_2=0,0
repeat=-9999999
for i in b:
    for m in range(len(a)):
        for n in range(m + 1, len(a)):
            if a[n]==repeat:
                break
            repeat=a[n]
            temp = a[m] + a[n]
            if temp+i<0:
                continue
            if temp+i==0:
                cnt_1+=1
                continue
            if temp+i>0:
                break
repeat=-9999999
for i in a:
    for m in range(len(b)):
        for n in range(m + 1, len(b)):
            if b[n] == repeat:
                break
            repeat = b[n]
            temp = b[m] + b[n]
            if temp + i < 0:
                continue
            if temp + i == 0:
                cnt_1 += 1
                continue
            if temp + i > 0:
                break
print(cnt_1+cnt_2)
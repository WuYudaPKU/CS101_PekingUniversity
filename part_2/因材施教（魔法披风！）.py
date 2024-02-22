n,m=map(int,input().split())
lst_1=list(map(int,input().split()))
lst_1.sort()
flag=1
lst_minus=[]
while True:
    try:
        temp=lst_1[flag]-lst_1[flag-1]
        lst_minus.append(temp)
        flag+=1
    except:
        break
lst_minus_1=lst_minus[::]
lst_minus_1.sort(reverse=True)
# print(lst_minus_1)
res=lst_1[-1]-lst_1[0]
for i in range(m-1):
    res-=lst_minus_1[i]
print(res)
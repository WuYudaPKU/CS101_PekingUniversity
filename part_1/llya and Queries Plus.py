raw=input()
lst_judge=[0]
lst_res=[]
flag=0
for i in range(len(raw)-1):
    if raw[i]==raw[i+1]:
        flag+=1
        lst_judge.append(flag)
    else:
        lst_judge.append(flag)
# print(raw)
# print(lst_judge)
m=int(input())
for _ in range(m):
    start,end=map(int,input().split())
    temp=lst_judge[end-1]-lst_judge[start-1]
    lst_res.append(temp)
for res in lst_res:
    print(res)

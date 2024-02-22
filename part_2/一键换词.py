import re
raw=input()
new,pre=map(str,input().split())
pre_new=pre[0].lower()+pre[1:]
a=""
for i in raw:
    a+=i.lower()
b=re.sub(new,pre_new,a)
b_lst=list(map(str,b.split(". ")))
res=[]
for i in b_lst:
    res.append(i.capitalize())
print(". ".join(res))
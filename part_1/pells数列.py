# from functools import lru_cache
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
m=max(lst)
lst_pell=[-1]*(m+1)
lst_pell[1]=1
lst_pell[2]=2
flag=3
while flag<=m:
    lst_pell[flag]=(2*lst_pell[flag-1]+lst_pell[flag-2])%32767
    flag+=1
for i in lst:
    print(lst_pell[i]%32767)
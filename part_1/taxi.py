import math
groups=int(input())
lst_1=[]
lst_2=[]
lst_3=[]
lst_4=[]
lst_0=list(map(int,input().split()))
for i in lst_0:
    if i ==1:
        lst_1.append(i)
    elif i==2:
        lst_2.append(i)
    elif i==3:
        lst_3.append(i)
    elif i==4:
        lst_4.append(i)
nums=len(lst_4)+len(lst_3)
a=len(lst_2)%2
if a==0:
    nums+=len(lst_2)//2
    b=len(lst_1)-len(lst_3)
    if b>=0:
        nums+=math.ceil(b/4)
    print(nums)
else:
    nums+=math.ceil(len(lst_2)/2)
    b=len(lst_1)-len(lst_3)-2
    if b>=0:
        nums+=math.ceil(b/4)
    print(nums)

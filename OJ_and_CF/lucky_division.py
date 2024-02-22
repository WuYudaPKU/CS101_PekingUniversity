def lucky_number(x):
    lst=list(x)
    lst_temp=[]
    flag=0
    while flag<=len(lst)-1:
        if lst[flag]!="4" and lst[flag]!="7":
            lst_temp.append(lst[flag])
            flag+=1
        else:
            flag+=1
    if len(lst_temp)!=0:
        return False
    else:
        return True

n=int(input())
if n>=0 and n<4:
    print("NO")
lst_n=[]
for i in range(1,n+1):
    if lucky_number(str(i)):
        lst_n.append(i)
for lucky in lst_n:
    a=n%lucky
    if a==0:
        print("YES")
        break
    else:
        if lucky==lst_n[-1]:
            print("NO")



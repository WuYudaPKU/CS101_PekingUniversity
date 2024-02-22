n= input()
list_2=[]
for i in range(1,int(n)+1):
    list_2.append(i)
    if (i%7 == 0) or ("7" in list(str(i))) is True:
        list_2.remove(i)
sum_1= 0
for i in list_2:
    sum_1 +=i**2
print(sum_1)
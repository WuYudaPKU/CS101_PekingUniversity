def seven(x): #x是一个数字
    if "7" in list(str(x)):
        return True
    elif x%7==0:
        return True
    else:
        return False
a=int(input())
list_sum = []
for i in range(1,a+1):
    if not seven(i):
        list_sum.append(i**2)
print(sum(list_sum))

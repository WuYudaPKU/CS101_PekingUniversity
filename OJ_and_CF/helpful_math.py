num=input()
list_num = list(num)
while "+" in list_num:
    list_num.remove("+")
list_num=sorted(list_num)#整理后的列表，形如 1 1 2 3 4 4
list_result=[]#储存 1+ 的列表
i=0
while True:
    if i <= len(list_num)-2:
        result= str(list_num[i])+"+"
        list_result.append(result)
        i+=1
    elif i == len(list_num)-1:
        result = str(list_num[i])
        list_result.append(result)
        break
    else:
        break
print("".join(list_result))


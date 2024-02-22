list_2=[]
list_1 = list(map(int,input().split()))
for i in list_1:
    if i < list_1[0]:
        list_2.append(i)
print(sum(list_2))
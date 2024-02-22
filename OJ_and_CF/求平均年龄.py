stu_num=input()
list_1=[]
for i in range(int(stu_num)):
    list_1.append(int(input()))
print("{:.2f}".format(sum(list_1)/len(list_1)))
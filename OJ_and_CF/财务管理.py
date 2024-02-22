list_1=[]
average=0
for i in range(12):
    list_1.append(float(input()))
average = sum(list_1)/len(list_1)
print("$"+"%.2f"%average)

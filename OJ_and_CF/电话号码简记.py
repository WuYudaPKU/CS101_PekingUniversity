quant_of_dells = input()
list_1=[]
list_result=list()
set_result=set()
dict={"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,
      "J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"R":7,"S":7,
      "T":8,"U":8,"V":8,"W":9,"X":9,"Y":9}
#输入转化为数字串
for i in range(int(quant_of_dells)):
    list_1=list(input())
    list_2=[]
    while "-" in list_1:
        list_1.remove("-")
    for j in list_1:
        if ord(j)>=48 and ord(j)<=57:
            list_2.append(j)
        else:
            list_2.append(dict[j])
    list_2.insert(3,"-")
    list_result.append("".join(str(x) for x in list_2))
#去重、排序、决定次数
if len(list_result) == len(set(list_result)):
    print("No duplicates.")
else:
    dict = {}
    for i in list_result:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    sorted_dict = {k:dict[k] for k in sorted(dict)}
    for key,value in sorted_dict.items():
        if value > 1:
            print(str(key)+" "+str(value))











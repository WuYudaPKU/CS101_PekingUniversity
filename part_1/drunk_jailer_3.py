lines_number = int(input())
list_of_n = []
escaped_number_list = []
for i in range(lines_number):
    list_of_n.append(int(input()))
def opposite(x):
    if x==1:
        x=0
    elif x==0:
        x=1
def escaped(n):
    list_1=[]
    dict_1={}
    for i in range(n):
        dict_1[i] = 0 #字典创建完成，100个0（关）
    for i in range(1,n+1):#i是轮数
        for j in range(n):#j是遍历
            if (j+1)%i == 0:
                opposite(dict[j])
    for i in range(n):
        if dict_1[i]==1:
            list_1.append(i)
    print(len(list_1))

for n in list_of_n:
    escaped(n)




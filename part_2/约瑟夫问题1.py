list_nm=[]
while True:
    a=list(map(int,input().split()))
    if a!=[0,0]:
        list_nm.append(a)
    else:
        break

def king(n,m):
    #第一步：m对剩余的数量取余数
    list_1 = list(i for i in range(1,n+1))
    flag,left_b=0,0
    while len(list_1)>1:
        if flag==0:
            left_a=m%len(list_1)#余数
            list_1.remove(list_1[left_a-1])#删除第余数位的数字
            left_b=left_a-1#left_b是下一次第一个数的编号
            flag+=1
        else:
            left_a = (left_b+m-1)%len(list_1)
            list_1.remove(list_1[left_a])
            left_b = left_a
    return list_1[0]

for _ in list_nm:
    print(king(_[0],_[1]))
t=int(input())
lst_result=[]
for _ in range(t):
    n=int(input())
    lst_deliver=list(map(int,input().split()))
    lst_self=list(map(int,input().split()))
    lst_minus=[]
    for i in range(n):
        temp=lst_deliver[i]-lst_self[i]
        lst_minus.append(temp)
    lst_all_1=list(zip(lst_deliver,lst_self,lst_minus))
    # print(lst_all)
    first_max=0
    lst_all_2=[]
    for tup in lst_all_1:
        if tup[-1]<=0:
            if tup[0]>first_max:
                first_max=tup[0]
        else:
            lst_all_2.append(tup)
    #对贪心一次后的lst_all_2进行操作
    lst_all_2.sort(key=lambda x:x[0],reverse=True)
    # print(lst_all_2)
    # print(first_max)
    time=0
    flag=0
    second_max=0
    while True:
        try:
            if time+lst_all_2[flag][1]<lst_all_2[flag][0]:
                time+=lst_all_2[flag][1]
                flag+=1
            else:
                if second_max<=lst_all_2[flag][0]:
                    second_max=lst_all_2[flag][0]
                flag+=1
                break
        except:
            break
    final_max=max(second_max,time,first_max)
    lst_result.append(final_max)
for i in lst_result:
    print(i)
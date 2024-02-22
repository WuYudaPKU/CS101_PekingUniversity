n,w=map(int,input().split())
lst_candy=[]
for _ in range(n):
    lst_candy.append(list(map(int,input().split())))
for list_value_weight in lst_candy:
    value,weight=list_value_weight[0],list_value_weight[1]
    list_value_weight.append(value/weight)
lst_candy.sort(key=lambda x: x[2],reverse=True)
# print(lst_candy)
#lst_candy的格式为[[value,weight,value_per_weight],...]
weight=0
value=0
flag=0
while weight<w:
    try:
        if weight+lst_candy[flag][1]<w:
            value+=lst_candy[flag][0]
            weight+=lst_candy[flag][1]
            flag+=1

        else:
            left_weight=w-weight
            value+=lst_candy[flag][2]*left_weight
            break
    except:
        break
print(round(float(value),1))

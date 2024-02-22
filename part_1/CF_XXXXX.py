list_1 = []
list_2 = []
for _ in range(int(input())):
    list_ab = list(map(int,input().split()))
    list_sequence = list(map(int,input().split()))
    list_1.append(list_ab)
    list_2.append(list_sequence)

def longest(list_x,hate):
    #先i（列表长度）,从长到短遍历，可以减少遍历次数
    #后j（切片开头）
    set_len=set()
    for i in range(len(list_x),0,-1):
        for j in range(list_x):
            try:
                list_temp=list_x[j:j+i]
                if sum(list_temp)%hate!=0:
                    set_len.add(len(list_temp))
            except:
                continue
    if set_len:
        return max(set_len)
    return -1

for list_ab,list_sequence in zip(list_1,list_2):
    hate=list_ab[1]
    print(longest(list_sequence,hate))
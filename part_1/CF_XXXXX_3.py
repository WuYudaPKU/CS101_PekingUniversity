list_1 = []
list_2 = []
for _ in range(int(input())):
    list_ab = list(map(int,input().split()))
    list_sequence = list(map(int,input().split()))
    list_1.append(list_ab)
    list_2.append(list_sequence)

def longest(list_x,hate):
    n=len(list_x)
    head,tail=0,0
    if sum(list_x)%hate!=0:
        return n
    for i in range(n):
        if list_x[i]%hate==0:
            head+=1
        else:
            head+=1
            break
    for j in range(n,-1,-1):
        if list_x[j-1]%hate==0:
            tail+=1
        else:
            tail+=1
            break
    return (n-min(head,tail))

for list_ab,list_sequence in zip(list_1,list_2):
    hate=list_ab[1]
    print(longest(list_sequence,hate))
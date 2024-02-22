nums=int(input())
list_nums=list(map(str,input().split()))
max_len=max(len(x) for x in list_nums)
list_a=[]
#将所有数的位数补成相同
for num in list_nums:
    temp=(num,num+"0"*(max_len-len(num)))
    list_a.append(temp)
print(list_a)

def key_1:

from collections import Counter
from collections import defaultdict
def is_qualified_1(dic):
    if len(dic)==1:
        return True
    else:
        return False
def is_qualified_2(dic):
    if len(dic)==2 and 1 in dic.values():
        return True
    else:
        return False
def is_qualified_3(dic):
    temp=set(dic.values())
    if len(temp)>=3:
        return False
    elif len(temp)==2:
        if 1 in temp and Counter(dic.values())[1]==1:
            return True
        lst=list(temp)
        lst.sort()
        if lst[1]-lst[0]==1 and Counter(dic.values())[lst[1]]==1:
            return True
        return False
    else:
        if 1 in temp:
            return True
        else:
            return False

n=int(input())
raw=list(map(int,input().split()))
dict_1=defaultdict(int)
max_day=0
for i in range(n):
    dict_1[raw[i]]+=1
    if is_qualified_1(dict_1) or is_qualified_2(dict_1)\
            or is_qualified_3(dict_1):
        max_day=i+1
print(max_day)
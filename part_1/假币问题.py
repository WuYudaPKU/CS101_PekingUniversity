n=int(input())
raw=[]
for _ in range(n):
    lst=[]
    for _ in range(3):
        lst.append(tuple(map(str,input().split())))
    raw.append(lst)

def judge_heavy(coin,lst_tuples):
    flag=True
    for tup in lst_tuples:
        left_temp=list(tup[0])
        right_temp=list(tup[1])
        state=tup[2]
        if coin in left_temp and state=="down": return not flag
        if coin in right_temp and state=="up": return not flag
        if (coin in left_temp or coin in right_temp) and state=="even":
            return not flag
    return flag

def judge_light(coin,lst_tuples):
    flag=True
    for tup in lst_tuples:
        left_temp=list(tup[0])
        right_temp=list(tup[1])
        state=tup[2]
        if coin in left_temp and state=="up": return not flag
        if coin in right_temp and state=="down": return not flag
        if (coin in left_temp or coin in right_temp) and state=="even":
            return not flag
    return flag

def fake(lst_tuple):
    origin=["A","B","C","D","E",
            "F","G","H","I","J","K","L"]
    for coin in origin:
        if judge_heavy(coin,lst_tuple):
            return coin,"heavy"
        if judge_light(coin,lst_tuple):
            return coin,"light"
for lst in raw:
    print(fake(lst)[0]+" is the counterfeit coin and it is "+fake(lst)[1]+".")
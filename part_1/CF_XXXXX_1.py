from collections import deque
def longest(deque_x,hate):
    a=len(deque_x)
    #先i（列表长度）
    #后j（切片开头）
    for i in range(len(deque_x),0,-1):
        for j in range(a):
            deque_temp=deque_x[j:j+i]
            if sum(deque_temp)%hate!=0:
                return len(deque_temp)
    return -1
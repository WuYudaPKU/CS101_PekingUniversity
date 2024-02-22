from collections import deque
list_1 = []
list_2 = []
for _ in range(int(input())):
    list_ab = list(map(int,input().split()))
    deque_sequence = deque(map(int,input().split()))
    list_1.append(list_ab)
    list_2.append(deque_sequence)
#前方为输入
def longest(deque_sequence,hate):
    n=len(deque_sequence)
    all=0
    for _ in deque_sequence:
        all+=_
    if all%hate!=0:
        return n
    """sum:删除元素数量之和
    left：从左侧删除的元素数量
    right：从右侧删除元素数量"""
    for sum in range(n):
        try:
            for left in range(sum):
                b=deque_sequence.popleft()
                all-=b
                for right in range(sum-left):
                    c=deque_sequence.pop()
                    all-=c
                    if all%hate!=0:
                        return n-sum
        except:
            return -1
    return -1

for list_ab,deque_sequence in zip(list_1,list_2):
    hate=list_ab[1]
    print(longest(deque_sequence,hate))
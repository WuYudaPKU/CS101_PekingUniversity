import heapq
n=int(input())
lst=list(map(int,input().split()))
lst_1=[-i for i in lst]
heapq.heapify(lst_1)
res=-sum(lst_1)
left=res
# print(lst_1)
while len(lst_1)>2:
    left-=-heapq.heappop(lst_1)
    res+=left
    # print(left)
print(res)
import heapq
n,lst,res=int(input()),list(map(int,input().split())),0
heapq.heapify(lst)
while n>=2:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    res+=a+b
    heapq.heappush(lst,a+b)
    n-=1
print(res)
# n,m=map(int,input().split())
# arr_1=list(map(int,input().split()))
# arr_m=[]
# for i in range(m):
#     arr_m.append(int(input()))
#
# def count(x,lst,n,dict_=None):
#     flag=x-1
#     set_1=set()
#     while flag<=n-1:
#         if lst[flag] not in set_1:
#             set_1.add(lst[flag])
#             flag+=1
#         else:
#             flag+=1
#     return len(set_1)
# for i in arr_m:
#     print(count(i,arr_1,n))
n, m = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_m = []
for i in range(m):
    arr_m.append(int(input()))

distinct_counts = [0] * n
distinct_count = 0
last_seen = {}

for i in range(n-1, -1, -1):
    if arr_1[i] not in last_seen:
        distinct_count += 1
    last_seen[arr_1[i]] = 1
    distinct_counts[i] = distinct_count

for i in arr_m:
    print(distinct_counts[i-1])

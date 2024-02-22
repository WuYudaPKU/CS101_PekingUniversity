# n = int(input())
# times = 0
# list_1 = list(input())
# i=1
# while i < len(list_1):
#     for i in range(1,n-1):
#         if list_1[i-1] == list_1[i]:
#             list_1.remove(list_1[i])
#             times = times + 1
#             i = i+1
#         else:
#             i=i+1
# print(times)
n = int(input())
stones = input()

count = 0
for i in range(1, n):
    if stones[i] == stones[i-1]:
        count += 1

print(count)

#只需要对是否相邻进行判断，无需把石头拿走。
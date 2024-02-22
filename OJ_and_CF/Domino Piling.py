list_1 = list(map(int, input().split()))
m, n = list_1[0], list_1[1]
# if m % 2 == 0 and n % 2 == 0:
#     print(m * n / 2)
# elif (m % 2 == 0 and n % 2 == 1) or (m % 2 == 1 and n % 2 == 0):
#     print(m * n / 2)
# else:
#     print(max((m // 2) * n, (n // 2) * m))
print((m*n)//2)
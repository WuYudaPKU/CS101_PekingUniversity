list_1 = list(map(int, input().split()))
m, n, a = list_1[0], list_1[1], list_1[2]
if m % a == 0:
    # 从这里就开始穷举了
    if n % a == 0:
        print(m * n / (a ** 2))
    else:
        print((m/a) * (n // a + 1))
else:
    if n % a == 0:
        print((n/a) * (m // a + 1))
    else:
        print(int(((n // a) + 1) * ((m // a) + 1)))

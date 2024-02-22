import bisect
n= int(input())
lst_price = list(map(int, input().split()))
lst_price.sort()
q = int(input())
for i in range(q):
    coins = int(input())
    print(bisect.bisect(lst_price, coins))
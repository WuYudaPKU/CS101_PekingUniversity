from collections import defaultdict

n = int(input())
info = list(map(int, input().split()))
cnt, max_n, max_cnt, ans = 0, 0, 0, 0
check = defaultdict(int)

for i in range(len(info)):
    c = info[i]
    if not check[c]:
        cnt += 1
    check[c] += 1
    if check[c] == max_n:
        max_cnt += 1
    if check[c] > max_n:
        max_n = check[c]
        max_cnt = 1
    if max_n == 1:
        ans = i + 1
    if max_cnt == 1 and cnt * (max_n - 1) == i:
        ans = i + 1
    if max_cnt == cnt - 1 and (cnt - 1) * max_n == i:
        ans = i + 1
print(ans)
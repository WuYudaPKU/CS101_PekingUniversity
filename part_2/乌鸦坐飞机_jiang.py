# 蒋子轩23工学院
n, _ = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0]*4
for i in a:
    cnt[i % 4] += 1
# add为空位数
add = cnt[1]+cnt[3]  # 余1或3的必定会造成一个空位
# 余2的优先放1、2和7、8，或和余1的组合放中间，这样就不会造成空位
t = cnt[2]-2*n-cnt[1]
if t > 0:  # 若还有余2的没能放好
    # 分类讨论余2的至少造成多少个空位
    add += t//3*2
    if t % 3 == 1:
        add += 2
    if t % 3 == 2:
        add += 4
print('YES' if sum(a)+add <= n*8 else 'NO')
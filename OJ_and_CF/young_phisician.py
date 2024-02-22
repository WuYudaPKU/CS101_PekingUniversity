n=int(input())
list_sum=[]#建立了一个列表，用来嵌套列表
sum_x,sum_y,sum_z = 0,0,0
for i in range(n):
    list_a = list(map(int,input().split()))
    list_sum.append(list_a)
for i in list_sum:
    sum_x += i[0]
    sum_y += i[1]
    sum_z += i[2]
if sum_x ==0 and sum_y==0 and sum_z==0:
    print("YES")
else:
    print("NO")
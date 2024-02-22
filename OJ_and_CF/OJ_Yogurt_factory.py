# n,s=map(int,input())
# def cost(ci,num_0,storage,fee=s):
#     a = ci*num_0 + storage*fee
#     return(a)
# list_Ci=[]
# list_Yi=[]
# for i in range(n):#第i周生产1桶成本为C_i；每周存1桶成本为S，第i周要送Y_i桶
#     list_Ci.append(list(map(int,input()))[0])
#     list_Yi.append(list(map(int, input()))[1])

"""典型的动态规划问题:
先假设第一周的牛奶价格就是最小价格，然后在接下来的每一周，如果价格比上一周加上仓储费用还要低
，尝试选择生产更多的酸奶（即使超过当周的需求）。如果高于上一周的价格加上仓储费用，
那就保持当前周的生产量。这样，最终的成本就是最小的。"""
def min_cost(n,s,arr):
    min_cost = arr[0][0] * arr[0][1]  #最小花销 = 第一周成本*第一周需求量
    min_price = arr[0][0] #假设第一周成本是最小成本
    for i in range(1,n):
        min_price = min(min_price+s,arr[i][0]) #第i周的最小成本是上周成本或者现在的成本
        cost = min_price * arr[i][1] #第i周的最小花费是
        min_cost+= cost
    return min_cost

N,S = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append([int(x) for x in input().split()]) #arr存起来每周“成本、需求”列表

print(min_cost(N,S,arr))
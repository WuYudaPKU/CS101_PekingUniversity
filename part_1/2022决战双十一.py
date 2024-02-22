"""n个商品和 m个店铺
此次跨店满减的活动升级为每满300减50
此外每个店铺也可能有多张不同档位的店铺券q-x（每个商品只买一件）
跨店满减活动可以叠加使用，它是指所有商品标价之和每满300，可以减去50
"""
# 以下，标号从1开始
n,m=map(int,input().split())
item_shop_price={i+1:[] for i in range(n)}
shop_minuss={i+1:[] for i in range(m)}
visited=[[True for i in range(n)] for j in range(m)]
matrix=[[0]*(n+2) for _ in range(m+2)]

for i in range(n):
    shop_price=map(str,input().split())
    for s_p in shop_price:
        temp=tuple(map(int,s_p.split(":")))
        item_shop_price[i+1].append(temp)
        # 字典item_shop_price形如 商品：[（店铺，价格），……]
        # {1: [(1, 100), (2, 120)], 2: [(1, 300), (2, 350)]}


for i in range(m):
    shop_minus=map(str,input().split())
    for j in shop_minus:
        temp=tuple(map(int,j.split("-")))
        shop_minuss[i+1].append(temp)

#初始化visited空间
for item,shop_price in item_shop_price.items():
    for tup in shop_price:
        shop,price=tup[0],tup[1]
        visited[shop-1][item-1]=False
        matrix[shop][item]=price

res,choices=[],[i for i in range(m)]
# for _ in matrix:
#     print(_)
# print(item_shop_price)
# print(shop_minuss)
# print(visited)
# print(choices)
def dfs(path,space,choice): #path用来储存第i件商品的购买店铺
    global res
    if len(path)==n:
        res.append(path)
        return
    for shop in choice:
        if space[shop][len(path)]==True:
            continue
        new_path=path+[shop+1]
        dfs(new_path,space,choice)

dfs([],visited,choices)
# print(res)
spend=[]
for alter in res:
    # print("start")
    temp_dict={i+1:0 for i in range(m)}
    for item_idx,shop_idx in enumerate(alter): #item_idx是从0开始的
        temp_dict[shop_idx]+=matrix[shop_idx][item_idx+1]
    # print(temp_dict)
    all=sum(value for value in temp_dict.values())
    # print(all)
    minus_1=(all//300)*50
    minus_2=0
    for shop in temp_dict.keys():
        lst = [0]
        for i in range(len(shop_minuss[shop])):
            if temp_dict[shop]>=shop_minuss[shop][i][0]:
                lst.append(shop_minuss[shop][i][1])
        # print("lst:",lst)
        minus_2+=max(lst)
    spend.append(all-minus_1-minus_2)
    # print("end")
print(min(spend))
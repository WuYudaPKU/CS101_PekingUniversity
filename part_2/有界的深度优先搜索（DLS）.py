from collections import defaultdict
n,m,L=map(int,input().split())
# 用字典模拟图
graph=defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    graph[a].append(b)
    graph[b].append(a)
start=int(input())
for i in graph.keys():
    graph[i].sort()
visited=[False]*n
res=[]

def dfs(path,node):
    global visited,graph,res
    res.append(node)
    visited[node]=True
    if len(path)==L+1:
        return
    for n_node in graph[node]:
        if visited[n_node]:
            continue
        path.append(n_node)
        dfs(path,n_node)
        path.pop()
    return

dfs([0],start)
ans=[str(i) for i in res]
print(" ".join(ans))

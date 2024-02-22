import heapq
def bfs(x,y,matrix):
    # 定义步空间
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    # 定义队列（heapq实现）和visited辅助空间
    queue,visited=[],set()
    heapq.heappush(queue,[0,x,y])
    visited.add((x,y))
    # while queue
    while queue:
        # 拆解当前访问坐标
        step,x,y=heapq.heappop(queue)
        # 当前访问元素的退出条件
        if matrix[x][y]==1:
            return step
        # 访问当前元素的比邻元素
        for i in range(4):
            # 取每种可能的下一步
            nx,ny=x+dx[i],y+dy[i]
            # 若不是障碍物且未经访问则入队
            if matrix[nx][ny]!=2 and (nx,ny) not in visited:
                heapq.heappush(queue,[step+1,nx,ny])
                visited.add((nx,ny))
    # 最终返回结果
    return "NO"

m,n=map(int,input().split())
matrix=[[2]*(n+2)]
for _ in range(m):
    matrix.append([2]+list(map(int,input().split()))+[2])
matrix.append([2]*(n+2))
print(bfs(1,1,matrix))
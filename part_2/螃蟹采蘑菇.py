from collections import deque

n=int(input())
matrix=[[1 for _ in range(n+2)]]
for _ in range(n):
    temp=list(map(int,input().split()))
    matrix.append([1]+temp+[1])
matrix.append([1 for _ in range(n+2)])
# for _ in matrix:print(_)
l_start=[]
for i in range(n+2):
    for j in range(n+2):
        if matrix[i][j]==5:
            l_start.append((i,j))
start=l_start[0]
delta_x=l_start[1][0]-start[0]
delta_y=l_start[1][1]-start[1]
# print(delta_x,delta_y)

def bfs(matrix,start):
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    queue=deque()
    visited=set()
    queue.append(start)
    visited.add(start)
    flag=0
    while queue:
        # print(flag,queue)
        flag+=1
        x,y=queue.popleft()
        if (matrix[x][y]==9 and matrix[x+delta_x][y+delta_y]!=1)\
                or (matrix[x+delta_x][y+delta_y]==9 and matrix[x+delta_x][y+delta_y]!=1):
            return "yes"
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if matrix[nx][ny]!=1 and matrix[nx+delta_x][ny+delta_y]!=1\
                and (nx,ny) not in visited:
                queue.append((nx,ny))
                visited.add((nx,ny))
    return "no"
print(bfs(matrix,start))

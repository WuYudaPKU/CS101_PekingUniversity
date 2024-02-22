res=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(maze,x,y,path=0):
    global res
    if maze[1][1]==1:
        res.append(0)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]==1:
            res.append(path+1)
            return
        if maze[nx][ny]==2 or maze[nx][ny]==-1:
            continue
        if maze[nx][ny]==0:
            maze[x][y]=2
            new_path=path+1
            dfs(maze,nx,ny,new_path)
            maze[x][y]=0
    return

m,n=map(int,input().split())
maze=[[-1]*(n+2)]
for _ in range(m):
    temp=[-1]+list(map(int,input().split()))+[-1]
    maze.append(temp)
maze.append([-1]*(n+2))
# for _ in maze:
#     print(_)
dfs(maze,1,1)
print(min(res) if res else "NO")
T=int(input())
cases=[]
for _ in range(T):
    cases.append(tuple(map(int,input().split())))

dx=[-1,1,2,2,1,-1,-2,-2]
dy=[-2,-2,-1,1,2,2,1,-1]
def DFS(visited,x,y):
    print(visited)
    global res,dx,dy,matrix
    #退出条件
    if len(visited) == len(matrix)*len(matrix[0]):
        return

    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if (nx<0 or nx>=len(matrix) or ny<0 or ny>=len(matrix)
                or (nx,ny) in visited):
            continue
        temp=set()
        temp.add((nx,ny))
        DFS(visited|temp,nx,ny)
        visited.discard((nx,ny))

for _ in range(T):
    res=0
    n,m,x,y=cases[_]
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    begin=set()
    begin.add((x,y))
    DFS(set(),x,y)
    print(res)

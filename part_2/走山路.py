import heapq
m,n,p=map(int,input().split())
matrix,test=[["#"]*(n+2)],[]
for _ in range(m):
    matrix.append(['#']+list(map(str,input().split()))+['#'])
matrix.append(["#"]*(n+2))
for _ in range(p):
    temp=tuple(map(int,input().split()))
    start,end=(temp[0]+1,temp[1]+1),(temp[2]+1,temp[3]+1)
    test.append((start,end))

def bfs(start,end):
    if matrix[start[0]][start[1]]=="#" or matrix[end[0]][end[1]]=="#":
        return "NO"
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    queue,visited,res=[],set(),[]
    heapq.heapify(queue)
    heapq.heappush(queue,[0,start[0],start[1]])
    visited.add((start[0],start[1]))
    while queue:
        height,x,y=heapq.heappop(queue)
        if (x,y)==end:
            return height
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if matrix[nx][ny]!="#" and (nx,ny) not in visited:
                heapq.heappush(queue,[height+abs(int(matrix[nx][ny])-int(matrix[x][y])),nx,ny])
                visited.add((x,y))
    return "NO"
for i in test:
    print(bfs(i[0],i[1]))
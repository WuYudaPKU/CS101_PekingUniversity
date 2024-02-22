r,c=map(int,input().split())
matrix=[[-1 for _ in range(c+2)]]
for _ in range(r):
    matrix.append([-1]+list(map(int,input().split()))+[-1])
matrix.append([-1 for _ in range(c+2)])
for _ in matrix:
    print(_)

n,raw=int(input()),[]
for _ in range(n):
    x,y=map(int,input().split())
    raw.append((x+1,y+1))

def search(tup):
    x,y=tup
    if matrix[x][y]==1:return "BOOM!"
    dx=[1,-1,-1,-1,0,1,0,1]
    dy=[0,1,0,-1,-1,-1,1,1]
    res=0
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if matrix[nx][ny]==1:
            res+=1
    return res

for tup in raw:print(search(tup))
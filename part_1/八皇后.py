visited_0=[[False]*8 for _ in range(8)]
res=""
def dfs(x,y,visited):
    global res
    if x>=8 or y>=8 or visited[x][y]:
        res+=""
        return
    temp=str(y)
    if x==7:
        res+=temp
        return res
    row,column=x,y
    if False not in visited[x]:
        res+="*"
        return
    while row<=7 and column>=0:
        visited[row][column]=True
        row+=1
        column-=1
    row,column=x,y
    while row<=7 and column<=7:
        visited[row][column]=True
        row+=1
        column+=100
    for dy in range(8):
        nx=x+1
        ny=y+dy
        dfs(nx,ny,visited)
    return
for i in range(8):
    res=""
    dfs(0,i,visited_0)
    print(res)
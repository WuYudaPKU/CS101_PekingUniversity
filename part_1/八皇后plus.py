#建立原始visited数组
visited_raw=[[False for _ in range(8)] for _ in range(8)]
lst_res=[]
res=""
def dfs(matrix,x,y,visited):
    global lst_res,res
    if len(res)==8:
        lst_res.append(res)
        return
    if False not in visited[x]:
        return
    if x>=8 or y>=8 or visited[x][y]:
        res+=''
        return
    row,col=x,y
    while row<=7 and col>=0:
        visited[row][col]=True
        row+=1
        col+=1
    row,col=x,y
    while row<=7 and col<=7:
        visited[row][col]=True
        row+=1
        col+
def dfs(matrix,x,y,visited):
    #如果越界，或接触边界，或接触已经标记的点，立刻终止递归并返回0
    if (x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0])
            or matrix[x][y]!="W" or visited[x][y]):
        return 0
    visited[x][y]=True
    area=1
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        area += dfs(matrix, x + dx, y + dy, visited)
    return area
def max_adj_area(matrix):
    rows,cols=len(matrix),len(matrix[0])
    visited=[[False for _ in range(cols)] for _ in range(rows)]
    max_area=0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]=="W" and not visited[row][col]:
                area=dfs(matrix,row,col,visited)
                max_area=max(max_area,area)
    return max_area
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    matrix_1=[input() for _ in range(N)]
    print(max_adj_area(matrix_1))
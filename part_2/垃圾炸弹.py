d=int(input())
n=int(input())
matrix=[[0]*1025 for _ in range(1025)]
# print(matrix)
for _ in range(n):
    x,y,q=map(int,input().split())
    for i in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            matrix[i][j]+=q
res=0
max_flag=0
for i in range(1025):
    for j in range(1025):
        if matrix[i][j]>max_flag:
            max_flag=matrix[i][j]
            res=1
        elif matrix[i][j]==max_flag:
            res+=1
print(res,max_flag)
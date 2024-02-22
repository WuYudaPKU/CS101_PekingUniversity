n,m=map(int,input().split())
matrix_d=[]
matrix_a=[]
matrix_l=[]

for i in range(n):
    temp=[0]*n
    matrix_d.append(temp)
    matrix_a.append(temp)
    matrix_l.append(temp)

for i in range(m):
    a,b=map(int,input().split())
    matrix_a[a][b],matrix_a[b][a]=1,1
    print(temp)
    matrix_d[a][a]+=1
    matrix_d[b][b]+=1
# print(id(matrix_a))
# print(id(matrix_d))
for row in range(n):
    for column in range(n):
        matrix_l[row][column]=matrix_d[row][column]-matrix_a[row][column]
for i in matrix_l:
    temp=[str(m) for m in i]
    # print(" ".join(temp))
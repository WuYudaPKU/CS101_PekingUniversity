n,m=map(int,input().split())
lst_0=[0]*(m+2)
matrix_1=[lst_0]
for _ in range(n):
    lst_temp=list(map(int,input().split()))
    lst_temp=[0]+lst_temp+[0]
    matrix_1.append(lst_temp)
matrix_1.append(lst_0)
# for _ in matrix_1:
#     print(_)
def adj(matrix,row,column):
    temp=0
    if matrix[row][column]==1:
        if matrix[row+1][column]==0:
            temp+=1
        if matrix[row][column+1] == 0:
            temp+=1
        if matrix[row-1][column] == 0:
            temp+=1
        if matrix[row][column-1] == 0:
            temp+=1
    return temp
res=0
for row in range(1,n+1):
    for column in range(1,m+1):
        res+=adj(matrix_1,row,column)
print(res)


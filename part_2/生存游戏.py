m,n=map(int,input().split())
matrix_1=[]
for _ in range(m+2):
    temp=[0]*(n+2)
    # print(temp)
    matrix_1.append(temp)
# print(matrix_1)
for row in range(m):
    temp = list(map(int, input().split()))
    for column in range(n):
        matrix_1[row+1][column+1]=temp[column]
# print(matrix_1)
def search(matrix,row,column):
    temp=matrix[row-1][column]+matrix[row-1][column-1]+matrix[row-1][column+1]\
    +matrix[row][column-1]+matrix[row][column+1]\
    +matrix[row+1][column-1]+matrix[row+1][column]+matrix[row+1][column+1]
    if matrix[row][column]==1:
        if temp<2 or temp>3:
            return 0
        else:
            return 1
    else:
        if temp==3:
            return 1
        else:
            return 0
matrix_change=[]
for _ in range(m+2):
    temp=[0]*(n+2)
    # print(temp)
    matrix_change.append(temp)
for row in range(m):
    for column in range(n):
        matrix_change[row+1][column+1]=search(matrix_1,row+1,column+1)
# for _ in matrix_change:
#     print(_)
matrix_change.pop(0)
matrix_change.pop()
for _ in matrix_change:
    _.pop(0)
    _.pop()
    __=[str(num) for num in _]
    print(" ".join(__))
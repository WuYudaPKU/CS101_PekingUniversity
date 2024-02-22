#矩阵的行列数，矩阵1非零元素数，矩阵2非零元素数
n,a,b=map(int,input().split())
matrix_1,matrix_2,matrix_result={},{},{}
#坐标对应元素
for _ in range(a):
    row,column,element=map(int,input().split())
    matrix_1[(row,column)]=element
for _ in range(b):
    row, column, element = map(int, input().split())
    matrix_2[(row, column)] = element
#对结果矩阵的每一位进行运算
for row in range(n):
    for column in range(n):
        matrix_result[(row, column)]=0
        for _ in range(n):
            if (row,_) in matrix_1 and (_,column) in matrix_2:
                matrix_result[(row,column)]+=matrix_1[(row,_)]*matrix_2[(_,column)]
            else:
                continue
#整理
sorted_matrix=sorted(matrix_result.items())
#打印
for item in sorted_matrix:
    a,b,c=item[0][0],item[0][1],item[1]
    if c!=0:
        print(a,b,c)
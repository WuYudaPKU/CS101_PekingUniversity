def MaxMatrixOdd(n,nums):
    matrix_1=[]
    for _ in range(n):
        temp = [0] * n
        matrix_1.append(temp)
    if nums!=0:
        if nums<=2*n-1:
            for i in range((nums-1)//2+1):
                matrix_1[0][i]=1
                matrix_1[i][0]=1
            return matrix_1
        else:
            for i in range(n):
                matrix_1[0][i]=1
                matrix_1[i][0]=1
            for row in range(1,n):
                for column in range(1,n):
                    matrix_1[row][column]=MaxMatrixEven(n-1,nums-(2*n-1))[row-1][column-1]
    if nums==0:
        return matrix_1
    return matrix_1

def MaxMatrixEven(n,nums):
    matrix_1=[]
    for _ in range(n):
        temp = [0] * n
        matrix_1.append(temp)
    if nums!=0:
        if nums<=2*n:
            for i in range(nums//2):
                matrix_1[0][i]=1
                matrix_1[i][0]=1
            matrix_1[1][1]=1
            return matrix_1
        else:
            for i in range(n):
                matrix_1[0][i]=1
                matrix_1[i][0]=1
            for row in range(1,n):
                for column in range(1,n):
                    matrix_1[row][column]=MaxMatrixOdd(n-1,nums-(2*n-1))[row-1][column-1]
    if nums==0:
        return matrix_1
    return matrix_1

n,nums=map(int,input().split())
if nums<=n*n:
    if nums%2==0:
        matrix_1=MaxMatrixEven(n,nums)
    else:
        matrix_1=MaxMatrixOdd(n,nums)
    for rows in matrix_1:
        temp=[str(i) for i in rows]
        print(" ".join(temp))
else:
    print(-1)
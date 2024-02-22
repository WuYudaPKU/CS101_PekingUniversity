t=int(input())
def MinNumber(matrix,n):
    lst_1,lst_2,lst_3,lst_4=[],[],[],[]
    for row in range(n//2):
        for column in range(n//2):
            lst_1.append(matrix[row][column])
    for column in range(n-1,n//2-1,-1):
        for row in range(n//2):
            lst_2.append(matrix[row][column])
    for row in range(n-1,n//2-1,-1):
        for column in range(n-1,n//2-1,-1):
            lst_3.append(matrix[row][column])
    for column in range(n//2):
        for row in range(n-1,n//2-1,-1):
            lst_4.append(matrix[row][column])
    lst=zip(lst_1,lst_2,lst_3,lst_4)
    res=0
    for tuple in lst:
        a=max(ord(i) for i in tuple)
        res+=sum(abs(a-ord(i)) for i in tuple)
    return res

for _ in range(t):
    n=int(input())
    matrix_1=[]
    for _ in range(n):
        temp=list(input())
        matrix_1.append(temp)
    print(MinNumber(matrix_1,n))
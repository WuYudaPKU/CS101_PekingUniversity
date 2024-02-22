rows,columns,lines=map(int,input().split())
matrix=[[0]*(columns+2) for _ in range(rows+2)]
lst_dots=[]
for _ in range(lines):
    lst_dots.append(tuple(map(int,input().split())))
def is_pixels(matrix_1,m,n):
    if matrix_1[m][n]*matrix_1[m-1][n]*matrix_1[m-1][n-1]*matrix_1[m][n-1]==1:
        return True
    elif matrix_1[m][n]*matrix_1[m-1][n]*matrix_1[m-1][n+1]*matrix_1[m][n+1]==1:
        return True
    elif matrix_1[m][n]*matrix_1[m][n-1]*matrix_1[m+1][n-1]*matrix_1[m+1][n]==1:
        return True
    elif matrix_1[m][n]*matrix_1[m][n+1]*matrix_1[m+1][n+1]*matrix_1[m+1][n]==1:
        return True
    else:
        return False
flag=0
for dot in lst_dots:
    flag+=1
    m,n=dot[0],dot[1]
    matrix[m][n]=1
    if is_pixels(matrix,m,n):
        print(flag)
        flag-=1
        break
if flag==len(lst_dots):
    print(0)
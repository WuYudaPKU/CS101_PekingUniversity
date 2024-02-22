n,nums=map(int,input().split())
matrix_1=[]
for i in range(n,-1,-1):
    temp=[0]*i
    matrix_1.append(temp)
matrix_1.pop()
# print(matrix_1)
row=0
left=nums
column=0
if nums>n*n:
    print(-1)
else:
    if nums!=1:
            while left>0:
                if left!=1:
                    if column<=len(matrix_1[row+1]):
                        matrix_1[row][column]=1
                        if column==0:
                            left-=1
                        else:
                            left-=2
                        column+=1
                    else:
                        row+=1
                        column=0
                        matrix_1[row][column] = 1
                        if column == 0:
                            left -= 1
                        else:
                            left -= 2
                        column += 1
                else:
                    row+=1
                    column=0
                    matrix_1[row][column]=1
                    break
    else:
            matrix_1[0][0]=1

    matrix_2=[]
    for row in matrix_1:
        minus=n-len(row)
        row=[0]*minus+row
        matrix_2.append(row)
    for i in range(n):
        for j in range(n):
            if matrix_2[i][j]==1 or matrix_2[j][i]==1:
                matrix_2[i][j],matrix_2[j][i]=1,1
    matrix_3 = []
    for i in matrix_2:
        temp = [str(j) for j in i]
        matrix_3.append(temp)
    for i in matrix_3:
        print(" ".join(i))
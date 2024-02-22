n=int(input())
matrix=[]
temp=[(-1) for _ in range(n+2)]
matrix.append(temp)
for _ in range(n):
    matrix.append([-1]+[0 for _ in range(n)]+[-1])
matrix.append(temp)
flag=0
num=1
i=1
j=1
# flag分别为0,1，2，3时分别对应向右、下、左、上。
while num<=n*n:
    if i==1 and j==1:
        matrix[i][j]=1
        i=i
        j+=1
        num+=1
    if flag==0:
        if matrix[i][j+1]==0:
            matrix[i][j]=num
            num+=1
            i=i
            j+=1
            continue
        else:
            matrix[i][j]=num
            num+=1
            i+=1
            j=j
            flag=1
            continue
    if flag==1:
        if matrix[i+1][j]==0:
            matrix[i][j]=num
            num+=1
            i+=1
            j=j
            continue
        else:
            matrix[i][j]=num
            num+=1
            i=i
            j-=1
            flag=2
            continue
    if flag==2:
        if matrix[i][j-1]==0:
            matrix[i][j]=num
            num+=1
            i=i
            j-=1
            continue
        else:
            matrix[i][j]=num
            num+=1
            i-=1
            j=j
            flag=3
            continue
    if flag==3:
        if matrix[i-1][j]==0:
            matrix[i][j]=num
            num+=1
            i-=1
            j=j
            continue
        else:
            matrix[i][j]=num
            num+=1
            i=i
            j+=1
            flag=0
            continue
del matrix[0]
matrix.pop()
for i in matrix:
    del i[0]
    i.pop()
matrix_str=[]
for i in matrix:
    temp=[str(x) for x in i]
    matrix_str.append(temp)
for _ in matrix_str:
    print(" ".join(_))
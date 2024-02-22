n=int(input())
matrix=[["#"]*(n+2)]
res,res_trans=[],[]
for _ in range(n):
    matrix.append(["#"]+list(map(int,input().split()))+["#"])
matrix.append(["#"]*(n+2))
# for i in matrix:
#     print(i)
def read(n):
    global res
    global matrix
    flag="down"
    i,j,times=1,1,0
    while times<n*n:
        times+=1
        res.append(matrix[i][j])
        # print(times,(i,j),res)
        matrix[i][j]="#"
        if flag=="down":
            if matrix[i+1][j]!="#":
                i+=1
                continue
            else:
                flag="right"
                j+=1
                continue
        if flag=="right":
            if matrix[i][j+1]!="#":
                j+=1
                continue
            else:
                flag="up"
                i-=1
                continue
        if flag=="up":
            if matrix[i-1][j]!="#":
                i-=1
                continue
            else:
                flag="left"
                j-=1
                continue
        if flag=="left":
            if matrix[i][j-1]!="#":
                j-=1
                continue
            else:
                flag="down"
                i+=1
                continue
read(n)
for i in res:
    if i!=0:
        res_trans.append(chr(i))
    else:
        res_trans.append(" ")
print("".join(res_trans))

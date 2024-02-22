n=int(input())
matrix=[[-1]*(n+2)]
for _ in range(n):
    temp=[-1]+list(map(int,input().split()))+[-1]
    matrix.append(temp)
matrix.append([-1]*(n+2))
visited=[[True] *(n+2)]
for _ in range(n):
    temp=[True]+[False for _ in range(n)]+[True]
    visited.append(temp)
visited.append([True for _ in range(n+2)])

times=0
flag=0
res=0
res_=0
i,j=1,1

while times<n*n:
    if i==1 and j==1:
        res+=matrix[i][j]
        visited[i][j]=True
        times+=1
        i=i
        j+=1
    if flag==0:
        if not visited[i][j+1]:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i=i
            j+=1
            continue
        else:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i+=1
            flag=1
            continue
    elif flag==1:
        if not visited[i+1][j]:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i+=1
            j=j
            continue
        else:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i=i
            j-=1
            flag=2
            continue
    elif flag==2:
        if not visited[i][j-1]:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i=i
            j-=1
            continue
        else:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i-=1
            j=j
            flag=3
            continue
    elif flag==3:
        if not visited[i-1][j]:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i-=1
            j=j
            continue
        else:
            res += matrix[i][j]
            visited[i][j] = True
            times += 1
            i=i
            j+=1
            flag=0
            res_=max(res,res_)
            res=0
            continue
print(res_)
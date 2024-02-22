A,B,K=map(int,input().split())
r_max=[]#用于计算保护圈大小
K_matrice=[[0]*4 for i in range(K)]#用矩阵存储R,S,P,T
for k in range(K):
    a=list(input().split())
    for i in range(4):
        K_matrice[k][i]=a[i]
    r=(int(a[2]))//2
    r_max.append(r)
r_protective=max(r_max)
field=[[0]*(B+2*r_protective) for i in range(A+2*r_protective)]
calculate_times=[[0]*(B+2*r_protective) for i in range(A+2*r_protective)]#用于计算某个方格被炸的次数    
for k in range(K):
    r=r_max[k]
    R,S,P,T=int(K_matrice[k][0]),int(K_matrice[k][1]),int(K_matrice[k][2]),int(K_matrice[k][3])
    if T==0:
        for i in range(R-1-r+r_protective,R+r+r_protective):
            for j in range(S-1-r+r_protective,S+r+r_protective):
                field[i][j]-=1
                calculate_times[i][j]+=1
    elif T==1:
        for i in range(R-1-r+r_protective,R+r+r_protective):
            for j in range(S-1-r+r_protective,S+r+r_protective):
                field[i][j]+=1
                calculate_times[i][j]+=1
possible_grid=0
max_column,max_row=[],[] 
for i in range(r_protective,r_protective+A):
    max_row.append(max(field[i]))#找出保护圈内每行的最大可能值
most_possible_grid=max(max_row)#找出整个保护圈内矩阵的最大可能值
for i in range(r_protective,r_protective+A):
    for j in range(r_protective,r_protective+B):#遍历保护圈内部所有可能值
        if field[i][j]==most_possible_grid:
            possible_grid+=1
print(possible_grid)
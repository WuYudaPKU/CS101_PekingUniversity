n=int(input())
height=list(map(int,input().split()))
matrix=[[0 for _ in range(max(height))] for _ in range(len(height))]

for row,h in enumerate(height):
    for i in range(h):
        matrix[row][i]="#"
# for _ in matrix:
#     print(_)
# print("\n")
col=0
res=0
while col<=len(matrix[0])-1:
    # print("col",col)
    flag_pre,times_pre=0,0
    flag_rev,times_rev=-1,0
    while flag_pre<=len(matrix)-1:
        if matrix[flag_pre][col]=="#":
            times_pre+=1
        if matrix[flag_pre][col]!="#":
            if times_pre>=1:
                matrix[flag_pre][col]+=1
        flag_pre+=1
    while flag_rev>=-len(matrix):
        if matrix[flag_rev][col]=="#":
            times_rev+=1
        if matrix[flag_rev][col]!="#":
            if times_rev>=1:
                matrix[flag_rev][col]+=1
        flag_rev-=1
    col+=1
    # for _ in matrix:
    #     print(_)
    # print("\n")
for row in matrix:
    for item in row:
        if item==2:
            res+=1
print(res)
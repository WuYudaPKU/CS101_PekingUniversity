import copy
import itertools
matrix=[[-1]*8]
for i in range(5):
    matrix.append([-1]+list(map(int,input().split()))+[-1])
matrix.append([-1]*8)
choices=itertools.product([0, 1], repeat=6)
def opp(x):
    if x==1:
        return 0
    elif x==0:
        return 1
    else:
        return -1
def push(x,y):
    global temp_matrix
    temp_matrix[x-1][y]=opp(temp_matrix[x-1][y])
    temp_matrix[x+1][y]=opp(temp_matrix[x+1][y])
    temp_matrix[x][y-1]=opp(temp_matrix[x][y-1])
    temp_matrix[x][y+1]=opp(temp_matrix[x][y+1])
    temp_matrix[x][y]=opp(temp_matrix[x][y])
    return
def push_judge(x,y):
    global temp_matrix
    if temp_matrix[x - 1][y] == 1:
        return True
    else:
        return False

# 主体部分
for i in choices:   # 对于第一行所有可能的按法
    # print("choice: ",i)
    temp_res=[[0]*6 for _ in range(5)]  # temp_res用来存储按键
    temp_matrix=copy.deepcopy(matrix)  # temp_matrix有保护圈
    temp_res[0]=i   # temp_res是没有保护圈的
    for k in range(len(i)):
        if i[k]==1:
            push(1,k+1)
    for row in range(2,6):
        for column in range(1,7):
            if push_judge(row,column):
                push(row,column)
                temp_res[row-1][column-1]=1
    flag=True
    if 1 in temp_matrix[5]:
        flag=not flag
    if flag:
        for _ in temp_res:
            temp=[str(i) for i in _]
            print(" ".join(temp))
        break
row,column,steps=map(int,input().split())
#建立矩阵
matrix=[]
for _ in range(row):
    temp=[]
    for i in range(column):
        temp.append(0)
    matrix.append(temp)

#存下黑像素点
lst_points=[]
for _ in range(steps):
    lst_points.append(tuple(map(int,input().split())))
for point in lst_points:
    matrix[point[0]-1][point[1]-1]=1

#开始逐行遍历矩阵,把每行连续的两个黑像素坐标存在列表中
lst_1=[]
lst_2=[]
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if column+1==len(matrix[0]):
            continue
        if matrix[row][column]==1 and matrix[row][column+1]==1:
            lst_1.append([(row,column),(row,column+1)])

#检索黑像素是否为2*2上下行连续,如果连续则把这四个像素点加入列表并储存
for lst_tuples in lst_1:
    try:
        if matrix[lst_tuples[0][0]+1][lst_tuples[0][1]]==1 \
                and matrix[lst_tuples[1][0]+1][lst_tuples[1][1]]==1:

            temp=[(lst_tuples[0][0]+1,lst_tuples[0][1])
                  ,(lst_tuples[1][0]+1,lst_tuples[1][1])]
            lst_tuples += temp
            lst_2.append(lst_tuples)
    except:
        continue
#开始比较最早的完成时间
if lst_2==[]:
    print(0)
else:
    lst_3,lst_4=[],[]
    for rec in lst_2:
        for point in rec:
            temp=(point[0]+1,point[1]+1)
            a=lst_points.index(temp)
            lst_3.append(a)
        b=max(lst_3)
        lst_4.append(b)
    c=min(lst_4)
    print(c+1)

list_rows=[]
list_count=[]
for i in range(5):
    list_row = list(input().split())
    list_rows.append(list_row)
for index,row in enumerate(list_rows):
    if "1" in row:
        list_count.append(index)    #把有1的行数加入列表count
for index,column in enumerate(list_rows[list_count[0]]):
    if "1" == column:
        list_count.append(index)
steps=abs(list_count[0]-2)+abs(list_count[1]-2) #abs是绝对值函数
print(steps)
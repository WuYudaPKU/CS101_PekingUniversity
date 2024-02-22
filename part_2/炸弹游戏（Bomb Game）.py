m,n,num=map(int,input().split())
matrix_1=[]
for _ in range(m+2):
    matrix_1.append([0] * (n + 2))
# print(matrix_1)
def bomb(matrix,row,column,field):
    list_pill=[]
    for i in range(max(1,row-(field-1)//2),min(len(matrix[0])-2,row+(field-1)//2)+1):
        for j in range(max(1,column-(field-1)//2),min(len(matrix)-2,column+(field-1)//2)+1):
            list_pill.append((i,j))
    return list_pill

lst_abcd=[]
lst_set_1=[]
lst_set_discard=[]
for i in range(num):
    temp_tuple=tuple(map(int,input().split()))
    lst_abcd.append(temp_tuple)
for tuple in lst_abcd:
    if tuple[-1]==1:
        temp_set=set()
        for i in bomb(matrix_1,tuple[0],tuple[1],tuple[2]):
            temp_set.add(i)
        lst_set_1.append(temp_set)
    if tuple[-1]==0:
        temp_set = set()
        for i in bomb(matrix_1, tuple[0], tuple[1], tuple[2]):
            temp_set.add(i)
        lst_set_discard.append(temp_set)

intersection=set.intersection(*lst_set_1)
union_discard=set.union(*lst_set_discard)
for i in union_discard:
    intersection.discard(i)
print(len(intersection))

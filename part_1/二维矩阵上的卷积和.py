m,n,p,q=map(int,input().split())
matrix_raw,matrix_core=[],[]
for _ in range(m):
    temp=list(map(int,input().split()))
    matrix_raw.append(temp)
for _ in range(p):
    temp_=list(map(int,input().split()))
    matrix_core.append(temp_)
# print(matrix_raw)
# print(matrix_core)
lst_res=[]
flag_row=0
while flag_row<=m-p:
    flag_column=0
    temp_lst=[]
    while flag_column<=n-q:
        res=0
        for step_wide in range(p):
            for step_deep in range(q):
                res+=matrix_core[step_wide][step_deep]\
                *matrix_raw[flag_row+step_wide][flag_column+step_deep]
        temp_lst.append(res)
        flag_column+=1
    lst_res.append([str(i) for i in temp_lst])
    flag_row+=1

for _ in lst_res:
    print(" ".join(_))
#代码在两个特殊情况样例上跑了起来
#找错误的时候因为输入错误（而不是代码错误）复现了错误
#最终找到的错误不是因为又跑了一遍发现的，而是因为眼睛瞄到了然后就改对了
#主打一个全靠概率
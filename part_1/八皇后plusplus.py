cols=[i for i in range(8)]
res=[]
def Queen(path,choices,main_diag,vice_diag):
    #退出条件
    if len(path)==8:
        temp=[str(j+1) for j in path]
        res.append("".join(temp))
        return
    #下一步操作
    for j in choices:
        #剪枝操作
        if j in path or j+len(path) in vice_diag or j-len(path) in main_diag:
            continue
        new_path = path + [j]
        new_main_diag = main_diag.copy()
        new_vice_diag = vice_diag.copy()
        new_main_diag.add(j - len(path))
        new_vice_diag.add(j + len(path))
        #下一层递归
        Queen(new_path, choices, new_main_diag, new_vice_diag)
main_diags=set()
vice_diags=set()
#直接调用函数，没有返回值
Queen([],cols,main_diags,vice_diags)
lst=[]
t=int(input())
for _ in range(t):
    lst.append(res[int(input())-1])
for i in lst:
    print(i)
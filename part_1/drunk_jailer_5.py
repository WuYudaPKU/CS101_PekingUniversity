times=int(input())
n_list=[]
for i in range(times):
    n_list.append(int(input()))
def f(n):
    a=0
    for prison in range(1,n+1):
        if prison**((1/2))%1==0:
            a+=1
    return(a)
for n in n_list:
    print(f(n))
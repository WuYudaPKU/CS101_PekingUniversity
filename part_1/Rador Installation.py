import math
raw=[]
while True:
    n,d=map(int,input().split())
    if n==0 and d==0:break
    temp_l=[]
    for _ in range(n):
        temp_l.append(tuple(map(int,input().split())))
    raw.append([n,d,temp_l]) # n_d_l
    blank=input()
# for _ in raw:
#     print(_)
def x_axis_d(spot,detect):
    x,y=spot[0],spot[1]
    return round(x-math.pow((detect**2-y**2),1/2),4)\
            ,round(x+math.pow((detect**2-y**2),1/2),4)

def least_radar(n_d_l):
    n=n_d_l[0]
    d=n_d_l[1]
    l=n_d_l[2] # [(1, 2), (-3, 1), (2, 1)]
    for tup in l:
        if tup[-1]>d:
            return -1

    lst_binary=[]
    for tup in l:
        lst_binary.append(x_axis_d(tup,d))
    lst_binary.sort(key=lambda x:x[1])
    end=lst_binary[0][1]
    cnt=1
    for i in range(1,len(lst_binary)):
        if lst_binary[i][0]<=end<=lst_binary[i][1]:
            continue
        else:
            end=lst_binary[i][-1]
            cnt+=1
    return cnt

for i in range(len(raw)):
    print("Case {x}: ".format(x=i+1)+str(least_radar(raw[i])))
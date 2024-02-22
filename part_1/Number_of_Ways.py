n=int(input())
lst_raw=list(map(int,input().split()))
flag,flag_abs=0,0
res_pre,res_rev,res_all,lst_sum=[],[],[],[]
all=sum(lst_raw)
if all%3!=0:
    print(0)
else:
    #这里分求和是否为0进行讨论，因为求和为0的数列非常特殊，每个等分点都同时是前后三等分点，可以直接自然数列累加出结果。
    if all!=0:
        #前后三等分之和
        pre=all//3
        last=pre*2
        while True:
            try:
                #出一个数加和一次，判断等分位置并储存
                temp=lst_raw[flag_abs]
                flag+=temp
                if flag==pre or flag==last:
                    flag_abs+=1
                    if flag==pre:
                        #如果元组[1]标记为1，则为1/3等分点
                        res_pre.append((flag_abs-1,1))
                        res_all.append((flag_abs-1,1))
                    if flag==last:
                        #如果元组[1]标记为2，则为2/3等分点
                        res_rev.append((flag_abs-1,2))
                        res_all.append((flag_abs - 1, 2))
                else:
                    flag_abs+=1
            except:
                break
        """这里把n2的复杂度改成了线性的复杂度，因为1/3,2/3等分点总是按照一个线性的顺序出现，如果遍历到1/3等分点，后面的2/3等分点
        个数即为此处1/3等分点可能的情况数；
        那么如果遍历到2/3等分点，让2/3的总数减少1,结果总数不增加即可
        前面将求和为0单独剔除，是因为同时讨论两种等分点很麻烦。"""
        if res_pre!=0 and res_rev!=0:
            res=0
            pre_len=len(res_pre)
            rev_len=len(res_rev)
            for tuple_ in res_all:
                if tuple_[1]==1:
                    temp=rev_len
                    res+=temp
                if tuple_[1]==2:
                    rev_len-=1
            print(res)
        else:
            print(0)
    else:
        pre = 0
        last = 0
        while True:
            try:
                temp = lst_raw[flag_abs]
                flag += temp
                if flag == 0:
                    res_all.append(1)
                    flag_abs+=1
                else:
                    flag_abs+=1
            except:
                break
        res=sum(i for i in range(len(res_all)-1))
        print(res)

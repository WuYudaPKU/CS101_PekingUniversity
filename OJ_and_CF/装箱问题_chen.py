sumlist=[]
while True:
    try:
        sum0 = 0
        n = list(map(int,input().split()))
        y_1 = n[0]
        y_2 = n[1]
        if sum(n) == 0:
            break
        sum0 += n[5]
        if n[4] !=0:
            if n[4] >= (n[0]-1)//11:
                sum0 += n[4]
                y_1 = 0
            else:
                y_1 = n[0]-11*n[4]
        if n[3] !=0:
            if n[3] >= (n[1]-1)//5:
                y_2 = 0
                if (n[3]*5-n[1])*4 >= y_1:
                    y_1 = 0
                    sum0 += n[3]
                else:
                    y_1 -= (n[3]*5-n[1])*4
                    sum0 += n[3]
            else:
                sum0 += n[3]
                y_2 = n[1]-5*n[3]
        if n[2] != 0:
            if n[2]%4 == 0:
                sum0 += n[2]//4
            else:
                if n[2]%4 == 1:
                    if y_2<=5:
                        y_1-=27-y_2*4
                        if y_1<=0:
                            y_1=0
                        y_2 =0
                    else:
                        y_2-=5
                        y_1-=7
                        if y_1<=0:
                            y_1=0
                    sum0+=1
                if n[2]%4 == 2:
                    if y_2<=3:
                        y_1-=18-y_2*4
                        if y_1<=0:
                            y_1=0
                        y_2=0
                    else:
                        y_2-=3
                        y_1-=6
                        if y_1<=0:
                            y_1=0
                    sum0+=1
                if n[2]%4 == 3:
                    if y_2<=1:
                        y_1-=9-y_2*4
                        if y_1<=0:
                            y_1=0
                        y_2=0
                    else:
                        y_2-=1
                        y_1-=5
                        if y_1<=0:
                            y_1=0
                    sum0+=1
        sum0+=(y_2*4+y_1)//36
        if (y_1+y_2*4)%36 == 0:
            sum0+=1
        sumlist.append(sum0)
    except EOFError:
        break
for i in sumlist:
    print(i)
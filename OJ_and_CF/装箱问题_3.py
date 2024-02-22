import math
def min_boxes(list_x):
    a6 = list_x[-1]
    a5 = list_x[-2]
    a4 = list_x[-3]
    a3 = list_x[-4]
    a2 = list_x[-5]
    a1 = list_x[-6]
#定义函数用于返回1*1箱子的填充情况
    def left_1(n):
        left_11 = 6 * 6 * n - 6 * 6 * a6 \
                  - 5 * 5 * a5 - 4 * 4 * a4 - 3 * 3 * a3 \
                  - 2 * 2 * a2
        if left_11 >= a1:
            return n
        else:
            left_11 = a1-left_11 #之前的箱子装满后剩余的1*1个数
            n += math.ceil(left_11/36)
            return n

    num_boxes=a6+a5+a4+math.ceil(a3/4)
    left_3=a3%4
    if a2>a4*5:
        left_2 = a2-a4*5 #再装2,2溢出4：
        dict_mod_num={1:5,2:3,3:1}
        if left_3!=0:
            for mod,num in dict_mod_num.items():
                if left_3 == mod:
                    left_2 = left_2 - num
                    num_boxes+=math.ceil(left_2/9)
                    return left_1(num_boxes)
        else:
            num_boxes+=math.ceil(left_2/9)
            return left_1(num_boxes)

    elif a2<=a4*5: #装1即可
        return left_1(num_boxes)

list_1 = []
while True:
    list_tem=list(map(int,input().split()))
    if list_tem != [0,0,0,0,0,0]:
        list_1.append(list_tem)
    else:
        break
for _ in list_1:
    print(int(min_boxes(_)))

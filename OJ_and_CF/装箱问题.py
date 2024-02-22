import math
list_1 = []
while True:
    list_tem=list(map(int,input().split()))
    if list_tem != [0,0,0,0,0,0]:
        list_1.append(list_tem)
    else:
        break

def min_boxes(x):

    def left_1(num_boxes):
        left_11 = 6 * 6 * num_boxes - 6 * 6 * x[-1] \
                  - 5 * 5 * x[-2] - 4 * 4 * x[-3] - 3 * 3 * x[-4] \
                  - 2 * 2 * x[-5]  # 前面都装完后剩余空位数
        if left_11 >= x[0]:
            return num_boxes
        else:
            left_11 = x[0]-left_11 #之前的箱子装满后剩余的1*1个数
            num_boxes += math.ceil(left_11 / 36)
            return num_boxes

    num_boxes = x[-1] + x[-2] + x[-3]
    if x[3]*5>=x[1]:#2*2比4*4的5倍少
        num_boxes+=math.ceil(x[2]/4)#讨论3*3的填充情况，只需把3*3尽量装满即可（因为2*2不单独占用箱子）
        return left_1(num_boxes)
    else:#2*2从4*4溢出
        dict_1 = {1: 5, 2: 3, 3: 1} #key=3*3个数对4取余，value=剩余位置可填充2*2的个数
        left_2= x[1]-5 * x[3] #剩下的2*2个数

        if x[2]%4==0:#3*3的箱子恰好完全装满
            num_boxes += x[2]/4 + math.ceil(x[1]/9)
            return left_1(num_boxes)
        else:
            for key,value in dict_1.items():
                if x[2]%4==key:
                    num_boxes+=x[2]//4+1
                    if left_2<=value:
                        return left_1(num_boxes)
                    else:
                        num_boxes+=math.ceil((left_2-value)/9)
                        return left_1(num_boxes)

for _ in list_1:
    print(int(min_boxes(_)))
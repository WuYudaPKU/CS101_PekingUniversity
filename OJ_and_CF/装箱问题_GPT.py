import math

def min_boxes(order):
    num_boxes = order[-1] + order[-2] + order[-3]  # 初始化箱子数量
    left_1 = 6 * 6 * num_boxes - (order[0] + 5 * 5 * order[-2] +4 * 4 * order[-3] + 3 * 3 * order[-4] + 2 * 2 * order[-5])
    # 计算剩余可填充1*1产品的位置
    if left_1 >= order[0]:
        # 如果剩余位置能够装下1*1产品，直接返回箱子数量
        return num_boxes
    else:
        left_1 = order[0] - left_1
        # 计算剩余无法填充1*1产品的数量
        num_boxes += math.ceil(left_1 / 36)
        # 增加所需的额外箱子数量
        return num_boxes

orders = []
while True:
    order = list(map(int, input().split()))
    if order == [0, 0, 0, 0, 0, 0]:
        break
    orders.append(order)

for order in orders:
    print(min_boxes(order))

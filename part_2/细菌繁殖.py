# 第一个数表示第一天的月份，
# 第二个数表示第一天的日期，
# 第三个数表示第一天细菌的数目，
# 第四个数表示要求的那一天的月份，
# 第五个数表示要求的那一天的日期
times = int(input())
list_1=[]#嵌套列表
for i in range(times):
    list_1.append(list(map(int,input().split())))

def count_months(month):
    if month == 1 or month ==3 or month ==5 or month ==7 or \
            month ==8 or month ==10 or month ==12:
        return 31
    elif month == 2:
        return 28
    else:
        return 30

def numbers(x):#作用对象是列表
    days = 0
    days += x[4] #最后一个月份日期加上
    for i in range(x[0],x[3]):
        days += count_months(i)
    days= days - x[1]
    return x[2]*(2**days)

for _ in list_1:
    print(numbers(_))

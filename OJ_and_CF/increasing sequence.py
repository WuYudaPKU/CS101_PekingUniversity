times = 0
num_d = list(map(int,input().split()))
number = num_d[0]
d = num_d[1]
list_1 = list(map(int,input().split()))
for i in range(1,number):
    while list_1[i-1] >= list_1[i]:
        # i最大取number-1,i+1=number.
        list_1[i] = list_1[i] + d
        times = times + 1
print(int(times))


lines_number = int(input())
list_n = []
for i in range(lines_number):
    list_n.append(int(input()))
list_open = []

def f(n):
    dict_1 = {}
    # round1
    for i in range(1, n + 1):
        dict_1[i] = 1
    for i in range(1,n+1):
        if i % 2 == 0:
            dict_1[i] = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            if dict_1[i]== 1:
                 dict_1[i]=0
            else:
                dict_1[i]=1
    for i in range(1, n + 1):
        if dict_1[i] == 0:
            var = list_open.append(i)
    print(len(list_open))

for i in list_n:
    f(i)

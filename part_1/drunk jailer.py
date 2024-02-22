lines_number = int(input())
list_n = []
list_2 = []
for i in range(lines_number):
    list_n.append(int(input()))

for i in range(lines_number):
    for j in range(2,11):
        if j**2 == i:
            var= list_2.append(i)
print(len(list_2))

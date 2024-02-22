lines_number = int(input())
list_of_n = []
escaped_number_list = []
for i in range(lines_number):
    list_of_n.append(int(input()))
for i in list_of_n:
    for j in range(1,i+1):
        if j**(1/2) %1==0:
            escaped_number_list.append(j)
    print(len(escaped_number_list))
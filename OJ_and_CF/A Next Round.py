number_str = input()
number_list = [int(num) for num in number_str.split()]
result = 0
n = number_list[0]
k = number_list[1]
number_rank_str = input()
number_rank_list = [int(num1) for num1 in number_rank_str.split()]
for i in number_rank_list:
    if i >= number_rank_list[k - 1]:
        result = result + 1
    else:
        result = result
print(result)

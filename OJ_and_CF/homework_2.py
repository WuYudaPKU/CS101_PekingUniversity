all_in = 0
times = int(input())
for i in range(times):
    numbers_str = input()
    numbers_list = [int(num) for num in numbers_str.split()]
    if sum(numbers_list) >= 2:
        all_in = all_in + 1
    else:
        all_in = all_in
print(all_in)
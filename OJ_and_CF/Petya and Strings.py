#2300011119武昱达
string_1 = list(input())
string_2 = list(input())
lower_list_1 = list(letter.upper() for letter in string_1)
lower_list_2 = list(letter.upper() for letter in string_2)
i=0
while i <= len(string_1) and lower_list_1 != lower_list_2:
    if lower_list_1[i] < lower_list_2[i]:
        print("-1")
        break
    elif lower_list_1[i] == lower_list_2[i]:
        i += 1
    else:
        print("1")
        break
else:
    print("0")
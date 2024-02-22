#2300011119武昱达
s = input()
list_s = list(s)
list_hello = []
for letter in list_s:
    if letter != "h":
        list_s.remove(letter)
    else:
        list_hello.append(letter)
        break

for letter in list_s:
    if letter != "e":
        list_s.remove(letter)
    else:
        list_hello.append(letter)
        break

for letter in list_s:
    if letter != "l":
        list_s.remove(letter)
    else:
        list_hello.append(letter)
        break

for letter in list_s:
    if letter != "l":
        list_s.remove(letter)
    else:
        list_hello.append(letter)
        break

for letter in list_s:
    if letter != "o":
        list_s.remove(letter)
    else:
        list_hello.append(letter)
        break

if "".join(list_hello)=="hello":
    print("YES")
else:
    print("NO")
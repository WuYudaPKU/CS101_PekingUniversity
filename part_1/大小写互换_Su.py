# chr()数字转字母   ord()字母转数字
a = list(input())
b = []
b_2=[]
for i in a:
    if ord(i) > 96 and ord(i) <= 122:
        b_2 = b.append(chr(ord(i) - 32))
    elif ord(i) <= 91 and ord(i)>= 65:
        b_2 = b.append(chr(ord(i) + 32))
    else:
        b_2 = b.append(i)
print("".join(b))
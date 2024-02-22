list_1 = []
def f(x):
    num = str(x)
    if num == num[::-1]:
        return True
    else:
        return False
while True:
    try:
        num=input()
        list_1.append(num)
    except EOFError:
        break
for i in list_1:
    if f(i) is True:
        print("YES")
    else:
        print("NO")












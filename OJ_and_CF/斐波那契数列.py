def f(n):
    if n<=2:
        return 1
    else:
        return f(n-1)+f(n-2)
n= int(input())
list_1 = []
for i in range(n):
    num=int(input())
    list_1.append(f(num))
for i in list_1:
    print(i)


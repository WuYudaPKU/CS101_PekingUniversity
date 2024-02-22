distance = int(input())
if distance<=5:
    print("1")
elif distance%5 == 0:
    print(int(distance/5))
else:
    a=distance//5
    print(a+1)
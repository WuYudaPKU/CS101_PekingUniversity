foot = int(input())
if foot%4 == 0:
    minimum=foot//4
    maximum = foot // 2
    print(minimum,maximum)
elif foot%4==2:
    minimum=(foot//4)+1
    maximum = foot // 2
    print(minimum, maximum)
else:
    print(0,0)
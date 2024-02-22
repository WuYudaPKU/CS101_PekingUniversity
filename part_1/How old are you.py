a=int(input())
while True:
    if a%2==0:
        b=a
        a=b//2
        print("{}/2={}".format(b, a))
        if a==1:
            break
    if a%2!=0:
        b=a
        a=b*3+1
        print("{}*3+1={}".format(b, a))
        if a==1:
            break

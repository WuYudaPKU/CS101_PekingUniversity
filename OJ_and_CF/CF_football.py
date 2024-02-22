a=list(input()) #000000011111
flag=0
while a:
    try:
        if flag==6:
            break
        if a[flag] == a[flag+1]:
            flag+=1
        else:
            del a[:flag+1]
            flag=0
    except:
        break
print("YES" if flag==6 else "NO")


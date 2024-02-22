list_a=list(input())
list_upper=[]
list_lower=[]
for i in list_a:
    if ord(i)>=65 and ord(i)<=91:
        list_upper.append(i)
    else:
        list_lower.append(i)
if len(list_lower)>=len(list_upper):

    print("".join(a.lower() for a in list_a))
else:
    print("".join(a.upper() for a in list_a))
list_1 = list(input())
list_1_change=[]
for i in list_1:
    if i.islower is True:
        b=i.upper()
    if i.isupper is True:
        b=i.lower()
print(''.join(list_1_change))
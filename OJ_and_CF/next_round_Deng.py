a = [int(x) for x in input().split()]
d=0
k=a[1]
b=[int(c) for c in input().split()]
for y in b:
    if y!=0 and y>=int(b[k-1]):

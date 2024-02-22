# x=int(input())
# cube=[i**3 for i in range(x+1)]
# for a in range(3,x+1):
#     for b in range(2,a):
#         for c in range(b,a):
#             for d in range(c,a):
#                 if cube[a] ==cube[b]+cube[c]+cube[d]:
#                     print("Cube = "+str(a)+", Triple = ("+str(b)+","+str(c)+","+str(d)+")")

#以下是第二种优化方案
n=int(input())
import math
for a in range(2,n+1):
    for b in range(2,int(math.pow(a**3/3,1/3))+1):
        for c in range(b,int(math.pow(a**3/2,1/3))+1):
            for d in range(c,a):
                if a**3==b**3+c**3+d**3:
                    print('Cube = '+str(a)+', Triple = ('+str(b)+','+str(c)+','+str(d)+')')
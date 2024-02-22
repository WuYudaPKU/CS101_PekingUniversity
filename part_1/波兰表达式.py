from functools import lru_cache
from collections import deque
a=deque(input().split())
lst=["+","-","*","/"]
c=deque()
for i in a:
    if i in lst:
        c.append(i)
    else:
        c.append(float(i))
c_tuple=tuple(c)
@lru_cache(maxsize=None)
def result(x):
    b=x[0]
    if len(x)==3:
        if b == "+":
            return x[-2]+x[-1]
        if b == "-":
            return x[-2]-x[-1]
        if b == "*":
            return x[-2]*x[-1]
        if b == "/":
            return x[-2]/x[-1]
    flag=1
    while True:
        if x[flag-1] not in lst and x[flag+1] in lst:
            if b=="+":
                return result(x[1:flag+1])+result(x[flag+1:])
            if b=="-":
                return result(x[1:flag+1])-result(x[flag+1:])
            if b=="*":
                return result(x[1:flag+1])*result(x[flag+1:])
            if b=="/":
                return result(x[1:flag+1])/result(x[flag+1:])
        else:
            flag+=1
print(result(c_tuple))
#* - + 34 22 * / 24 11 12 3.5
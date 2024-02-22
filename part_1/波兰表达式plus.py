#* - + 34 22 * / 24 11 12 3.5
from functools import lru_cache
lst=["+","-","*","/"]
a=list(input().split())
c=[]
for i in a:
    if i in lst:
        c.append(i)
    else:
        c.append(float(i))
c_tuple=tuple(c)
@lru_cache(maxsize=128)
def res(x:tuple):
    if len(x)==3:
        b = x[0]
        if len(x) == 3:
            if b == "+":
                return x[-2] + x[-1]
            if b == "-":
                return x[-2] - x[-1]
            if b == "*":
                return x[-2] * x[-1]
            if b == "/":
                return x[-2] / x[-1]
    if len(x)!=3:
        flag=len(x)-1
        while x[flag] not in lst:
            flag-=1
        temp=(res(x[flag:flag+3]),)
        return res(x[:flag]+temp+x[flag+3:])
print(round(res(c_tuple),6))
import math
#判断是否为完全平方数 不是则pass（参考drunkjailor）
def is_perfect(x):
    sqrt=math.sqrt(x)
    if sqrt.is_integer():
        return True
    else:
        return False

#如果是完全平方数，判断因子个数
def Euler_sieve(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return primes
tuple_primes=tuple(Euler_sieve(1000000))

def is_T_primes(x):
    a=int(math.sqrt(x))
    if tuple_primes[a]:
        return True
    else:
        return False

n=int(input())
int_tuple=tuple(map(int,input().split()))
int_set=set(int_tuple)
dict_1={i:is_T_primes(i) for i in int_set}
for i in int_tuple:
        print("YES" if dict_1[i] else "NO")


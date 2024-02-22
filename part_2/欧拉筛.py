def Euler_sieve(n): # n==10
    primes = [True for _ in range(n+1)]
    #[True,...,True]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p): # 4,6,8,10  # 3,6,9
                primes[i] = False
        print(primes)
        p += 1
    return primes[-1]
print(Euler_sieve(1000))
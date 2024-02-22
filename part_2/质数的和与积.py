a=int(input())

def is_prime(n):
    if n <= 1:  # 1及以下的数字不是质数
        return False
    if n <= 3:  # 2和3是质数
        return True
    if n % 2 == 0 or n % 3 == 0:  # 排除能被2或3整除的数
        return False
    i = 5
    while i * i <= n:  # 只需检查到平方根的整数即可
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

"""可以采取一种更简单的写法：
def is_prime(n):
    if n==1:
    return False
    for i in range(1,(n**1/2)//1+1):
        if n%i==0:
            return False
    return True
    
"""

list_prime=[]
for i in range(a):
    if is_prime(i) and is_prime(a-i):
        list_prime.append([i,a-i])

print(max(x[0]*x[1] for x in list_prime))
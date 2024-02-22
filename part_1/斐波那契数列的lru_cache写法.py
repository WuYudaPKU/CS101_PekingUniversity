from functools import lru_cache
@lru_cache(maxsize=20)
def F(x):
    if x<=2:
        return 1
    else:
        return F(x-1)+F(x-2)
print(F(30))
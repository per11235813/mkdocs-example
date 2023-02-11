from functools import lru_cache
from itertools import chain
from math import factorial

@lru_cache
def fac(n):
    return 1 if n < 1 else n*fac(n-1)


for i in range(15):
    print(f"fac({i: >2}): {fac(i): >15} {factorial(i): >15}")

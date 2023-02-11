from functools import lru_cache
from itertools import chain


@lru_cache
def fib(n: int) -> int:
    if n < 2: 
        return n
    else:
        return fib(n-1) + fib(n-2)

@lru_cache
def fib2(n: int) -> int:
    """"Fibonacci function"""
    return n if n < 2 else fib2(n-1) + fib2(n-2)


for i in chain(range(10), range(10, 100, 10)):
    print(f"fib2({i: >2}): {fib2(i): >25}")
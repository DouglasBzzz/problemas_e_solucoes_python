from functools import lru_cache
from typing import Dict
from typing import Generator
memo: Dict[int, int] = {0: 0,1: 1} #casos de base

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

#porem, sem definir um valor de base de parada, nao conseguirmos sequer rodar esse script

def fib2(n:int)->int:
    if n < 2:
        return n
    return fib2(n - 2)+fib2(n - 1) #caso recursivo

def fib3(n:int)->int:
    if n not in memo:
        memo[n] = fib3(n - 1)+fib3(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n:int)->int:
    if n<2: #caso de base
        return n
    return fib4(n-2)+fib4(n-1)

def fib5(n : int) -> int:
    if n == 0 : return 0 #trata um caso especial
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last+next
    return next

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 #caso especial
    if n > 0: yield 1 #caso especial
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next #passo principal dessa geracao

if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))
    print(fib3(50))
    print(fib4(60))
    print(fib5(212))

    for i in fib6(50):
        print(i)
from functools import lru_cache
from typing import Dict
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

if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))
    print(fib3(50))
    print(fib4(60))
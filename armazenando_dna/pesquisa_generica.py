from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar("T")

def busca_linear(iteravel: Iterable[T], chave: T) -> bool:
    for item in iteravel:
        if item == chave:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        pass

    def __lt__(self, other: C) -> bool:
        pass

    def __gt__(self, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self, other: C) -> bool:
        return self < other or self == other

    def __ge__(self, other: C) -> bool:
        return not self < other

def busca_binaria(sequence: Sequence[C], chave: C) -> bool:
    menor_valor: int = 0
    maior_valor: int = len(sequence) - 1
    while menor_valor <= maior_valor: #enquanto houver um espaco para pesquisa
        mediana: int = (menor_valor + maior_valor) // 2
        if sequence[mediana] < chave:
            menor_valor = mediana + 1
        elif sequence[mediana] > chave:
            maior_valor = mediana - 1
        else:
            return True
    return False


if __name__ == "__main__":
    print(busca_linear([1,4,6,7,8,9,45,356,987,341,234,87],356)) #true
    print(busca_binaria(["a", "d", "e", "f", "z"], "f")) #true
    print(busca_binaria(["Douglas", "Anderson", "Geri", "Maicon", "Andrielly", "Ivania"], "Fabiano")) #false

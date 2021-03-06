from typing import TypeVar, Generic, List

T = TypeVar("T")

class Pilha(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def coloca(self, item: T) -> None:
        self._container.append(item)

    def retira(self) -> T:
        return self._container.pop()

    #__repr__ é basicamente o que é exibido quando você dá print numa pilha
    def __repr__(self) -> str:
        return repr(self._container)

numero_de_discos: int = 5
torre_a: Pilha[int] = Pilha()
torre_b: Pilha[int] = Pilha()
torre_c: Pilha[int] = Pilha()


"""
vale ressaltar que a resolucao da torre tem uma funcao que dita o numero maximo de movimentos que podem ser feitos
m = 2^x - 1 = ?

onde
m = numero de movimentos
x = numero de discos presentes nas torres

"""

for i in range(1, numero_de_discos + 1):
    torre_a.coloca(i)

def hanoi(begin: Pilha[int], end: Pilha[int], temp: Pilha[int], n: int) -> None:
    if n == 1:
        end.coloca(begin.retira())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)

if __name__ == "__main__":
    hanoi(torre_a, torre_c, torre_b ,numero_de_discos)
    print(torre_a)
    print(torre_b)
    print(torre_c)
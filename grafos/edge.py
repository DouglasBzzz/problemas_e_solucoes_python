from __future__ import annotations
from dataclasses import dataclass

#uma Edge é como uma conexao entre dois vértices inteiros. Por convencao matemática, U é usado para definir
#o primeiro vértice, e V é utilziado para representar o segundo.
@dataclass
class Edge:
    u: int #o vértice DE
    v: int #o vértice PARA

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"


    def ola_mundo(self):
        print("olá mundo")
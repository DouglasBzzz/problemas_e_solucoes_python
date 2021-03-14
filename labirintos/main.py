# o labirinto deste exemplo diferente do existe no algoritmo de game do pacman, sera uma matriz de cells
# onde para cada " " temos um caminho livre, e para cada "X" temos um caminho fechado.

from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
#from armazenando_dna.pesquisa_generica import dfs, bfs,

class Cell(str, Enum):
    VAZIO = " "
    BLOQUEADO = "X"
    INICIO = "S"
    OBJETIVO = "G"
    CAMINHO = "*"

class LocalizacaoLabirinto(NamedTuple):
    linha: int
    coluna: int

class Labirinto:
    def __init__(self, linhas: int = 10, colunas: int = 10, espacamento: float = 0.2,
                 inicio: LocalizacaoLabirinto = LocalizacaoLabirinto(0,0), objetivo: LocalizacaoLabirinto =
                 LocalizacaoLabirinto(9,9)) -> None:
        # inicia as variaveis basicas
        self._linhas: int = linhas
        self._colunas: int = colunas
        self.inicio: LocalizacaoLabirinto = inicio
        self._objetivo: LocalizacaoLabirinto = objetivo
        #preenche a grande com celulas vazias
        self._grid: List[List[Cell]] = [[Cell.VAZIO for c in range(colunas)] for r in range(linhas)]
        #preenche a grande com celulas bloqueadas
        self._preenche_randomico(linhas, colunas, espacamento)
        #preenche as posicoes finais iniciais e finais
        self._grid[inicio.linha][inicio.coluna] = Cell.INICIO
        self._grid[objetivo.linha][objetivo.coluna] = Cell.OBJETIVO

    def _preenche_randomico(self, linhas: int, colunas: int, espacamento: float):
        for linha in range(linhas):
            for coluna in range(colunas):
                if random.uniform(0, 1.0) < espacamento:
                    self._grid[linha][coluna] = Cell.BLOQUEADO

    def __str__(self) -> str:
        saida: str = ""
        for linha in self._grid:
            saida += "".join([c.value for c in linha]) + "\n"
        return saida

if __name__ == "__main__":
    labirinto: Labirinto = Labirinto()
    print(labirinto)
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
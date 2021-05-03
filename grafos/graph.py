from typing import TypeVar, Generic, List, Optional
from edge import Edge
import pprint

V = TypeVar("V") #tipo dos vértices no grafo

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) #numero de vértices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) #numero de arestas

    #adicionando um vértice ao grafo e devolvendo seu indice
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) #adiciona uma lista vazia que vai conter as arestas
        return self.vertex_count - 1 #devolve o indice do vertice adicionado

    #este eh um grafo nao direcionado
    #portando sempre adicionamos arestas nas duas direcoes
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    #adiciona uma aresta usando indices dos vértices (método auxiliar)
    def add_edge_by_indices(self, u:int, v:int) -> None:
        edge:Edge = Edge(u,v)
        self.add_edge(edge)

    #adiciona uma aresta consultando os indices dos vértices (método auxiliar)
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u,v)

    #encontra o vértice em um indice especifuico
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    #encontra o indice de um vértice no grafo
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    #encontra os vértices aos quais um vértice com determinado indice está conectado
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    #consulta o indice de um vértice e encontra seus vizinhos (método auxiliar)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    #devolve todas as arestas associadas a um vértice em um indice
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    #consulta o indice de um vertice e devolve suas arestas(método auxiliar)
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    #facilita a exibibicao elegante desses grafos
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)} \n"
        return desc

if __name__ == "__main__":
    #ste para uma construcao básica de um grafo
    grafo_de_cidades: Graph[str] = Graph([
        "Porto Alegre", "Florianópolis", "Curitiba", "São Paulo", "Rio de Janeiro",
        "Belo Horizonte", "Campo Grande", "Cuiabá", "Goiânia", "Distrito Federal", "Porto Velho", "Rio Branco",
        "Manaus", "Boa Vista", "Macapá", "Belém", "Palmas", "São Luís", "Teresina", "Fortaleza",
        "Natal", "João Pessoa", "Recife", "Maceió", "Aracaju", "Salvador", "Vitória"
    ])

    grafo_de_cidades.add_edge_by_vertices("Porto Alegre", "Florianópolis")
    grafo_de_cidades.add_edge_by_vertices("Porto Alegre", "Curitiba")
    grafo_de_cidades.add_edge_by_vertices("Florianópolis", "Curitiba")
    grafo_de_cidades.add_edge_by_vertices("Curitiba", "São Paulo")
    grafo_de_cidades.add_edge_by_vertices("Curitiba", "Vitória")
    grafo_de_cidades.add_edge_by_vertices("Curitiba", "Belo Horizonte")
    grafo_de_cidades.add_edge_by_vertices("São Paulo", "Porto Alegre")
    grafo_de_cidades.add_edge_by_vertices("São Paulo", "Manaus")
    grafo_de_cidades.add_edge_by_vertices("São Paulo", "João Pessoa")
    grafo_de_cidades.add_edge_by_vertices("São Paulo", "Vitória")
    grafo_de_cidades.add_edge_by_vertices("São Paulo", "Rio de Janeiro")
    grafo_de_cidades.add_edge_by_vertices("São Paulo", "Salvador")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "São Paulo")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "Macapá")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "Rio Branco")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "Porto Alegre")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "Curitiba")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "Boa Vista")
    grafo_de_cidades.add_edge_by_vertices("Distrito Federal", "Manaus")
    grafo_de_cidades.add_edge_by_vertices("Palmas", "Belém")
    grafo_de_cidades.add_edge_by_vertices("Palmas", "Rio Branco")
    grafo_de_cidades.add_edge_by_vertices("Palmas", "Recife")
    grafo_de_cidades.add_edge_by_vertices("Palmas", "Natal")
    grafo_de_cidades.add_edge_by_vertices("Palmas", "São Luís")

    #print(pprint.PrettyPrinter(grafo_de_cidades))

    #impressao = pprint.PrettyPrinter()

    #impressao.pprint(grafo_de_cidades)

    print(grafo_de_cidades)
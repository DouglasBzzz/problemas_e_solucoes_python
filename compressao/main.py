class GeneCompactado:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # comeca com uma sentinela
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # desloca dois bits para a esquerda
            if nucleotide == "A":  # muda os dois ultimos bits para 00
                self.bit_string |= 0b00
            elif nucleotide == "C":  # muda os odois ultimos para 01
                self.bit_string |= 0b01
            elif nucleotide == "G":  # muda os dois ultimos para 10
                self.bit_string |= 0b10
            elif nucleotide == "T":  # muda os dois ultimos para 11
                self.bit_string |= 0b11

            else:
                raise ValueError(f"Nucleotideo inválido: {nucleotide}")

    def descompacta(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # -1 para excluir a sentinela
            bits: int = self.bit_string >> i & 0b11 #obtem apenas 2 bits relevantes
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: #C
                gene += "C"
            elif bits == 0b10: #G
                gene += "G"
            elif bits == 0b11: #T
                gene += "T"
            else:
                raise ValueError(f"Bits inválidos: {bits}")
        return gene[::-1] #inverte a string usando fatiamento com inversao

    def __str__(self) -> str:
        return self.descompacta()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = "TACGGGTACCAAATTGGGTTTGCAGTACGTACGTAAAGGGTTTAAACCCAAGTAGACT" * 100
    print(f"O gene original tem: {getsizeof(original)} byts")
    comprimido: GeneCompactado = GeneCompactado(original) #compacta
    print(f"o gene comprimido tem: {getsizeof(comprimido.bit_string)} bytes")
    print(comprimido)

    print(f"Genes identicos: {original == comprimido.descompacta()}")

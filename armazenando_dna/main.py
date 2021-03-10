from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] #alias de tipo para códons
Gene = List[Codon] #alias de tipo para genes
gene_str: str = "TACGGGTACCAAATTGGGTTTGCAGTACGTACGTAAAGGGTTTAAACCCAAGTAGACT" * 100

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if(i + 2) >= len(s): #nao avanca para alem do final
            return gene
        # inicializa codon a partir de tres nucleotideos
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon) #adiciona condon em gene
    return gene

meu_gene: Gene = string_to_gene(gene_str)

#print(meu_gene)

def busca_linear(gene: Gene, chave_codon: Codon) -> bool:
    for codon in gene:
        if codon == chave_codon:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(busca_linear(meu_gene, acg)) #deve retornar TRUE
print(busca_linear(meu_gene, gat)) #deve retornar FALSE
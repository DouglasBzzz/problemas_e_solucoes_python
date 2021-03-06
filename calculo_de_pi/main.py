def calcula_pi(n_casas: int) -> float:
    numerador: float = 4.0
    denominador: float = 1.0
    operacao: float = 1.0
    pi: float = 0.0

    for _ in range(n_casas):
        pi += operacao * (numerador / denominador)
        denominador += 2.0
        operacao *= -1.0

    return pi

if __name__ == "__main__":
    print(calcula_pi(10000000))


#método para cacularmos o número de PI baseado na equacao de LEIBNIZ, que diz que a convergencia da série:
"""

pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...

o operador sempre é 4, e o denominar é sempre acrescido de 2. 
aS operacoes sao alternadas, sendo iniciadas por uma subtracao, e seguidas por uma soma.

"""
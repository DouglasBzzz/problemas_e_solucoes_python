from secrets import token_bytes
from typing import Tuple

def chave_aleatoria(length: int) -> int:
    #gera os códigos aleatórios
    tb: bytes = token_bytes(length)
    #converte estes bytes em uma cadeia de bits e a devolve
    return int.from_bytes(tb, "big")

print("Gerando chave básica: ")
print(chave_aleatoria(1))

#a pegada desse algoritmo é a utilizacao do XOR (exclusive OR).

def encripta(original: str) -> Tuple[int, int]:
    chave_original: bytes = original.encode()
    dummy: int = chave_aleatoria(len(chave_original))
    chave_original: int = int.from_bytes(chave_original, "big")
    encriptada: int = chave_original ^ dummy #XOR
    return dummy, encriptada

print("Saída método básico de criptografia para Douglas")
print(encripta("Douglas"))

def descriptogra(key1: int, key2: int) -> str:
    descriptografada: int = key1 ^ key2 #XOR
    temp: bytes = descriptografada.to_bytes((descriptografada.bit_length()+7)//8, "big")
    return temp.decode()

print("saída método descriptografado")
print(descriptogra(25499338998130956,8717988598499455))

if __name__ == "__main__":
    key1, key2 = encripta("One time Pad!")
    resultado: str = descriptogra(key1, key2)
    print(resultado)
import random

def gerar_numeros_aleatorios(N, M):
    if N > M:
        numero_aleatorio = random.randint(M, N)

    else:
        numero_aleatorio = random.randint(N, M)
        
    return numero_aleatorio


N = int(input("Digite o valor de N: "))
M = int(input("Digite o valor de M: "))


numero = gerar_numeros_aleatorios(N, M)
print(f"Número aleatório entre {N} e {M}: {numero}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
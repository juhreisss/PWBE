def eh_impar(numero):
    return numero % 2 != 0

numero = int(input("Digite um número inteiro: "))

if eh_impar(numero):
    print(f"O número {numero} é ímpar.")
else:
    print(f"O número {numero} é par.")
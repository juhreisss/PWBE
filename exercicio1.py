def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

num = int(input("Digite um número inteiro positivo: "))
print("Numero em binário:", decimal_para_binario(num))

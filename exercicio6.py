def numero_digitos(n):
    return len(str(n))


n = int(input("Digite um número inteiro positivo: "))

print(f"O número {n} possui {numero_digitos(n)} dígitos.")

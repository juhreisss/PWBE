valor = int(input("Digite o valor: "))
cedulas = [100, 50, 20, 10, 5, 2, 1]

print("Quantidade mínima de cédulas:")
for cedula in cedulas:
    qtd = valor // cedula
    if qtd > 0:
        print(f"{cedula}: {qtd}")
        valor -= qtd * cedula
def calcular_imc(altura, peso):
    return peso / (altura ** 2)

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
print("Seu IMC é:", calcular_imc (altura, peso))
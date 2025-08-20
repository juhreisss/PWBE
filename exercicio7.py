def volume_cilindro(raio, altura):
    pi = 3.14159
    volume = pi * (raio ** 2) * altura
    return volume


raio = float(input("Digite o raio da base do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

print(f"O volume do cilindro é: {volume_cilindro(raio, altura)}")
def area_circulo(raio):
    pi = 3.14159
    return pi * (raio ** 2)

raio = float(input("Digite o raio do círculo: "))

print(f"A área do círculo é: {area_circulo(raio)}")

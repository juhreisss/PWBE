def raio_circulo(area):
    pi = 3.14159 
    raio = (area / pi) ** 0.5
    return raio


area = float(input("Digite a área do círculo: "))

resultado = raio_circulo(area)
print(f"O raio do círculo com área {area} é: {resultado}")

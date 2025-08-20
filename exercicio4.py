def distancia_pontos(x1, y1, x2, y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return distancia


x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))


resultado = distancia_pontos(x1, y1, x2, y2)
print(resultado)
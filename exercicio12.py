import random

numero_secreto = int(random.random() * 100) + 1

while True:
    palpite = int(input("Adivinhe o número de 1 a 100: "))
    if palpite < numero_secreto:
        print("Maior!")
    elif palpite > numero_secreto:
        print("Menor!")
    else:
        print("Parabéns! Você acertou!")
        break
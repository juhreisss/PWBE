import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while tentativas < 10:
        palpite = int(input("Digite seu palpite (1-100): "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            return
        elif palpite < numero_secreto:
            print("O número é maior!")
        else:
            print("O número é menor!")

    
        inicio_intervalo = max(1, numero_secreto - 10)
        fim_intervalo = min(100, numero_secreto + 10)
        print(f"Dica: o próximo palpite pode estar entre {inicio_intervalo} e {fim_intervalo}.")

    print(f"Suas tentativas acabaram! O número era {numero_secreto}.")
    
jogo_adivinhacao()
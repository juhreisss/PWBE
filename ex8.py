import random

palavras = ["cachorro", "banana", "comida", "escola", "livro", "computador", "pipoqueira", "italia" ]
palavra_secreta = random.choice(palavras)

letras_descobertas = []
tentativas = 8

print("Jogo da forca")

while tentativas > 0:
    palavra_mostrada = ""
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += "_"
    print("Palavra: ", palavra_mostrada)

    if "_" not in palavra_mostrada:
        print("Parabéns, você acertou a palavra:", palavra_secreta)
        break

    letra = input("Digite uma letra: ")

    if letra in letras_descobertas:
        print("Já tentou essa letra. Tenta outra.")
        continue

    if letra in palavra_secreta:
        print("Acertou! a letra ta na palavra")
        letras_descobertas.append(letra)
    else:
        print("Errou!")
        tentativas -= 1
        print("Tentativas restantes:", tentativas)

if "_" in palavra_mostrada:
    print("Você perdeu, a palvra certa era:", palavra_secreta)

            
palavra = input("Digite uma palavra: ")

invertida = ""
for letra in palavra:
    invertida = letra + invertida

if palavra == invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
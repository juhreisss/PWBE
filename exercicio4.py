numero = int(input("Digite um numero para ver a tabuada:"))
print("A tabuada desse numero é:")
for i in range(1, 11):
    resultado = numero * i 
    print("{numero} x {i} = {resultado}")
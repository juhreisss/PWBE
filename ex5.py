numero = input("digite um numero inteiro:" )

if numero:
    numero = int(numero)
    print("Os numeros até", numero)
    for i in range(0, numero + 1):
        print(i)
  
    
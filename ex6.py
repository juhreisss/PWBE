maior = -1 

while True:
    numero = int(input("Digite um numero:" ))
    
    if numero < 0:
        break 
    
    if numero > maior:
     maior = numero
    
    if maior >= 0:
        print("O maior numero digitado foi: ")
    
    
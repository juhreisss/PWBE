numeros = []

for i in range(5):
    numero = float(input(f" Digite o {i+1} numero:"))
    numeros.append(numero)
    
    maior = max(numeros)
    menor = min(numeros)
    
    print(f"O maior numero digitado foi: {maior}")
    print(f"O menor numero digitado foi: {menor}")
    
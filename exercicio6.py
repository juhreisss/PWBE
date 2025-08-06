positivos = 0
for i in range(10):
    numero = float(input(f"Digite o {i+1} numero:"))
    if numero > 0:
        positivos += 1
        
        print(f"Voce diitou {positivos} numeros positivos.")
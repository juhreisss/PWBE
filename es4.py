soma = 0

for i in range(1, 6):
 nota = float(input("Digite sua nota: "))
soma += nota

media = soma / 5 

if media >= 5:
    print("Aprovado")
elif media >= 2.5:
    print(" Recuperação")
else:
    print("Reprovado")
 
    

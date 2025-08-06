notas = []
soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)
    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Média das notas: {media}")
else:
    print("Nenhuma nota foi digitada.")
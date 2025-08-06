n = int(input("Digite quantos termos da sequencia: "))

a, b = 0, 1
print("Sequência de Fibonacci:")
for i in range(n):
    print(a)
    a, b = b, a + b
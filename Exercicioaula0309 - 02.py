class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10  

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * 0.20  


funcionario1 = Funcionario("João", 3000)
gerente1 = Gerente("Maria", 6000)

print(f"Funcionário: {funcionario1.nome} | Salário: {funcionario1.salario} | Bônus: {funcionario1.calcular_bonus()}")
print(f"Gerente: {gerente1.nome} | Salário: {gerente1.salario} | Bônus: {gerente1.calcular_bonus()}")

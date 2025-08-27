class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Marca do carro: {self.marca}")
        print(f"Modelo do carro: {self.modelo}")
        print(f"Ano do carro: {self.ano}")
        print("-" * 40)



class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"Funcionário: {self.nome}, {self.idade} anos - Setor: {self.setor}")
        print("-" * 40)

class Manual:
    def __init__(self, titulo, autor, ano_de_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao

    def informacoes(self):
        print(f"Manual: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_de_publicacao}")
        print("-" * 40)



class Produto:
    def __init__(self, nome_do_produto, preco_unitario, quantidade_disponivel):
        self.nome_do_produto = nome_do_produto
        self.preco_unitario = preco_unitario
        self.quantidade_disponivel = quantidade_disponivel

    def mostrar_estoque(self):
        print(f"Produto: {self.nome_do_produto}")
        print(f"Preço unitário: R$ {self.preco_unitario}")
        print(f"Quantidade disponível: {self.quantidade_disponivel}")
        print("-" * 40)



class Treinamento:
    def __init__(self, titulo, instrutor, duracao):
        self.titulo = titulo
        self.instrutor = instrutor
        self.duracao = duracao

    def descricao(self):
        print(f"Título: {self.titulo}")
        print(f"Instrutor: {self.instrutor}")
        print(f"Duração: {self.duracao} minutos")
        print("-" * 40)


class Aluno:
    def __init__(self, nome, curso, nota_final):
        self.nome = nome
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        resultado = "Aprovado" if self.nota_final >= 7 else "Reprovado"
        print(f"Aluno: {self.nome}")
        print(f"Curso: {self.curso}")
        print(f"Nota Final: {self.nota_final} - {resultado}")
        print("-" * 40)


print("=== FROTA DE VEÍCULOS ===")
carro1 = Carro("Honda", "HRV", 2025)
carro1.detalhes()

carro2 = Carro("Audi", "R8", 2021)
carro2.detalhes()


print("=== FUNCIONÁRIOS ===")
funcionario1 = Pessoa("Murilo", 19, "Produção")
funcionario1.apresentar()

funcionario2 = Pessoa("Julia", 19, "Produto")
funcionario2.apresentar()

funcionario3 = Pessoa("Isabela", 29, "Manutenção")
funcionario3.apresentar()


print("=== MANUAIS TÉCNICOS ===")
manual1 = Manual("Segurança do trabalho", "Julia Reis", 2025)
manual1.informacoes()

manual2 = Manual("Segurança da internet", "Isabela Reis", 2025)
manual2.informacoes()


print("=== PRODUTOS EM ESTOQUE ===")
produto1 = Produto("Prego", 455.89, 1765)
produto1.mostrar_estoque()

produto2 = Produto("Notebook", 20876.00, 12)
produto2.mostrar_estoque()

produto3 = Produto("Teclado", 199.90, 150)
produto3.mostrar_estoque()


print("=== TREINAMENTOS ===")
treinamento1 = Treinamento("Segurança no Trabalho", "Julia Reis", 90)
treinamento1.descricao()

treinamento2 = Treinamento("Segurança na Internet", "Isabela Reis", 70)
treinamento2.descricao()

print("=== ALUNOS NOS CURSOS DE CAPACITAÇÃO ===")
aluno1 = Aluno("Julia", "Teste de software", 9.6)
aluno1.status()

aluno2 = Aluno("Murilo", "Operação de máquinas", 10)
aluno2.status()

aluno3 = Aluno("Isabela", "Logística", 6.4)
aluno3.status()
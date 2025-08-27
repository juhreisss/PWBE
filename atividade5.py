class Treinamento:
    def __init__(self, titulo, instrutor, duracao):
        self.titulo = titulo
        self.instrutor = instrutor
        self.duracao = duracao

    def descricao(self):
        print(f"Título do treinamento: {self.titulo}")
        print(f"Instrutor responsável: {self.instrutor}")
        print(f"Duração: {self.duracao} minutos")


treinamento1 = Treinamento("Segurança no Trabalho", "Julia Reis", 90)
treinamento1.descricao()
treinamento2 = Treinamento("Segurança no Internet", "Isabela Reis", 70)
treinamento2.descricao()
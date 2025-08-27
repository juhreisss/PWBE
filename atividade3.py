class Manual:
    def __init__(self, titulo, autor, ano_de_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao

    def informacoes(self):
        print(f"O manual {self.titulo}, escrito por {self.autor}, foi publicado em {self.ano_de_publicacao}.")


manual1 = Manual("Segurança do trabalho", "julia Reis", 2025)
manual1.informacoes()
manual2 = Manual("Segurança da internet", "Isabela Reis", 2025)
manual2.informacoes()

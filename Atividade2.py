class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome}, tenho {self.idade} anos e trabalho no setor de {self.setor}.")


funcionario1 = Pessoa("Murilo", 19, "Produção")
funcionario1.apresentar()
funcionario2 = Pessoa("Julia", 19, "Produto")
funcionario2.apresentar()
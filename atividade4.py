class Produto:
    def __init__(self, nome_do_produto, preco_unitario, quantidade_disponivel):
        self.nome_do_produto = nome_do_produto
        self.preco_unitario = preco_unitario
        self.quantidade_disponivel = quantidade_disponivel

    def mostrar_estoque(self):
        print(f"Produto: {self.nome_do_produto}, Preço: {self.preco_unitario}, Quantidade em estoque: {self.quantidade_disponivel}.")


produto1 = Produto("Prego", 455.89, 1765)
produto1.mostrar_estoque()
produto2 = Produto("Notebook", 20.876, 12)
produto2.mostrar_estoque()

class Aluno:
    def __init__(self, nome, curso, nota_final):
        self.nome = nome
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        resultado = "Aprovado" if self.nota_final >= 7 else "Reprovado"
        print("Os resultados foram:")
        print(f"Aluno: {self.nome}")
        print(f"Curso: {self.curso}")
        print(f"Nota Final: {self.nota_final} - {resultado}")


aluno1 = Aluno("Julia", "Teste de software", 9.6)
aluno1.status()
aluno2 = Aluno("Murilo", "Operação de maquinas", 10)
aluno2.status()
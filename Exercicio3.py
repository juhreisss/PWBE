class Voador:
    def __init__(self, nome,):
       self.nome = nome

    def voar(self):
        print(f"{self.nome} .. voou")

class Aquatico:
   def __init__(self, nome):
       self.nome = nome

def nadar(self):
      print(f"{self.nome}... nadou")


class Pato(Voador, Aquatico):
    def __init__(self, nome, idade):
     super().__init__(nome)
     self.idade = idade

    def grasna(self):
        print(F"{self.nome} ... gransca quack quack")

        pato1 = Pato("Pato joão", 375)

        pato1.voar()
        pato1.nadar()
        pato1.grasna()
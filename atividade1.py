class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Marca do carro: {self.marca}")
        print(f"Modelo do carro: {self.modelo}")
        print(f"Ano do carro: {self.ano}")


carro1 = Carro("Honda", "HRV", 2025)
carro1.detalhes()

carro2 = Carro("Audi", "R8", 2021)
carro2.detalhes()
 
 
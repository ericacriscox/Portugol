class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def exibir_informacoes(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)        
        print("ano: ", self.ano)

carro1 = Carro("Toyota", "Corolla", "Prata", 2002)
carro2 = Carro("Honda", "Civic", "Preto", 2023)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

input()
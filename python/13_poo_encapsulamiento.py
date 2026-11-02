class Guerrero:
    nombre: str
    __poder: int
    def __init__(self, nombre:str, poder:int):
        self.nombre = nombre
        self.poder = poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("POder ", self.__poder)

    def get_pder(self):
        return self.__pioder

goku = Guerrero("Goku", 9000)
vegeta = Guerrero("Vegeta", 6000)
piccolo = Guerrero("Piccolo", 10000)
roberto = Guerrero("Roberto", 5000)

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
roberto.mostrar_info()

print(goku.nombre())
print(goku.__poder())
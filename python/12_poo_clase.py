class Guerrero:
    nombre: str
    raza: str
    def __init__(self, nombre:str, raza:str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

goku = Guerrero("Goku", "Saiyajin")
vegeta = Guerrero("Vegeta", "Saiyajin")
piccolo = Guerrero("Piccolo", "Namkiano")
roberto = Guerrero("Roberto", "Humnao")

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
roberto.mostrar_info()
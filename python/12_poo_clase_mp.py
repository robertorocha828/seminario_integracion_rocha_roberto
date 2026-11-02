class Aspirante:
    nombre: str
    carrera: str
    def __init__(self, nombre:str, carrera:str):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Carrera ", self.carrera)

roberto = Aspirante("Roberto Rocha", "Desarrollo de Software")
hernan = Aspirante("Hernán Varas", "Mecánica Automotriz")
christian = Aspirante("Christian Cañar", "Electricidad")
josue = Aspirante("Josué Ruiz", "Gastronomía")

roberto.mostrar_info()
hernan.mostrar_info()
christian.mostrar_info()
josue.mostrar_info()
class Aspirante:
    nombre: str
    carrera: str
    def __init__(self, nombre:str, carrera:str):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Carrera ", self.carrera)

class AspiranteBecado(Aspirante):
    def __init__(self, nombre: str, carrera: str, nota: float):
        super().__init__(nombre, carrera)
        self.nota = nota  # nota del examen, sobre 10

    def muestra_nombre(self):
        print("Nombre: ", self.nombre)

    def mostrar_info(self):
        super().mostrar_info()
        print("Nota (sobre 10) ", self.nota)


roberto = AspiranteBecado("Roberto Rocha", "Desarrollo de Software", 9.5)
hernan = Aspirante("Hernán Varas", "Mecánica Automotriz")
christian = Aspirante("Christian Cañar", "Electricidad")
eduardo = AspiranteBecado("Eduardo Pérez", "Gastronomía", 9.0)

roberto.mostrar_info()
hernan.mostrar_info()
christian.mostrar_info()
eduardo.mostrar_info()

roberto.muestra_nombre()
print(isinstance(roberto, Aspirante))

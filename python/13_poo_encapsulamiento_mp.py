class Postulante:
    nombre: str
    __nota_examen: float
    def __init__(self, nombre:str, nota_examen:float):
        self.nombre = nombre
        self.__nota_examen = nota_examen

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Nota del examen (sobre 10) ", self.__nota_examen)

    def get_nota_examen(self):
        return self.__nota_examen

eduardo = Postulante("Eduardo Pérez", 9.0)
josue = Postulante("Josué Ruiz", 6.0)
carlos = Postulante("Carlos Baños", 10.0)
roberto = Postulante("Roberto Rocha", 8.5)

eduardo.mostrar_info()
josue.mostrar_info()
carlos.mostrar_info()
roberto.mostrar_info()

# El nombre es público y se lee directo; la nota se lee con el getter
print(eduardo.nombre)
print(eduardo.get_nota_examen())

# El atributo privado no se puede leer desde afuera
try:
    print(eduardo.__nota_examen)
except AttributeError:
    print("No se puede acceder directamente a __nota_examen")
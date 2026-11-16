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

print(roberto.nombre)
print(roberto.get_nota_examen())



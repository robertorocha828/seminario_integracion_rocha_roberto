print("Funciones")
print("Autor: Roberto Rocha")

def dar_bienvenida():
    print("El Instituto Central Técnico da la bienvenida a los aspirantes")
    print("¡Admisiones 2026!")

dar_bienvenida()
dar_bienvenida()
dar_bienvenida()
dar_bienvenida()

def registrar_asistencia(aspirante):
    print(aspirante, "registra su asistencia al examen")

registrar_asistencia("Roberto Rocha")
registrar_asistencia("Hernán Varas")
registrar_asistencia("Christian Cañar")
registrar_asistencia("Eduardo Pérez")


def calcular_costo(valor_certificado, cantidad):
    total = valor_certificado * cantidad
    return total

resultado = calcular_costo(5,4)
print("El total a pagar de Roberto Rocha es:", resultado, "USD")

resultado = calcular_costo(5,10)
print("El total a pagar de Josué Ruiz es:", resultado, "USD")

def evaluar_admision(nombre, nota):
    if nota >= 7:
        print(f"{nombre} aprobó la admisión al instituto")
    else:
        print(f"{nombre} necesita mejorar su nota")

evaluar_admision("Carlos Baños", 6.5)
evaluar_admision("Camila Andrade", 9.5)

nombre_aspirante : str = "Hernán Varas"
edad : int = 19
nota_examen : float = 8.5
esta_admitido : bool = True

def calcular_promedio(nota_examen: float, nota_entrevista: float) -> float:
    return (nota_examen + nota_entrevista) / 2

promedio: float = calcular_promedio(9.0, 8.0)
print("Promedio calculado", promedio)
print("Funciones")
print("Autor: Roberto Rocha")

def kamehameha():
    print("Goku concentra su energia")
    print("kamehameha")

kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Roberto")
atacar("Carlos")
atacar("Rocha")
atacar("Delgado")


def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio

resultado = calcular_poder(4,26)
print("El poder de Roberto Rocha es:", resultado)

resultado = calcular_poder(45,26)
print("El poder de Goku es:", resultado)

def transformar_saiyajin(nombre, poder):
    if poder > 9000:
        print(f"Transformacion de {nombre} a SuperSaiyajin exitosa")
    else:
        print(f"{nombre} Necesitas aumentar tu poder")

transformar_saiyajin("Roberto Rocha", 5000)
transformar_saiyajin("Gohan", 15000)

nombre_personaje : str = "Goku"
edad : int = 33
altura : float = 1.74
es_activo : bool = True

def multiuplicador_poder(entrenamiento: float, edad: int) -> float:
    return entrenamiento*edad

poder: float = multiuplicador_poder(15.5,2)
print("POder calculado", poder)
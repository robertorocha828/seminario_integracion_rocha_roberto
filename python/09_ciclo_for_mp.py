for pregunta in range(1,6):
    print("Roberto Rocha responde la pregunta",pregunta)

for numero in range(1,11):
    print("Certificados", numero, "x 5 USD =", 5*numero, "USD")

for numero in range(1,11,2):
    print("Certificados", numero, "x 5 USD =", 5*numero, "USD")

aspirantes = [
    {"id": 1, "nombre": "Roberto Rocha", "carrera": "Desarrollo de Software", "estado": "Admitido"},
    {"id": 2, "nombre": "Hernán Varas", "carrera": "Mecánica Automotriz", "estado": "Admitido"},
    {"id": 3, "nombre": "Christian Cañar", "carrera": "Electricidad", "estado": "En espera"},
]
print("Lista de aspirantes")
for aspirante in aspirantes:
    print(f"{aspirante['id']} - nombre : {aspirante['nombre']}")

nombres = ["Eduardo Pérez", "Josué Ruiz", "Carlos Baños"]
for nombre in nombres:
    print("Nombre actual: ", nombre)

notas = {
    "Roberto Rocha" : 9.5,
    "Joselyn Quishpe" : 8.0,
    "Daniela Loor" : 8.0,
    "Kevin Chicaiza" : 6.5
}

for nombre, nota in notas.items():
    if nota >= 9:
        print(nombre, "accede a la beca de excelencia")
    else:
        print(nombre, "necesita mejorar su nota")


print("Ciclo for anidado")
aspirantes = ["Roberto Rocha", "Hernán Varas", "Christian Cañar", "Camila Andrade", "Mateo Pazmiño"]
for aspirante in aspirantes:
    print("Turno de: ", aspirante)
    for etapa in range(1,4):
        print("Etapa: ",etapa)

print("Break y continue ")
for aspirante in aspirantes:
    if (aspirante == "Camila Andrade"):
        break
    if (aspirante == "Hernán Varas"):
        continue
    print("Aspirante", aspirante)
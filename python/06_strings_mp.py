nombre1 = "Camila Andrade"
print(f"Aspirante 1: {nombre1}")
print(f"Tipo de dato: {type(nombre1)}")
nombre2 = "Joselyn Quishpe"
print(f"Aspirante 2: {nombre2}")
print(f"Tipo de dato: {type(nombre2)}")


print("Funciones comunes de texto")
carrera_1 = "Gastronomía"
carrera_2 = "Electricidad"
longitud_carrera_1=len(carrera_1)
longitud_carrera_2=len(carrera_2)
print("nombre carrera 1", carrera_1)
print("Longitud carrera 1", longitud_carrera_1)
print("nombre carrera 2", carrera_2)
print("Longitud carrera 2", longitud_carrera_2)


print("Convertir Mayúsculas y minúsculas")
mensaje = "El Instituto Central Técnico abre las inscripciones en Quito"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje Original", mensaje)
print("Mensaje en Mayúsculas", mensaje_mayuscula)
print("Mensaje en Minúsculas", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "La entrevista de admisión será en Ambato"
nuevo_mensaje = mensaje.replace("Ambato", "Cuenca")
print("Mensaje Original", mensaje)
print("Mensaje Reemplazado", nuevo_mensaje)

print("Separación de cadenas en un arreglo")
ciudades = "Quito, Ambato,Cuenca"
print("ciudades: ", ciudades)
lista_ciudades = ciudades.split(",")
print(lista_ciudades)
print("Primera ciudad: ", lista_ciudades[0])
print("Segunda ciudad sin espacios: ", lista_ciudades[1].strip())

print("Extraer subcadenas")
mensaje = "Bienvenida Camila a la carrera de Desarrollo de Software"
aspirante = mensaje[11:17]
sustantivo = mensaje[23:30]
print("aspirante es: ", aspirante)
print("sustantivo es: ", sustantivo)


print("Comprobaciones útiles")
codigo="INS2026"
numero="2026"
nombre="Instituto Japón"
identificador="SOFT01"
print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())###### Funciones comunes de las variables string
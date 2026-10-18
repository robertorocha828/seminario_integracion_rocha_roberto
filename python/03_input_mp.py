print("Incluir datos con Input")
nombre=input("¿Cuál es tu nombre? ")
print("Hola", nombre, "!")
print("Bienvenido al Instituto Central Técnico de Quito")
print("Hasta luego "+nombre)


cantidad=int(input("¿Cuántos aspirantes hay en la fila? "))
total=cantidad+2
print("Aspirantes totales: ",total)

print("Conversiones")
print("==== Secretaría de Admisiones ====")
nombre_aspirante=input("Nombre del aspirante: ")
valor_certificado=float(input("Valor del certificado de notas (USD): "))
cantidad=int(input("Cantidad de certificados: "))
total= cantidad * valor_certificado
print("Total a pagar: ",total)
print("Total a pagar (round): ", round(total,2))
print(f"Total a pagar (f): ${total:.2f}")
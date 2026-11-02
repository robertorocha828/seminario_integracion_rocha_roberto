nota_simulacro = 2
while nota_simulacro < 10:
    print("Hernán Varas está practicando para el examen, su nota de simulacro es", nota_simulacro)
    nota_simulacro += 2

print("¡Hernán Varas alcanzó la nota objetivo!")

cupos_disponibles = 40
while cupos_disponibles > 0:
    print("Quedan", cupos_disponibles, "cupos en Desarrollo de Software")
    cupos_disponibles -=5
print("Se agotaron los cupos")

print("Continue y break")
dia = 0
while dia < 10:
    dia +=1
    if dia == 4:
        print("Día 4: Josué Ruiz entrega sus documentos")
        continue
    print("Día ", dia, "Josué Ruiz asiste a las tutorías")
    if dia == 8:
        print("Fin del proceso de inscripción")
        break

aulas = [1,2,3,4,5,6,7,8,9,10]
for aula in aulas:
    if aula == 3:
        print("Aula 3 cerrada por mantenimiento")
        continue
    if aula == 7:
        print("Carlos Baños encuentra su aula de examen")
        break
    else:
        print("Revisando el aula", aula)
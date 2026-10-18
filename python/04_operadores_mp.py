print("OPERADORES")
print("Operadores aritméticos")
aspirantes = 17
comisiones = 5
print("Hay 17 aspirantes y 5 comisiones de entrevista")
print("+ Suma: ", aspirantes, "+" , comisiones,"=",aspirantes+comisiones)
print("- Resta: ", aspirantes, "-" , comisiones,"=",aspirantes-comisiones)
print("* Multiplicación: ", aspirantes, "*" , comisiones,"=",aspirantes*comisiones)
print("/ División: ", aspirantes, "/" , comisiones,"=",aspirantes/comisiones)
print("// División entera (aspirantes por comisión): ", aspirantes, "//" , comisiones,"=",aspirantes//comisiones)
print("% Residuo (aspirantes que sobran): ", aspirantes, "%" , comisiones,"=",aspirantes%comisiones)
print("** Potencia (resultados posibles de 3 etapas aprobadas o no): ", 2, "**" , 3,"=",2**3)

print("Tabla de multiplicar del 5 (certificados de 5 USD cada uno)")
print(5, "x", 1, "=", 5*1)
print(5, "x", 2, "=", 5*2)
print(5, "x", 3, "=", 5*3)
print(5, "x", 4, "=", 5*4)
print(5, "x", 5, "=", 5*5)
print(5, "x", 6, "=", 5*6)
print(5, "x", 7, "=", 5*7)
print(5, "x", 8, "=", 5*8)
print(5, "x", 9, "=", 5*9)
print(5, "x", 10, "=", 5*10)

print("OPERADORES DE COMPARACION")
nota_minima = 7
nota_camila = 9.5
nota_mateo = 6
print("Nota mínima:", nota_minima, "| Camila Andrade:", nota_camila, "| Mateo Pazmiño:", nota_mateo)
print("== Igual a : ", nota_minima, "==", 7, nota_minima==7)
print("== Igual a : ", nota_mateo, "==", nota_minima, nota_mateo==nota_minima)
print("!= Diferente de : ", nota_mateo, "!=", nota_minima, nota_mateo!=nota_minima)
print("!= Diferente de : ", nota_minima, "!=", 7, nota_minima!=7)
print("> Mayor que: ", nota_camila, ">", nota_minima, nota_camila>nota_minima)
print("> Mayor que: ", nota_mateo, ">", nota_minima, nota_mateo>nota_minima)
print("< Menor que: ", nota_mateo, "<", nota_minima, nota_mateo<nota_minima)
print("< Menor que: ", nota_camila, "<", nota_minima, nota_camila<nota_minima)
print(">= Mayor o igual que: ", nota_camila, ">=", nota_minima, nota_camila>=nota_minima)
print(">= Mayor o igual que: ", nota_mateo, ">=", nota_minima, nota_mateo>=nota_minima)
print("<= Menor o igual que: ", nota_mateo, "<=", nota_minima, nota_mateo<=nota_minima)
print("<= Menor o igual que: ", nota_camila, "<=", nota_minima, nota_camila<=nota_minima)

print("OPERADORES LÓGICOS")
edad_camila = 18
print("Operador and : (nota_camila>=nota_minima)and(edad_camila>=17)", (nota_camila>=nota_minima)and(edad_camila>=17))
print("Operador and : (nota_camila>=nota_minima)and(edad_camila>=20)", (nota_camila>=nota_minima)and(edad_camila>=20))
print("Operador or : (nota_camila>=nota_minima)or(nota_mateo>=nota_minima)", (nota_camila>=nota_minima)or(nota_mateo>=nota_minima))
print("Operador or : (nota_camila<nota_minima)or(nota_mateo>=nota_minima)", (nota_camila<nota_minima)or(nota_mateo>=nota_minima))
print("Operador not : not (nota_mateo>=nota_minima)", not (nota_mateo>=nota_minima))
print("Operador not : not (nota_camila>=nota_minima)", not (nota_camila>=nota_minima))


tiene_documentos = True
inscripciones_abiertas = True
puede_inscribirse = tiene_documentos and inscripciones_abiertas
print("¿Puede inscribirse? ", puede_inscribirse)


es_abanderado = True
promedio_alto = False
acceso_beca = es_abanderado or promedio_alto
print("¿Accede a beca?", acceso_beca)
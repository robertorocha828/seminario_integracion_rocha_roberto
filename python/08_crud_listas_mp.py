print("CRUD DE EstudianteS EN PYTHON")
Estudiantes = [
    {"id": 1, "nombre": "Camila Andrade", "carrera": "Desarrollo de Software", "nota": 9.2, "estado": "Admitido"},
    {"id": 2, "nombre": "Joselyn Quishpe", "carrera": "Enfermería", "nota": 8.7, "estado": "Admitido"},
    {"id": 3, "nombre": "Mateo Pazmiño", "carrera": "Mecánica Automotriz", "nota": 7.1, "estado": "En espera"},
]
id_publico = 4

def pedir_nota(mensaje):
    # La nota del examen debe estar entre 0 y 10
    try:
        nota = float(input(mensaje).replace(",", "."))
    except ValueError:
        return None
    if 0 <= nota <= 10:
        return nota
    return None

def create():
    global id_publico
    print("Registrar Estudiante")
    nombre = input("Nombre del Estudiante: ")
    carrera = input("Carrera: ")
    nota = pedir_nota("Nota del examen (sobre 10): ")
    if nota is None:
        print("Nota inválida, debe estar entre 0 y 10")
        return
    estado = input("Estado (Admitido, En espera, Rechazado): ")
    nuevo_Estudiante = {
        "id": id_publico,
        "nombre": nombre,
        "carrera": carrera,
        "nota": nota,
        "estado": estado
    }
    Estudiantes.append(nuevo_Estudiante)
    id_publico += 1
    print("Creado")

def read():
    print("Lista de Estudiantes")
    for Estudiante in Estudiantes:
        print(f"{Estudiante['id']} - nombre: {Estudiante['nombre']} - {Estudiante['carrera']} - nota: {Estudiante['nota']}/10 - {Estudiante['estado']}")

def update():
    print("Actualizar Estudiante")
    try:
        id_update = int(input("id a modificar: "))
    except ValueError:
        print("El id debe ser un número")
        return
    for Estudiante in Estudiantes:
        if Estudiante["id"] == id_update:
            Estudiante["nombre"] = input("Nuevo nombre: ")
            Estudiante["carrera"] = input("Nueva carrera: ")
            nota = pedir_nota("Nueva nota (sobre 10): ")
            if nota is None:
                print("Nota inválida, debe estar entre 0 y 10")
                return
            Estudiante["nota"] = nota
            Estudiante["estado"] = input("Nuevo estado: ")
            print("Actualizado")
            return
    print("No existe un Estudiante con ese id")

def delete():
    print("Eliminar Estudiante")
    try:
        id_delete = int(input("id a borrar: "))
    except ValueError:
        print("El id debe ser un número")
        return
    for Estudiante in Estudiantes:
        if Estudiante["id"] == id_delete:
            Estudiantes.remove(Estudiante)
            print("Estudiante eliminado")
            return
    print("No existe un Estudiante con ese id")

def menu():
    while True:
        print("Admisión - Estudiantes")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Salir")
        option = input("Seleccione 1 al 5: ")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Cerrando sistema")
            break
        else:
            print("Intente nueva opción")

if __name__ == "__main__":
    menu()
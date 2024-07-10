# Sistema de Gestión de Estudiantes y Cursos

# Datos iniciales
estudiantes = []
cursos = []
registro_estudiantes_cursos = {}

# Menú del sistema
def mostrar_menu():
    print("\nMenú del Sistema de Gestión de Estudiantes y Cursos")
    print("1. Agregar Estudiante")
    print("2. Eliminar Estudiante")
    print("3. Agregar Curso")
    print("4. Eliminar Curso")
    print("5. Inscribir Estudiante en Curso")
    print("6. Consultar Cursos de un Estudiante")
    print("7. Listar Estudiantes")
    print("8. Listar Cursos")
    print("9. Salir")

# Funciones del sistema
def agregar_estudiante():
    nombre = input("Nombre del Estudiante: ")
    edad = int(input("Edad del Estudiante: "))
    id_estudiante = input("ID del Estudiante: ")

    for estudiante in estudiantes:
        if estudiante[2] == id_estudiante:
            print("El ID del estudiante ya existe.")
            return

    estudiantes.append((nombre, edad, id_estudiante))
    registro_estudiantes_cursos[id_estudiante] = set()
    print("Estudiante agregado con éxito.")

def eliminar_estudiante():
    id_estudiante = input("ID del Estudiante a eliminar: ")

    for estudiante in estudiantes:
        if estudiante[2] == id_estudiante:
            estudiantes.remove(estudiante)
            del registro_estudiantes_cursos[id_estudiante]
            print("Estudiante eliminado con éxito.")
            return

    print("El estudiante no existe.")

def agregar_curso():
    nombre_curso = input("Nombre del Curso: ")
    codigo_curso = input("Código del Curso: ")

    for curso in cursos:
        if curso[1] == codigo_curso:
            print("El código del curso ya existe.")
            return

    cursos.append((nombre_curso, codigo_curso))
    print("Curso agregado con éxito.")

def eliminar_curso():
    codigo_curso = input("Código del Curso a eliminar: ")

    for curso in cursos:
        if curso[1] == codigo_curso:
            cursos.remove(curso)
            for id_estudiante in registro_estudiantes_cursos:
                registro_estudiantes_cursos[id_estudiante].discard(codigo_curso)
            print("Curso eliminado con éxito.")
            return

    print("El curso no existe.")

def inscribir_estudiante_en_curso():
    id_estudiante = input("ID del Estudiante: ")
    codigo_curso = input("Código del Curso: ")

    if id_estudiante not in registro_estudiantes_cursos:
        print("El estudiante no existe.")
        return

    for curso in cursos:
        if curso[1] == codigo_curso:
            registro_estudiantes_cursos[id_estudiante].add(codigo_curso)
            print("Estudiante inscrito en el curso con éxito.")
            return

    print("El curso no existe.")

def consultar_cursos_estudiante():
    id_estudiante = input("ID del Estudiante: ")

    if id_estudiante in registro_estudiantes_cursos:
        cursos_inscritos = registro_estudiantes_cursos[id_estudiante]
        if cursos_inscritos:
            print("Cursos inscritos por el estudiante:")
            for codigo_curso in cursos_inscritos:
                for curso in cursos:
                    if curso[1] == codigo_curso:
                        print(curso[0])
        else:
            print("El estudiante no está inscrito en ningún curso.")
    else:
        print("El estudiante no existe.")

def listar_estudiantes():
    if estudiantes:
        print("Lista de Estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante[0]}, Edad: {estudiante[1]}, ID: {estudiante[2]}")
    else:
        print("No hay estudiantes registrados.")

def listar_cursos():
    if cursos:
        print("Lista de Cursos:")
        for curso in cursos:
            print(f"Nombre: {curso[0]}, Código: {curso[1]}")
    else:
        print("No hay cursos disponibles.")

# Bucle principal del sistema
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        eliminar_estudiante()
    elif opcion == "3":
        agregar_curso()
    elif opcion == "4":
        eliminar_curso()
    elif opcion == "5":
        inscribir_estudiante_en_curso()
    elif opcion == "6":
        consultar_cursos_estudiante()
    elif opcion == "7":
        listar_estudiantes()
    elif opcion == "8":
        listar_cursos()
    elif opcion == "9":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
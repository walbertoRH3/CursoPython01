#Sistema de Gestion de estudiantes y cursos
#Datos Iniciales
estudiantes = []
cursos = []
registro_estudiantes_curso = {}  #En este diccionario alamcenaremos los estudiantes y los cursos

#Menu del sistema
def mostrar_menu():
    print("\n***********************")
    print("Menu del sistema de Gestion de estudiantes y cursos")
    print("1. Agregar un estudiante")
    print("2. Eliminar un estudiante")
    print("3. Agregar un curso")
    print("4. Eliminar un curso")
    print("5. Inscribir un estudiante en un curso")
    print("6. Consultar cursos de un estudiante")
    print("7. Listar Estudaintes")
    print("8. Listar Cursos")
    print("9. Salir")

#Funciones d emi sistema
def agregar_estudiante():
    nombre = input("Nombre del Estudiante: ")
    edad = int(input("Edad del Estudiante: "))
    id_estudiante = input("ID del Estudiante: ")

    for estudiante in estudiantes:
        if estudiante[2] == id_estudiante:
            print("El ID del estudiante ya existe!")
            break

    estudiantes.append((nombre, edad, id_estudiante))
    registro_estudiantes_curso[id_estudiante] = set() #---->
    print("Estudiante agregado con Exito...")

def eliminar_estudiante():
    id_estudiante = input("ID del Estudiante a eliminar: ")
    
    for estudiante in estudiantes:
        if estudiante[2] == id_estudiante:
            estudiantes.remove(estudiante)
            del registro_estudiantes_curso[id_estudiante]
            print("Estudiante eliminado con exito")
            break
    
    print("El estudiante no existe...")

def agregar_curso():
    nombre_curso = input("Nombre del Curso: ")
    codigo_curso = input("Codigo Curso:" )

    for curso in cursos:
        if curso[1] == codigo_curso:
            print("El Curso ya existe!")
            break
    
    cursos.append((nombre_curso, codigo_curso))
    print("Curso Agregado con Exito.")

def eliminar_curso():
    codigo_curso = input("Codigo del Curso a Eliminar: ")

    for curso in cursos:
        if curso[1] == codigo_curso:
            cursos.remove(curso)
            for id_estudiante in registro_estudiantes_curso:
                registro_estudiantes_curso[id_estudiante].discard(codigo_curso)
            print("Curso eliminado con Exito")
            break
    print("El curso no existe!")

def inscribir():
    id_estudiante = input("ID del Estudiante: ")
    codigo_curso = input("Codigo del curso: ")

    if id_estudiante not in registro_estudiantes_curso:
        print("El estudiante no existe: ")
        return
    
    for curso in cursos:
        if curso[1] == codigo_curso:
            registro_estudiantes_curso[id_estudiante].add(codigo_curso)
            print("Estudiante Inscrito en el curso con exito...")
            break
    print("El curso no existe!")

def consultar_cursos():
    id_estudiante = input("ID del Estudiante: ")

    if id_estudiante in registro_estudiantes_curso:
        cursos_inscrito = registro_estudiantes_curso[id_estudiante]
        if cursos_inscrito:
            print("Cursos en los que el estudiante esta inscrito: ")
            for codigo_curso in cursos_inscrito:
                for curso in cursos:
                    if curso[1] == codigo_curso:
                        print(curso[0])
        else:
            print("El estudiante no esta inscrito en ningun curso")
    else:
        print("El estudainte no existe!")

def listar_estudiantes():
    if estudiantes:
        print("Lista de Estudiantes: ")
        for estudiante in estudiantes:
            print("Nombre: {} ,Edad: {} , ID: {}".format(estudiante[0], estudiante[1], estudiante[2]))
    else:
        print("No hay estudiantes registrados")

def listar_cursos():
    if cursos:
        print("Lista d eCursos: ")
        for curso in cursos:
            print("Nombre: {} , Codigo: {}".format(curso[0], curso[1]))
    else:
        print("No hay cursos disponibles!")

#bucle principal del Sistema
while True:
    mostrar_menu()
    print("-------^^^---------")
    opcion = int(input("Seleccione una opcion valida: "))

    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        eliminar_estudiante()
    elif opcion == 3:
        agregar_curso()
    elif opcion == 4:
        eliminar_curso()
    elif opcion == 5:
        inscribir()
    elif opcion == 6:
        consultar_cursos()
    elif opcion == 7:
        listar_estudiantes()
    elif opcion == 8:
        listar_cursos()
    elif opcion == 9:
        print("Saliendo del Sistema....")
        break
    else:
        print("Opcion invalida! Intentalo de nuevo.")
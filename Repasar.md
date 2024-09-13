def ingresarestudiantes(dicDatos)
dni=input("ingrese su dni: ")
     apellido=input("ingrese su apellido: ")
     nombre=input("ingrese su nombre: ")
     aNac=int(input("ingrese el año de nacimiento: "))
     dicDatos[dni]={"apellido":apellido
               "nombre":nombre
               "aNac":aNac
               }
     GuardarDatos(dicDatos)
return
def menu():
    print("\n--  Menu  --")
    print("precione 1 para añadir estudiante")
    print("precione 2 para listar")
    print("precione 3 para salir")
    op=input("Seleccione una opcion:  ")
    return op
def listar(dicLegajos):
    limpiarpantalla()
    print("listado de estudiantes".center(60," "))
    print("-"*60)
    for dni, datos in dicLegajos.item():
        print(f"dni: {dni}")
        print(f"apellido {datos("apellido")}")
        print(f"nombre {datos("nombre")}")
        print(f"año de nacimiento{datos("aNac")}")
def limpiarpantalla():
    os.system("cls")

legajos=Cargardatos():
while True:
    opcion=menu()
    if opcion== "0":
        break
    elif opcion== "1":
        ingresarestudiantes(legajos)
    elif opcion== "2":
        listar(legajos)
    else:
        print("opcion no valida")

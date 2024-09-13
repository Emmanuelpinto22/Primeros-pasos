
print("******************************")
print("***       Bienvenidos      ***")
print("***      a AppleStore      ***")
print("******************************")
print(" ")
print("ingresa tu nombre")
nombre = input()
print("ingresa tu apellido")
apellido = input()
nom_completo = nombre + " " + apellido
precio_manzanas= 5

# Definir los precios de los tipos de manzanas
precio_manzana_roja = 5
precio_manzana_verde = 5
precio_manzana_amarilla = 5

# Definir las cantidades iniciales de cada tipo de manzana
cantidad_manzanas_rojas = 8
cantidad_manzanas_verdes = 15
cantidad_manzanas_amarillas = 10

# Definir el total inicial
total = 33

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Comprar manzanas")
    print("2. Ver cantidad de manzanas disponibles")
    print("3. Ver total")
    print("4. Salir")

    # Pedir al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Opción 1: Comprar manzanas
    if opcion == "1":
        print("\n--- Tipos de manzanas ---")
        print("1. Manzanas rojas")
        print("2. Manzanas verdes")
        print("3. Manzanas amarillas")

        tipo_manzana = input("Seleccione el tipo de manzana: ")

        if tipo_manzana == "1":
            cantidad = int(input("Ingrese la cantidad de manzanas rojas que desea comprar: "))
            if cantidad <= cantidad_manzanas_rojas:
                total += cantidad * precio_manzana_roja
                cantidad_manzanas_rojas -= cantidad
            else:
                print("Lo sentimos, no hay suficientes manzanas rojas disponibles.")

        elif tipo_manzana == "2":
            cantidad = int(input("Ingrese la cantidad de manzanas verdes que desea comprar: "))
            if cantidad <= cantidad_manzanas_verdes:
                total += cantidad * precio_manzana_verde
                cantidad_manzanas_verdes -= cantidad
            else:
                print("Lo sentimos, no hay suficientes manzanas verdes disponibles.")

        elif tipo_manzana == "3":
            cantidad = int(input("Ingrese la cantidad de manzanas amarillas que desea comprar: "))
            if cantidad <= cantidad_manzanas_amarillas:
                total += cantidad * precio_manzana_amarilla
                cantidad_manzanas_amarillas -= cantidad
            else:
                print("Lo sentimos, no hay suficientes manzanas amarillas disponibles.")

        else:
            print("Opción inválida. Por favor, seleccione un tipo de manzana válido.")

    # Opción 2: Ver cantidad de manzanas disponibles
    elif opcion == "2":
        print(f"\n--- Cantidad de manzanas disponibles ---")
        print(f"Manzanas rojas: {cantidad_manzanas_rojas}")
        print(f"Manzanas verdes: {cantidad_manzanas_verdes}")
        print(f"Manzanas amarillas: {cantidad_manzanas_amarillas}")

    # Opción 3: Ver total
    elif opcion == "3":
        print(f"\n--- Total ---")
        print(f"El total es: ${total:.2f}")

    # Opción 4: Salir
    elif opcion == "4":
        print("Gracias por visitarnos!")
        break

    # Opción inválida
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
# Lista de paquetes turísticos
paquetes_turisticos = [{
        'id': 1,  # Se asigna el primer ID
        'destino': "Amazonas",  # Destino del paquete
        'nombre': "Aventura en la Selva",  # Nombre del paquete
        'descripcion': "Exploración de la selva amazónica",  # Descripción del paquete
        'precio': 1200,  # Precio del paquete
        'actividades': ["Senderismo", "Observación de aves"],  # Lista de actividades del paquete
        'itinerario': {  # Itinerario por días
            1: ["Llegada a la ciudad", "Tour por la selva"],
            2: ["Senderismo en la selva", "Visita a comunidades indígenas"]
        }
    },
    {
        'id': 2,
        'destino': "Caribe",  # Destino del paquete
        'nombre': "Playa Caribe",
        'descripcion': "Relajación en playas caribeñas",
        'precio': 800,
        'actividades': ["Snorkel", "Tirolesa"],
        'itinerario': {
            1: ["Llegada al hotel", "Tiempo libre en la playa"],
            2: ["Excursión en barco", "Snorkel y buceo"]
        }
    },
    {
        'id': 3,
        'destino': "Andes",
        'nombre': "Cultura Andina",
        'descripcion': "Visita a las maravillas de los Andes",
        'precio': 1500,
        'actividades': ["Senderismo", "Visita a ruinas", "Degustación de comida típica"],
        'itinerario': {
            1: ["Llegada a la ciudad", "Recorrido por el mercado local", "Cena tradicional"],
            2: ["Visita a ruinas arqueológicas", "Almuerzo con comida típica", "Tarde libre para explorar"],
            3: ["Senderismo en la montaña", "Cena de despedida", "Regreso al hotel"]
        }
    }]
id_paquete = 4

# Validación para entradas no vacías
def validar_entrada_no_vacia(entrada):
    return len(entrada.strip()) > 0

# Validación para verificar que el texto no contenga números
def validar_entrada_sin_numeros(texto):
    if any(char.isdigit() for char in texto):  # Verifica si hay algún dígito en el texto
        print("La entrada no debe contener números.")
        return False
    return True

# Validación del precio (debe ser un número válido y positivo)
def validar_precio(precio):
    try:
        precio = float(precio)
        if precio <= 0:
            print("El precio debe ser un número positivo.")
            return False
        return True
    except ValueError:
        print("El precio debe ser un número válido.")
        return False

# Validación del ID (verifica que sea un número entero)
def validar_id(id_paquete):
    try:
        return int(id_paquete)
    except ValueError:
        print("El ID debe ser un número entero.")
        return None

# Función para crear un paquete turístico
def crear_paquete(destino, nombre, descripcion, precio, actividades, itinerario):
    global id_paquete
    paquete = {
        "id": id_paquete,
        "destino": destino,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "actividades": actividades,
        "itinerario": itinerario
    }
    paquetes_turisticos.append(paquete)
    id_paquete += 1
    print(f"Paquete '{nombre}' creado exitosamente con ID {paquete['id']}.")

# Función para mostrar todos los paquetes turísticos
def mostrar_paquetes():
    if not paquetes_turisticos:
        print("No hay paquetes disponibles.")
    else:
        for paquete in paquetes_turisticos:
            print("")
            print(f"ID: {paquete['id']}")
            print(f"Destino: {paquete['destino']}")
            print(f"Nombre: {paquete['nombre']}")
            print(f"Descripción: {paquete['descripcion']}")
            print(f"Precio: {paquete['precio']:.2f}")
            print(f"Actividades: {', '.join(paquete['actividades'])}")
            print("Itinerario:")
            for dia, actividades in paquete['itinerario'].items():
                print(f"  Día {dia}: {', '.join(actividades)}")

# Función para mostrar un paquete específico por su ID
def mostrar_paquete_por_id(id_paquete):
    id_valido = validar_id(id_paquete)
    if id_valido is None:
        return  # Si el ID no es válido, se detiene la función

    for paquete in paquetes_turisticos:
        if paquete["id"] == id_valido:
            print(f"\n--- Detalles del Paquete {paquete['id']} ---")
            print(f"Destino: {paquete['destino']}")
            print(f"Nombre: {paquete['nombre']}")
            print(f"Descripción: {paquete['descripcion']}")
            print(f"Precio: ${paquete['precio']:.2f}")
            print(f"Actividades: {', '.join(paquete['actividades'])}")
            print("Itinerario:")
            for dia, actividades in paquete['itinerario'].items():
                print(f"  Día {dia}: {', '.join(actividades)}")
            return

    print(f"Paquete con ID '{id_paquete}' no encontrado.")

# Función para actualizar un paquete
def actualizar_paquete(id_paquete):
    id_valido = validar_id(id_paquete)  # Valida que el ID sea correcto
    if id_valido is None:
        return  # Si el ID no es válido, se detiene la función

    for paquete in paquetes_turisticos:  # Busca el paquete en la lista
        if paquete["id"] == id_valido:
            print(f"Actualizando paquete con ID: {paquete['id']}")
            
            # Destino
            while True:
                nuevo_destino = input(f"Nuevo destino ({paquete['destino']}): ").strip()
                if validar_entrada_no_vacia(nuevo_destino) and validar_entrada_sin_numeros(nuevo_destino):
                    paquete['destino'] = nuevo_destino
                    break
                print("El destino no puede estar vacío y no debe contener números.")

            # Nombre
            while True:
                nuevo_nombre = input(f"Nuevo nombre ({paquete['nombre']}): ").strip()
                if validar_entrada_no_vacia(nuevo_nombre) and validar_entrada_sin_numeros(nuevo_nombre):
                    paquete['nombre'] = nuevo_nombre
                    break
                print("El nombre no puede estar vacío y no debe contener números.")

            # Descripción
            while True:
                nueva_descripción = input(f"Nueva descripción ({paquete['descripcion']}): ").strip()
                if validar_entrada_no_vacia(nueva_descripción) and validar_entrada_sin_numeros(nueva_descripción):
                    paquete['descripcion'] = nueva_descripción
                    break
                print("La descripción no puede estar vacía y no debe contener números.")

            # Precio
            while True:
                nuevo_precio = input(f"Nuevo precio ({paquete['precio']}): ").strip()
                if validar_precio(nuevo_precio):
                    paquete['precio'] = float(nuevo_precio)
                    break

            # Actividades
            while True:
                nuevas_actividades = input(f"Nuevas actividades (separadas por comas, {', '.join(paquete['actividades'])}): ").split(",")
                nuevas_actividades = [a.strip() for a in nuevas_actividades if a.strip()]
                if all(validar_entrada_sin_numeros(a) for a in nuevas_actividades):
                    paquete['actividades'] = nuevas_actividades
                    break
                print("Las actividades no deben contener números.")

            # Actualización del itinerario
            while True:
                print("\n--- Actualización del Itinerario ---")
                print("1. Agregar un día al itinerario")
                print("2. Editar un día del itinerario")
                print("3. Eliminar un día del itinerario")
                print("4. Finalizar actualización del itinerario")
                opcion_itinerario = input("Selecciona una opción: ")

                if opcion_itinerario == "1":
                    dia = int(input("Nuevo día del itinerario: "))
                    actividades_dia = input("Actividades para el día (separadas por comas): ").split(",")
                    paquete['itinerario'][dia] = [a.strip() for a in actividades_dia if a.strip()]

                elif opcion_itinerario == "2":
                    dia = int(input("Día a editar: "))
                    if dia in paquete['itinerario']:
                        actividades_dia = input("Nuevas actividades para el día (separadas por comas): ").split(",")
                        paquete['itinerario'][dia] = [a.strip() for a in actividades_dia if a.strip()]
                    else:
                        print(f"No se encontró el día {dia} en el itinerario.")

                elif opcion_itinerario == "3":
                    dia = int(input("Día a eliminar: "))
                    if dia in paquete['itinerario']:
                        del paquete['itinerario'][dia]
                        print(f"Día {dia} eliminado del itinerario.")
                    else:
                        print(f"No se encontró el día {dia} en el itinerario.")

                elif opcion_itinerario == "4":
                    break

                else:
                    print("Opción inválida. Inténtalo de nuevo.")
            print(f"Paquete '{paquete['nombre']}' actualizado exitosamente.")
            return
    print(f"Paquete con ID '{id_paquete}' no encontrado.")

# Función para eliminar un paquete turístico por su ID
def eliminar_paquete(id_paquete):
    id_valido = validar_id(id_paquete)
    if id_valido is None:
        return  # Si el ID no es válido, se detiene la función

    for paquete in paquetes_turisticos:
        if paquete["id"] == id_valido:
            paquetes_turisticos.remove(paquete)
            print(f"Paquete con ID {id_valido} eliminado.")
            return

    print(f"Paquete con ID '{id_paquete}' no encontrado.")

# Menú principal
def menu_paquetes():
    while True:
        print("\n--- Menú de Paquetes Turísticos ---")
        print("1. Crear paquete")
        print("2. Mostrar todos los paquetes")
        print("3. Mostrar paquete específico por ID")
        print("4. Actualizar paquete")
        print("5. Eliminar paquete")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Validación del destino del paquete
            while True:
                destino = input("Destino del paquete: ").strip()
                if validar_entrada_no_vacia(destino) and validar_entrada_sin_numeros(destino):
                    break
                print("El destino no puede estar vacío y no debe contener números.")

            # Validación del nombre del paquete
            while True:
                nombre = input("Nombre del paquete: ").strip()
                if validar_entrada_no_vacia(nombre) and validar_entrada_sin_numeros(nombre):
                    break
                print("El nombre no puede estar vacío y no debe contener números.")

            # Validación de la descripción del paquete
            while True:
                descripcion = input("Descripción del paquete: ").strip()
                if validar_entrada_no_vacia(descripcion) and validar_entrada_sin_numeros(descripcion):
                    break
                print("La descripción no puede estar vacía y no debe contener números.")

            # Validación del precio del paquete
            while True:
                precio = input("Precio del paquete: ").strip()
                if validar_precio(precio):
                    precio = float(precio)
                    break

            # Validación de las actividades del paquete
            while True:
                actividades = input("Actividades (separadas por comas): ").split(",")
                actividades = [a.strip() for a in actividades if a.strip()]  # Elimina espacios en blanco
                if all(validar_entrada_sin_numeros(a) for a in actividades):  # Verifica que ninguna actividad contenga números
                    break
                print("Las actividades no deben contener números.")

            # Itinerario
            itinerario = {}
            while True:
                agregar_itinerario = input("¿Deseas agregar itinerario? (s/n): ").lower()
                if agregar_itinerario == "s":
                    dia = int(input("Día del itinerario: "))
                    actividades_dia = input("Actividades para el día (separadas por comas): ").split(",")
                    itinerario[dia] = [a.strip() for a in actividades_dia if a.strip()]
                else:
                    break

            crear_paquete(destino, nombre, descripcion, precio, actividades, itinerario)

        elif opcion == "2":
            mostrar_paquetes()

        elif opcion == "3":
            id_paquete = input("Ingrese el ID del paquete a mostrar: ")
            mostrar_paquete_por_id(id_paquete)

        elif opcion == "4":
            id_paquete = input("Ingrese el ID del paquete a actualizar: ")
            actualizar_paquete(id_paquete)

        elif opcion == "5":
            id_paquete = input("Ingrese el ID del paquete a eliminar: ")
            eliminar_paquete(id_paquete)

        elif opcion == "6":
            print("Saliendo del menú de paquetes turisticos...")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")


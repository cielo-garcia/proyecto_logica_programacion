# Diccionario para almacenar reservas de tiquetes y hoteles
reservas = {
    "tiquetes": [], # Lista para almacenar reservas de tiquetes
    "hoteles": [] # Lista para almacenar reservas de hoteles
}

# Función para crear una reserva de tiquete
def crear_reserva_tiquete(destino, clase, horario):
    reservas["tiquetes"].append({"destino": destino, "clase": clase, "horario": horario})
    print(f"Reserva creada: {destino}, {clase}, {horario}")

# Función para consultar las reservas de tiquetes
def consultar_reservas_tiquetes():
    if reservas["tiquetes"]:
        for idx, reserva in enumerate(reservas["tiquetes"], 1):
            print(f"{idx}. Destino: {reserva['destino']}, Clase: {reserva['clase']}, Horario: {reserva['horario']}")
    else:
        print("No hay reservas de tiquetes.")

# Función para actualizar una reserva de tiquete
def actualizar_reserva_tiquete():
    consultar_reservas_tiquetes()
    if reservas["tiquetes"]:
        idx = int(input("Seleccione el número de la reserva a actualizar: ")) - 1
        if 0 <= idx < len(reservas["tiquetes"]):
            print("¿Qué desea actualizar?")
            print("1. Destino")
            print("2. Clase")
            print("3. Horario")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nuevo_destino, _, _ = seleccionar_tiquete()
                reservas["tiquetes"][idx]["destino"] = nuevo_destino
            elif opcion == "2":
                _, nueva_clase, _ = seleccionar_tiquete()
                reservas["tiquetes"][idx]["clase"] = nueva_clase
            elif opcion == "3":
                _, _, nuevo_horario = seleccionar_tiquete()
                reservas["tiquetes"][idx]["horario"] = nuevo_horario
            else:
                print("Opción no válida")
            
            print("Reserva actualizada.")
        else:
            print("Número inválido.")

# Función para eliminar una reserva de tiquete
def eliminar_reserva_tiquete():
    consultar_reservas_tiquetes()
    if reservas["tiquetes"]:
        idx = int(input("Seleccione el número de la reserva a eliminar: ")) - 1
        if 0 <= idx < len(reservas["tiquetes"]):
            reservas["tiquetes"].pop(idx)
            print("Reserva eliminada.")
        else:
            print("Número inválido.")

# Función para crear una reserva de hotel
def crear_reserva_hotel(estancia, comidas, ubicacion):
    reservas["hoteles"].append({"estancia": estancia, "comidas": comidas, "ubicacion": ubicacion})
    print(f"Reserva de hotel creada: {estancia}, {comidas}, {ubicacion}")

# Función para consultar las reservas de hoteles
def consultar_reservas_hoteles():
    if reservas["hoteles"]:
        for idx, reserva in enumerate(reservas["hoteles"], 1):
            print(f"{idx}. Estancia: {reserva['estancia']}, Comidas: {reserva['comidas']}, Ubicación: {reserva['ubicacion']}")
    else:
        print("No hay reservas de hoteles.")

# Función para actualizar una reserva de hotel
def actualizar_reserva_hotel():
    consultar_reservas_hoteles()
    if reservas["hoteles"]:
        idx = int(input("Seleccione el número de la reserva a actualizar: ")) - 1
        if 0 <= idx < len(reservas["hoteles"]):
            print("¿Qué desea actualizar?")
            print("1. Tipo de estancia")
            print("2. Comidas")
            print("3. Ubicación")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nueva_estancia, _, _ = seleccionar_hotel()
                reservas["hoteles"][idx]["estancia"] = nueva_estancia
            elif opcion == "2":
                _, nuevas_comidas, _ = seleccionar_hotel()
                reservas["hoteles"][idx]["comidas"] = nuevas_comidas
            elif opcion == "3":
                _, _, nueva_ubicacion = seleccionar_hotel()
                reservas["hoteles"][idx]["ubicacion"] = nueva_ubicacion
            else:
                print("Opción no válida")
            
            print("Reserva actualizada.")
        else:
            print("Número inválido.")

# Función para eliminar una reserva de hotel
def eliminar_reserva_hotel():
    consultar_reservas_hoteles()
    if reservas["hoteles"]:
        idx = int(input("Seleccione el número de la reserva a eliminar: ")) - 1
        if 0 <= idx < len(reservas["hoteles"]):
            reservas["hoteles"].pop(idx)
            print("Reserva eliminada.")
        else:
            print("Número inválido.")

# Menú principal para gestionar las reservas
def menu_reservas():
    while True:
        print("\n--- Menú de Reservas ---")
        print("1. Consultar reservas de tiquetes")
        print("2. Crear reserva de tiquete")
        print("3. Actualizar reserva de tiquete")
        print("4. Eliminar reserva de tiquete")
        print("5. Consultar reservas de hotel")
        print("6. Crear reserva de hotel")
        print("7. Actualizar reserva de hotel")
        print("8. Eliminar reserva de hotel")
        print("9. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            consultar_reservas_tiquetes()
        
        elif opcion == "2":
            destino_seleccionado, tiquete_seleccionado, horario_seleccionado = seleccionar_tiquete()
            crear_reserva_tiquete(destino_seleccionado, tiquete_seleccionado, horario_seleccionado)
        
        elif opcion == "3":
            actualizar_reserva_tiquete()

        elif opcion == "4":
            eliminar_reserva_tiquete()

        elif opcion == "5":
            consultar_reservas_hoteles()
        
        elif opcion == "6":
            estancia, comidas, ubicacion = seleccionar_hotel()
            crear_reserva_hotel(estancia, comidas, ubicacion)

        elif opcion == "7":
            actualizar_reserva_hotel()

        elif opcion == "8":
            eliminar_reserva_hotel()

        elif opcion == "9":
            print("Saliendo del menú de reservas...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Funciones auxiliares para seleccionar tiquete 
def seleccionar_tiquete():
    while True:
        print ("\n--- Menú de Destinos ---")
        print("1. Amazonas")
        print("2. Caribe")
        print("3. Pacífico")
        opcion_destino = input("Seleccione el destino: ")

        if opcion_destino == "1":
            destino_seleccionado = "Amazonas"
        elif opcion_destino == "2":
            destino_seleccionado = "Caribe"
        elif opcion_destino == "3":
            destino_seleccionado = "Pacífico"
        else:
            print("Opción no válida")
            continue

        print("\n--- Menú de Tiquetes ---")
        print("1. Tiquete clase económica")
        print("2. Tiquete clase media")
        print("3. Tiquete clase ejecutiva")
        opcion_tiquete = input("Seleccione una opción de tiquete: ")

        if opcion_tiquete == "1":
            tiquete_seleccionado = "clase económica"
        elif opcion_tiquete == "2":
            tiquete_seleccionado = "clase media"
        elif opcion_tiquete == "3":
            tiquete_seleccionado = "clase ejecutiva"
        else:
            print("Opción no válida")
            continue

        print("\n--- Horarios ---")
        print("1. En la mañana")
        print("2. Al medio día")
        print("3. En la noche")
        opcion_horario = input("Seleccione una opción de horario: ")

        if opcion_horario == "1":
            horario_seleccionado = "en la mañana"
        elif opcion_horario == "2":
            horario_seleccionado = "al medio día"
        elif opcion_horario == "3":
            horario_seleccionado = "en la noche"
        else:
            print("Opción no válida")
            continue
        
        return destino_seleccionado, tiquete_seleccionado, horario_seleccionado

# Funciones auxiliares para seleccionar hotel
def seleccionar_hotel():
    while True:
        print("\n--- Menú de Reservas de Hotel ---")
        print("1. Para una persona")
        print("2. Para una pareja")
        print("3. Para una familia (3-6 personas)")
        print("4. Para quedarse con amigos")
        opcion_hotel = input("Seleccione el tipo de estancia: ")

        if opcion_hotel == "1":
            tipo_estancia = "una persona"
        elif opcion_hotel == "2":
            tipo_estancia = "una pareja"
        elif opcion_hotel == "3":
            tipo_estancia = "una familia (3-6 personas)"
        elif opcion_hotel == "4":
            tipo_estancia = "para quedarse con amigos"
        else:
            print("Opción no válida")
            continue

        print("\n--- Opciones de Comidas ---")
        print("1. Desayuno")
        print("2. Almuerzo")
        print("3. Cena")
        opcion_comida = input("Seleccione las comidas deseadas (ej. 1 y 2): ")

        comidas_seleccionadas = []
        if "1" in opcion_comida:
            comidas_seleccionadas.append("Desayuno")
        if "2" in opcion_comida:
            comidas_seleccionadas.append("Almuerzo")
        if "3" in opcion_comida:
            comidas_seleccionadas.append("Cena")

        if not comidas_seleccionadas:
            print("Opción no válida")
            continue

        comidas_incluidas = " y ".join(comidas_seleccionadas)

        print("\n--- Ubicación del Hotel ---")
        print("1. En la ciudad")
        print("2. A las afueras")
        opcion_ubicacion = input("Seleccione la ubicación del hotel: ")

        if opcion_ubicacion == "1":
            ubicacion_hotel = "En la ciudad"
        elif opcion_ubicacion == "2":
            ubicacion_hotel = "A las afueras"
        else:
            print("Opción no válida")
            continue

        return tipo_estancia, comidas_incluidas, ubicacion_hotel
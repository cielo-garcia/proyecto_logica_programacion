import paquetes_turisticos
import reservas
import gestion_clientes

def menu_principal():
    while True:
        print("\n--- Menú Principal de la Agencia de Viajes ---")
        print("1. Gestión de Paquetes Turísticos")
        print("2. Reservas de Vuelos y Hoteles")
        print("3. Gestión de Clientes")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            paquetes_turisticos.menu_paquetes()
        elif opcion == "2":
            reservas.menu_reservas()
        elif opcion == "3":
            gestion_clientes.menu_clientes()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

menu_principal()
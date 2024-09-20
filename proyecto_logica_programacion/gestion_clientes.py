import re  # Importamos el módulo de expresiones regularez

clientes = [
    {"nombre": "Carlos", "apellido": "López", "email": "carlos.lopez@gmail.com"},
    {"nombre": "María", "apellido": "Pérez", "email": "maria.perez@yahoo.com"},
    {"nombre": "Ana", "apellido": "García", "email": "ana.garcia@hotmail.com"}
]  

# Función que valida que el nombre solo contenga letras, espacios, acentos y la letra "ñ"
def es_valido_nombre(nombre):
    return bool(re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre))  # Usa una expresión regular para validar el nombre

# Función que valida que el email tenga un formato correcto
def es_valido_email(email):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))  # Usa una expresión regular para validar el email

# Función para verificar si el email ya existe en la lista de clientes
def es_email_duplicado(email, email_actual=None):
    for cliente in clientes:
        if cliente["email"] == email and cliente["email"] != email_actual:
            return True
    return False

# Función para registrar un nuevo cliente en la lista
def registrar_cliente(nombre, apellido, email):
    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }
    clientes.append(cliente)  # Añadimos el cliente a la lista de clientes
    print(f"Cliente '{nombre} {apellido}' registrado exitosamente.")

# Función para actualizar los datos de un cliente existente
def actualizar_cliente(email):
    for cliente in clientes:
        if cliente["email"] == email:
            nuevos_datos = {}

            # Validación y actualización del nombre
            while True:
                nuevo_nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
                if not nuevo_nombre or es_valido_nombre(nuevo_nombre):
                    if nuevo_nombre:
                        nuevos_datos["nombre"] = nuevo_nombre
                    break
                else:
                    print("Error: El nombre solo debe contener letras. Inténtalo de nuevo.")

            # Validación y actualización del apellido
            while True:
                nuevo_apellido = input("Nuevo apellido (deja en blanco para no cambiar): ")
                if not nuevo_apellido or es_valido_nombre(nuevo_apellido):
                    if nuevo_apellido:
                        nuevos_datos["apellido"] = nuevo_apellido
                    break
                else:
                    print("Error: El apellido solo debe contener letras. Inténtalo de nuevo.")

            # Validación y actualización del email
            while True:
                nuevo_email = input("Nuevo email (deja en blanco para no cambiar): ")
                if not nuevo_email or (es_valido_email(nuevo_email) and not es_email_duplicado(nuevo_email, email)):
                    if nuevo_email:
                        nuevos_datos["email"] = nuevo_email
                    break
                elif es_email_duplicado(nuevo_email, email):
                    print(f"Error: El email '{nuevo_email}' ya está registrado. Introduce un email diferente.")
                else:
                    print("Error: El formato del email es inválido. Inténtalo de nuevo.")

            cliente.update(nuevos_datos)
            print(f"Cliente '{email}' actualizado exitosamente.")
            return

    print(f"Error: Cliente con email '{email}' no encontrado.")  # Si no encuentra el cliente, muestra este mensaje

# Función para eliminar un cliente de la lista
def eliminar_cliente(email):
    for cliente in clientes:
        if cliente["email"] == email:
            clientes.remove(cliente)
            print(f"Cliente con email '{email}' eliminado exitosamente.")
            return
    print(f"Error: Cliente con email '{email}' no encontrado.")  # Si no encuentra el cliente, muestra este mensaje

# Función para mostrar todos los clientes registrados
def mostrar_clientes():
    if not clientes:  # Si la lista de clientes está vacía, muestra este mensaje
        print("No hay clientes registrados.")
    else:
        print("\n--- Lista de clientes registrados ---")
        for cliente in clientes:  # Si hay clientes, los muestra uno por uno
            print(f"Nombre: {cliente['nombre']} {cliente['apellido']}, Email: {cliente['email']}")

# Función que gestiona el menú principal
def menu_clientes():
    while True:
        # Mostramos las opciones del menú
        print("\n--- Menú de Gestión de Clientes ---")
        print("1. Registrar cliente")
        print("2. Actualizar cliente")
        print("3. Eliminar cliente")
        print("4. Mostrar clientes")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":  # Registrar cliente
            # Solicitamos y validamos el nombre
            while True:
                nombre = input("Nombre: ")
                if es_valido_nombre(nombre):
                    break
                else:
                    print("Error: El nombre solo debe contener letras. Inténtalo de nuevo.")

            # Solicitamos y validamos el apellido
            while True:
                apellido = input("Apellido: ")
                if es_valido_nombre(apellido):
                    break
                else:
                    print("Error: El apellido solo debe contener letras. Inténtalo de nuevo.")

            # Solicitamos, validamos el email, y verificamos si está duplicado
            while True:
                email = input("Email: ")
                if not es_valido_email(email):
                    print("Error: El formato del email es inválido. Inténtalo de nuevo.")
                elif es_email_duplicado(email):
                    print(f"Error: El email '{email}' ya está registrado. Introduce un email diferente.")
                else:
                    break  # Si el email es válido y no está duplicado, salimos del bucle

            registrar_cliente(nombre, apellido, email)  # Registramos el cliente

        elif opcion == "2":  # Actualizar cliente
            email = input("Email del cliente a actualizar: ")  # Solicitamos el email del cliente a actualizar
            actualizar_cliente(email)  # Actualizamos los datos del cliente

        elif opcion == "3":  # Eliminar cliente
            email = input("Email del cliente a eliminar: ")  # Solicitamos el email del cliente a eliminar
            eliminar_cliente(email)  # Eliminamos el cliente

        elif opcion == "4":  # Mostrar clientes
            mostrar_clientes()  # Mostramos todos los clientes registrados

        elif opcion == "5":  # Salir del menú
            print("Saliendo del menú de gestión de clientes...")
            break  # Terminamos el ciclo del menú

        else:
            print("Error: Opción no válida.")  # Si el usuario elige una opción incorrecta, muestra este mensaje

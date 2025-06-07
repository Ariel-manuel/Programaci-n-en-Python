# Creamos un diccionario para almacenar la información de un contacto
contacto = {
    "nombre": "Ana",
    "telefono": "310-1234567",
    "email": "ana.perez@ejemplo.com",
    "ciudad": "Bogotá" # ¡Hola desde Bogotá!
}

print("¡Bienvenido a tu Mini Base de Datos de Contactos!")
print("Aquí está la información de un contacto de ejemplo:")

# Accedemos y mostramos la información usando las "claves"
print(f"Nombre: {contacto['nombre']}")
print(f"Teléfono: {contacto['telefono']}")
print(f"Email: {contacto['email']}")
print(f"Ciudad: {contacto['ciudad']}")

print("\n--- ¡Puedes buscar información específica! ---")

# Pedimos al usuario qué información quiere ver
clave_buscada = input("¿Qué información quieres saber del contacto (nombre, telefono, email, ciudad)? ").lower()

# Verificamos si la clave existe en el diccionario antes de mostrarla
if clave_buscada in contacto:
    print(f"La {clave_buscada} de Ana es: {contacto[clave_buscada]}")
else:
    print("Lo siento, esa información no está disponible o la escribiste mal.")

print("\n¡Los diccionarios son geniales para organizar datos!")
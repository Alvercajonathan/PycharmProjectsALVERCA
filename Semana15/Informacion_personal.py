# Crear un diccionario llamado 'informacion_personal' con claves y valores ficticios
informacion_personal = {
    "nombre": "Jonathan Alverca",
    "edad": 30,
    "ciudad": "Puyo",
    "profesion": "Ingeniero Informatico"
}

# Acceder al valor de la clave 'ciudad' y modificarlo
informacion_personal["ciudad"] = "Zamora"  # Cambio de ciudad

# Verificar si la clave 'telefono' existe en el diccionario, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"  # Agregar número de teléfono

# Eliminar la clave 'edad' del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
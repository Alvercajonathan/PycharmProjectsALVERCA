# Escritura en archivo de texto

# Abrimos el archivo 'my_notes.txt' en modo escritura ('w').
# Si el archivo no existe, se crea. Si ya existe, su contenido se sobrescribe.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales.
    file.write("Mis apuntes de la semana 16.\n")
    file.write("Yo utilizo python como leguaje de programacion.\n")
    file.write("Programacion es mi materia favorita.\n")

# Lectura del archivo de texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos cada línea del archivo.
    line = file.readline()
    while line:
        print(line.strip())  # strip() elimina los saltos de línea adicionales al imprimir.
        line = file.readline()

# No es necesario cerrar manualmente el archivo debido al uso de 'with', que gestiona el cierre automáticamente.

#creación de la función que calculará el descuento utilizando el valor de la compra y el valor del descuento
def calcular_descuento(valor_compra , descuento=12):
    #operación que realiza el descuento
    valor_de_descuento= valor_compra*descuento/100
    #devuelve el valor del descuento
    return valor_de_descuento

#bucle que mantiene funcionando el programa
while True:
    #se le pide al usuario que ingrese el monto de su compra
    valor_comprado = int(input('Ingrese el monto de su compra'))
    #se llama la función y se aplica el descuento utilizando el parámetro predeterminado
    valor_descontado = calcular_descuento(valor_comprado)
    #se imprime el valor del descuento
    print(f'tiene un descuento de: {valor_descontado}$')

    #se le pregunta al usuario si desea aplicar su propio descuento
    descontar=int(input('1:escriba 1 si desea ingresar su propio descuento, 2:escriba 2 para continuar'))

    #si el usuario responde 1, se le pide el valor del descuento.
    if descontar == 1:
        valor_descuento = int(input('Ingrese el valor de descuento'))
        #se llama a la función y se calcula el descuento con el valor de la compra y el valor de descuento ingresado por el usuario
        valor_descontado2 = calcular_descuento(valor_comprado, valor_descuento)
        #se imprime el valor del descuento
        print(f'tiene un descuento de {valor_descontado2}$')

    #se le pregunta al usuario si desea volver a utilizar el programa
    volver = int(input('1:escriba 1 si desea volver a utilizar el programa, 2: escriba 2 si desea cerrar'))
    #si responde 1. se vuelve a ejecutar el bucle, si responde 2 se cierra.
    if volver == 2:
        print('gracias por utilizar nuestro servicio')
        break


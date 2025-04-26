# 5_ Imprimir un mensaje de error si no se pasan suficientes argumentos.
def validarCantidadArgumentos(*argumentos):
    # print(argumentos)
    respuesta = True if len(argumentos) >= 1 else False
    return respuesta


try:
    lista_argumentos = input(
        "Ingresar una lista de palabras separada por espacios que serán usados como argumentos.  Enter para continuar: \n"
    ).split()

    # print(lista_argumentos)
    # print(len(lista_argumentos))

    validez = validarCantidadArgumentos(*lista_argumentos)

    print("Procesando argumentos ingresados.")
except TypeError:
    print(f"Ha ocurrido un error con los tipos de datos")
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    if validez == False:
        print(f"Numero de argumentos insuficientes. ")
    else:
        print(f"Numero de argumentos valido. ")
finally:
    print("Fin del programa.")

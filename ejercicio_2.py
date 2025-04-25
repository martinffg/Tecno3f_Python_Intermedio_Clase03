# 2_ Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario.


def buscarPalabra(palabra, *args):
    i = 0
    respuesta = False

    print(args)
    for arg in args:
        if palabra == args[i]:
            respuesta = True
    return respuesta


try:
    lista_palabras = input(
        "Ingresar una lista de palabras separada por espacios.  Enter para continuar: \n"
    ).split()

    palabra = input(
        "Ingresar una palabra a buscar en la lista. Enter para continuar: \n"
    )

    print(lista_palabras)
    print(palabra)

    # lista_tupla = tuple(lista_palabras)

    cadena_con_comas = "'" + "','".join(lista_palabras) + "'"

    print(cadena_con_comas)

    respuesta = True if buscarPalabra(palabra, cadena_con_comas) else False
    print("Procesando números ingresados.")
except TypeError:
    print(f"Ha ocurrido un error con los tipos de datos")
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    print(f"La palabra {palabra} está en la lista? {respuesta}")
finally:
    print("Fin del programa.")

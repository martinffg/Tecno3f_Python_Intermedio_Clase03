# 2_ Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario.


def buscarPalabra(palabra, *args):
    try:
        respuesta = False

        posicion = args.index(palabra)
    except ValueError:
        respuesta = False
    else:
        if posicion >= 0:
            respuesta = True
    finally:
        return respuesta


try:
    lista_palabras = input(
        "Ingresar una lista de palabras separada por espacios.  Enter para continuar: \n"
    ).split()

    palabra = input(
        "Ingresar una palabra a buscar en la lista. Enter para continuar: \n"
    )

    # print(lista_palabras)
    # print(palabra)

    encontrado = True if buscarPalabra(palabra, *lista_palabras) else False
    print("Procesando números ingresados.")
except TypeError:
    print(f"Ha ocurrido un error con los tipos de datos")
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    if encontrado:
        print(f"EXITO!! La palabra SI está en la lista cargada. ")
    else:
        print(f"ERROR!! La palabra NO está en la lista cargada. ")
finally:
    print("Fin del programa.")

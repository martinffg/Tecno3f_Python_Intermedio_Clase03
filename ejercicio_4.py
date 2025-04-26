# 4_ Calcular el promedio de una lista de números usando args y un operador ternario.


def validarPromedio(*args):
    i = 0
    respuesta = False
    if args[1] > 0:
        respuesta = True
    return respuesta


try:
    lista_numeros = input(
        "Ingresar una lista de numeros separada por espacios.  Enter para continuar: \n"
    ).split()

    cantidad_numeros = len(lista_numeros)

    total = 0

    for numero in lista_numeros:
        total += int(numero)

    promedio = total / cantidad_numeros

    respuesta = True if validarPromedio(total, cantidad_numeros, promedio) else False
    print("Procesando números ingresados.")
except TypeError:
    print(f"Ha ocurrido un error con los tipos de datos")
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    print(
        f"El promedio de la lista ingresada es: {promedio} y la validez de su calculo es {respuesta}"
    )
finally:
    print("Fin del programa.")

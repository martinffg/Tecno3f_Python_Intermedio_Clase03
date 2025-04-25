# 1_ Calcular el mayor de dos números ingresados por teclado usando un operador ternario.

try:
    print("Ingresar dos números por teclado.\n")
    numero_mayor = -999999999
    numero1 = int(input("Ingresar 1er número: "))
    numero2 = int(input("Ingresar 2do número: "))
    numero_mayor = numero1 if numero1 >= numero2 else numero2
    print("Procesando números ingresados.")
except TypeError:
    print(f"Ha ocurrido un error con los tipos de datos")
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    print(f"El número mayor es: {numero_mayor}")
finally:
    print("Fin del programa.")

# 3_ Determinar si un número es par o impar.


try:
    numero1 = int(input("Ingresar un número para saber si es par o impar: "))
    resultado = numero1 % 2
    mensaje = "PAR" if resultado == 0 else "IMPAR"
    print("Procesando números ingresados.")
except TypeError:
    print(f"Ha ocurrido un error con los tipos de datos")
except Exception as e:
    print(f"Ha ocurrido un error. {e}")
else:
    print(f"El número es: {mensaje}")
finally:
    print("Fin del programa.")

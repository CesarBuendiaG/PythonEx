
# ----------------------- mi solucion -----------------------------------

# n1 = ""
# n2 = ""
# op = ""

# if n1 == "":
#         n1 = int(input("Introduce el primer numero: "))
#         print(n1)

# while op.lower() != "salir":
    
#     op = input("Que operacion: ")
#     if op.lower() == "salir":
#          break
    
#     n2 = int(input("Numero 2: "))
    
#     if op == "suma":
#         resultado = n1 + n2
#         print(resultado)
#         n1 = resultado
#     elif op == "resta":
#         resultado = n1 - n2
#         print(resultado)
#         n1 = resultado
#     elif op == "mult":
#         resultado = n1 * n2
#         print(resultado)
#         n1 = resultado
#     elif op == "div":
#         resultado = n1 / n2
#         print(resultado)
#         n1 = resultado


# ------------------------------- Respuesta ideal --------------------------------

print("Bienvenidos a la calculadora")
print("Para salir escribe 'salir'")
print("Las operaciones son suma, resta, multi y div")

resultado = "" # Primero definimos la variable de resultado, ya que la vamos a preguntar al inicio

while True:  # While True para hacer el ciclo infinito (Dentro vamos a poner breaks para "Salir")

    if not resultado: # "Sí 'Resultado' es False" (no tiene info) pidelo por input ((Siempre va a pasar en la primera ejecucion))
        resultado = input("Ingrese número 1: ")
        if resultado.lower() == "salir":  # *Revisa sí el usuario quiere salir desde el numero 1
            break
        resultado = int(resultado)

    op = input("Ingresa que operacion: ") # Pides la operacion
    if op.lower() == "salir":  # *Revisa sí el usuario quiere salir desde la seleccion de operacion
        break

    n2 = input("Ingresa siguiente numero: ") # Pides el segundo numero (Recuerda que siempre  recibes Input en String)
    if n2.lower() == "salir": # *Revisa sí el usuario quiere salir desde el numero 2 en forma de String
        break
    n2 = int(n2) # Convertimos el numero dos de String a numero (Despues de evaluar la condicion de salida)

    if op.lower() == "suma": # Tus operaciones que asignan directamente el resultado a la variable
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida") # Tu excepcion, por si no introduce una operacion correctamente
        break

    print(f"El resultado es {resultado}") # Print del resultado





# Ingresar un numero y regresar una cadena de 0 al numero de uno en uno, y al reves


numero = input("Ingresa un numero positivo")
numero = int(numero)

listaNormal = []
listaReversa = []

for n in range(0,numero + 1,1):
    listaNormal.append(n)

for n in range(numero , - 1,-1):
    listaReversa.append(n)

# Suponiendo ingreso el numero 10
print(listaNormal) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listaReversa) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


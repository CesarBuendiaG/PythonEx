
# Recibir una palabra o frase (¿Que hacemos con los espacios?)
# Retorna sí es true o false de palindromo 


print("Bienvenido al verificador de palindormos")
print("Para salir en cualquier momento solo ingrese 'salir'")

palabra = ""
cruda = ""
reversa = ""



while True:
    palabra = input("Ingrese palabra ")
    cruda = palabra.lower().replace(" ","") # Pasamos todo a minusculas y quitamos todos los espacios
    reversa = cruda[::-1]

    if cruda == "salir":
        print("Ha salido")
        break

    if cruda == reversa:
        print(f"El dato '{palabra.strip()}' es un palindromo = {cruda == reversa}")
        
    else:
        print(f"El dato '{palabra.strip()}' NO es un palindromo = {cruda == reversa}")



# --------- Para transformar una palabra a minusculas y sin espacion con ciclo for ----

# Alternativa con "for" de:  || cruda = palabra.lower().replace(" ","") ||

# palabra2 = "amo la paloma"
# acumulado = ""
# char2 = ""

# for char in palabra2:
#     char2 = char.strip().lower()
#     acumulado += char2

# print(acumulado)




# Alternativa 2 (Solo espacio, sin metodos de strings)

# def sin_espacio(texto):
#     nuevo_texto = "" # Creas tu variable de almacenamiento de la nueva cadena
#     for char in texto: # Iteras cada char
#         if char != "": # Sí char es diferente de " " (espacio), acumulalo en la variable
#             nuevo_texto += char
#     return nuevo_texto # Regresas todos los char sin espacio



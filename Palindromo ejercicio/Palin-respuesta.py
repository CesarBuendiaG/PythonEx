

def reverse_string(str):  
    str1 = ""   # Declaras una variable vacia para ir acumulando los resultados
    for i in str:  # Ciclo que recorre cada letra
        str1 = i + str1 # Toma la palabra actual y sumala para la derecha
    return str1    # It will return the reverse string to the caller function  
     
    # Given String       
str = "JavaTpoint"
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  


# Cada nueva letra la sumas a la derecha (De esta manera la ponemos al reves)
# J -> a+J -> v+aJ -> a+vaJ
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.




def calc(parcial, iva = 21):
    c_iva = iva * 0.01
    complete = parcial + (parcial * c_iva)
    print(complete)


calc(100)
calc(100, 10)
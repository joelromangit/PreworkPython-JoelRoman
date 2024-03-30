'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''
#Hacemos la función teniendo en cuenta que conocemos el total a pagar en el restaurante sin tener en cuenta la propina
def calculadoraPropina(cuenta):
    propina = cuenta*0.15
    totalPagar = cuenta + propina
    print(f'La cuenta de {cuenta}€ con propina es de {totalPagar}€')
    return(totalPagar)

#Ejemplo con 50€
calculadoraPropina(50)
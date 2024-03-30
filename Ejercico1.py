'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''
def CelsiusToFahrenheit(Celsius):
    Fahrenheit = (Celsius*9/5)+32
    print(f'{Celsius}ºC son {Fahrenheit}ºF')
    return(Fahrenheit)

#Ejemplo con 20ºC
CelsiusToFahrenheit(20)
'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''
#Sabemos que un año es bisiesto si el número de año es divisible entre 4 pero no entre 100 o el año es divisible entre 400.
def bisiesto(año):
  if (año%4 == 0 and año%100 != 0) or año%400 == 0:
        print(f'El año {año} es bisiesto')
  else:
    print(f'El año {año} no es bisiesto')


#Ejemplo con año bisiesto 2024
bisiesto(2024)
#Ejemplo con año no bisiesto 2025
bisiesto(2025)

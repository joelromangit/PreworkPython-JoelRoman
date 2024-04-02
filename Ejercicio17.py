'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''
def millasToKm(millas):
  print(f'{millas} millas son {millas*1.60934:.2f} km')

#Ejemplo 100 millas
millasToKm(100)
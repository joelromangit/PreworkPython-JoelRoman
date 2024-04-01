'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''
def dolarToEuro(dolar):
  print(f'{dolar}$ son {dolar*0.85:.2f}€')

#Prueba con 50 dólares
dolarToEuro(50)
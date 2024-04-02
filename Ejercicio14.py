'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''
def descuento(precio):
  print(f'El precio rebajado de {precio}€ con 20% de descuento es de {precio*0.8:.2f}€, ahorrando {precio*0.2:.2f}€')

#Ejemplo con 100€
descuento(100)
#Ejemplo con 129,99€
descuento(129.99)
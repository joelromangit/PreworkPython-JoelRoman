'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario
'''
#Vamos a hacerlo de la manera más simple posible, solo imprimiremos el resultado de las opciones

#Definimos la opción suma
def suma(x,y):
  if int(x) and int(y):
    print(x+y)
  else:
    print("Los elementos de entrada han de ser números")

#Definimos la opción resta
def resta(x,y):
  print(x-y)

#Definimos la opción multiplicación
def mult(x,y):
  print(x*y)

#Definimos la opción divisón
def div(x,y):
  if y != 0:
    print(x/y)
  else:
    print("No se puede dividir entre 0")
opcion = 0
while opcion != 5:
  print('Calculadora básica\n'
  '----------------------------\n'
  '   1. Suma\n'
  '   2. Resta\n'
  '   3. Multiplicación\n'
  '   4. División\n'
  '   5. Salir\n'
  '----------------------------\n'
  )
  opcion = input('   Seleccione opción: ')
  if opcion == 1:
    x = input('Primer número suma: ')
    y = input('Segundo número suma')
    suma(x,y)
  if opcion == 5:
    break

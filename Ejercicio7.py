'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario
'''
#Vamos a hacerlo de la manera más simple posible, solo imprimiremos el resultado de las opciones
#También vamos a dar por hecho que el usuario introducirá int como entrada

#Definimos la opción suma
def suma(x,y):
  print(f'      {x} + {y} = {x+y}')

#Definimos la opción resta
def resta(x,y):
  print(f'      {x} - {y} = {x-y}')

#Definimos la opción multiplicación
def mult(x,y):
  print(f'      {x} x {y} = {x*y}')

#Definimos la opción divisón
def div(x,y):
  if y != 0:
    print(f'      {x} / {y} = {(x/y):.2f}') #Limitamos a 2 decimales la división
  else:
    print("  No se puede dividir entre 0")

while True:
  print('Calculadora básica\n'
  '----------------------------\n'
  '   1. Suma\n'
  '   2. Resta\n'
  '   3. Multiplicación\n'
  '   4. División\n'
  '   5. Salir\n'
  '----------------------------\n'
  )
  opcion = int(input('   Seleccione opción: '))
  if opcion == 1:
    x = int(input('Primer número suma: '))
    y = int(input('Segundo número suma: '))
    print('\n----------------------------\n')
    suma(x,y)
    print('\n----------------------------')
  if opcion == 2:
    x = int(input('Primer número resta: '))
    y = int(input('Segundo número resta: '))
    print('\n----------------------------\n')
    resta(x,y)
    print('\n----------------------------')
  if opcion == 3:
    x = int(input('Primer número multiplicación: '))
    y = int(input('Segundo número multiplicación: '))
    print('\n----------------------------\n')
    mult(x,y)
    print('\n----------------------------')
  if opcion == 4:
    x = int(input('Primer número división: '))
    y = int(input('Segundo número división: '))
    print('\n----------------------------\n')
    div(x,y)
    print('\n----------------------------')
  if opcion == 5:
    break

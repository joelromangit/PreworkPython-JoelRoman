'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''
def contador(lista):
  pares = 0
  impares = 0
  for num in lista:
    if num%2 == 0:
      pares += 1
    else:
      impares += 1
  print(f'En tu lista hay {pares} par/es y {impares} impar/es')

#Ejemplo 1
lista = [1,2,3,4,5,6,7,8,9,10]
contador(lista)
#Ejemplo 2
lista1 = [3,4,7,13,164,975]
contador(lista1)
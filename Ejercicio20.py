'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''
def sumaLista(lista):
  suma = 0
  for num in lista:
    suma += num
  print(f'La suma de los números de tu lista es {suma}')

#Ejemplo
lista = [1,2,3,4,6,10,2,-4,-120,405]
sumaLista(lista)
'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''
num = 1 #contador del bucle
suma = 0  #Inicializamos suma de pares
pares = []  #Hacemos lista de pares para mostrar como el programa coge estos números
while num <= 100:
  if num%2 == 0:  #Por definición sabemos que un númnero es par si su residuo es 0
    suma += num
    pares.append(num)
  num += 1
print(suma)
print(pares)
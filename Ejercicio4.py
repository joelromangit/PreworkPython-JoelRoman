'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''
vocales = ["a","e","i","o","u"]
def contadorVocales(palabra):
  contador = 0
  palabraMinus = palabra.lower() #Para evitar que las mayúsculas no cuenten como vocal, hacemos todas las letras de palabra minúsculas
  for letra in palabraMinus:
    for vocal in vocales:
      if letra == vocal:
        contador += 1
  print(f'La palabra {palabra} tiene {contador} vocales')
  return(contador)

#Ejemplo con "Abecedario" que tiene 6 vocales
contadorVocales("Abecedario")
'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def palindromo(palabra):
  palabra = palabra.lower()
  largo = len(palabra)
  if largo%2 != 0:  #Para que una palabra sea palíndroma, el número de letras ha de ser impar
    principio = 0 #Contador con el que recorreremos la palabra del principio a la mitad
    final = largo - 1 #Contador con el que recorreremos la palabra del final a la mitad
    while principio < final:
      if palabra[principio] != palabra[final]:
        print(f'La palara {palabra} no es políndroma')  #No entiendo porque no printea, ¿será por el break?
        break
      principio += 1
      final -= 1
    print(f"La palabra {palabra} es políndroma")

#Ejemplo con palabra palíndroma
palindromo("Malayalam")

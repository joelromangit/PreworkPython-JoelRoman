'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''
#Entendemos que la frase estará bien escrita, respetando los espacios y los signos
def contarPalabras(frase):
  contador = 1  #Empezamos en 1 ya que en una frase hay tantas palabras como espacios entre palabras + 1
  for letra in frase:
    if letra == " ":  #Contamos espacios entre palabras
      contador += 1
  print(f'En tu frase hay {contador} palabras')

#Ejemplo con frase
frase = "Hola buenas tardes aventurero, veamos como cuenta palabras este programa."
contarPalabras(frase)
'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''
def primo(num):
  if num <= 3:
    print(f'El número {num} es primo')
  div = 2
  while div<=(num//2):
    if num%div == 0:
      print(f'El número {num} no es primo')
      break
    elif div == num//2:
      print(f'El número {num} es primo')
      break
    else:
      div += 1

while True:
  num = int(input('¿Qué número quieres comprobar que sea primo? '))
  primo(num)
  repetir = input('¿Quieres probar otro número? (Y/N): ') #Entendemos que se pone de forma 100% correcta
  if repetir == "N":
    break

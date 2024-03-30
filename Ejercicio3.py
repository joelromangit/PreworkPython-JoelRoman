'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''
def mayorEdad(edad):
  if edad>=18:
    print(f'Con {edad} años es mayor de edad')
  else: 
    print(f'Con {edad} años no es mayor de edad')

#Ejemplo siendo mayor de edad (20 años)
mayorEdad(20)
#Ejemplo siendo menor de edad (17 años)
mayorEdad(17)
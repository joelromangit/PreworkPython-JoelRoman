'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''
def conocerDiaSemana(dia):
  semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
  if dia <= 7:
    print(f'El día {dia} es {semana[dia-1]}')
  elif dia <= 14:
    print(f'El día {dia} es {semana[dia-7-1]}')
  elif dia <= 21:
    print(f'El día {dia} es {semana[dia-14-1]}')
  elif dia <= 28:
    print(f'El día {dia} es {semana[dia-21-1]}')
  else:
    print(f'El día {dia} es {semana[dia-28-1]}')

while True:
  dia = int(input('¿De qué día quiere conocer su día de la semana? (1-31): '))
  print('\n')
  if dia <= 0 or dia > 31:
    print('El día tiene que estar entre el 1 y el 31. Prueba de nuevo\n')
    continue  #Vuelve a iniciar el bucle
  conocerDiaSemana(dia)
  repetir = input('\n¿Quiere conocer otro día? (Y/N): ')  #Damos por hecho que se pondrá de forma correcta
  print('\n')
  if repetir == "N":
    break
'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''

while True:
  año = int(input('¿Qué año naciste? '))
  if año < 1907:
    print('¿Sabías que la persona más longeva conocida fue Lucile Randon? Nacida el 11 de febrero del 1907 falleció el 17 de enero de 2023 con casi 119 años\nPrueba de nuevo...\n'
    )
    continue
  elif año == 2024:
    print('No me creo que acabes de nacer y me estés haciendo esta pregunta...\nPrueba de nuevo...\n')
    continue
  elif año > 2024:
    print('¿Aún no has nacido?\nPrueba de nuevo...\n')
    continue
  print(f'Si naciste el año {año}, tienes {2024-año-1} o {2024-año} dependiendo del mes que nacieras')
  break
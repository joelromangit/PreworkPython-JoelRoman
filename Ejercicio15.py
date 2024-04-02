'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

def conversorTiempo(minutos):
  if minutos < 60:
    print(f'No hace falta convertir en horas y minutos {minutos} minutos por no pasar de las hora')
  elif minutos == 60:
    print(f'{minutos} minutos es 1 hora')
  elif minutos < 120:
    hora = minutos//60
    mints = int((minutos/60 - hora)*60)
    print(f'{minutos} minutos es {hora} hora y {mints} minutos')
  elif minutos%60 == 0:
    print(f'{minutos} minutos son {minutos//60} horas')
  else:
    hora = minutos//60
    mints = int((minutos/60 - hora)*60)
    print(f'{minutos} minutos es {hora} horas y {mints} minutos')

while True:
  minutos = int(input('Escribe los minutos que quieren convertir en horas: '))
  conversorTiempo(minutos)
  repetir = input('¿Quieres convertir otros minutos? (Y/N): ')
  if repetir == "N":
    break
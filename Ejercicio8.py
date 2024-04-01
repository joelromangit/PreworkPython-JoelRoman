'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
def calculoIMC(peso,altura):
  imc = peso/altura**2
  print(f"Su IMC con peso {peso}kg y altura {altura}m es de {imc:.2f}")

#Ejemplo con peso 83kg y altura 1.83m
calculoIMC(83,1.83)
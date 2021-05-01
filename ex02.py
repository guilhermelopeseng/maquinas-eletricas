# Programa para mostrar o esquema de ligação de um motor de indução trifásico de quatro tensões
import math

line_voltage = int(input('Informe a tensão de linha da rede: '))
fase_voltage = line_voltage/math.sqrt(3)
v1 = int(input('\nInforme a primeira tensão de operação do motor: '))
v2 = int(input('\nInforme a segunda tensão de operação do motor: '))
v3 = int(input('\nInforme a terceira tensão de operação do motor: '))
v4 = int(input('\nInforme a quarta tensão de operação do motor: '))

if v1 == line_voltage:
  print('Fechamento em duplo triangulo, ligação 1-7-6-12, 2-8-4-10, 3-9-5-11')
elif v2 == line_voltage:
  print('Fechamento em Duplo Estrela, ligar 4-10-5-11-6-12, alimentar as fases nos terminais 1-7, 2-8, 3-9')
elif v3 == line_voltage:
  print('Fechamento em Triangulo, liga 9-6, 5-8, 4-7, alimentar as fases nos terminais 1-12, 2-10, 3-11 ')
elif v4 == line_voltage:
  print('Fechamento em Estrela, ligar 4-7, 10-11-12, 5-8, 6-9, alimentar as fases nos terminais 1, 2, 3')
else:
  print('Verifique as informações cedidas')
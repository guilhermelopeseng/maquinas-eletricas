# Programa para mostrar o esquema de ligação de um motor de indução trifásico de duas tensões
import math

line_voltage = int(input('Informe a tensão de linha da rede: '))
v1 = int(input('\nInforme a primeira tensão de operação do motor: '))
v2 = int(input('\nInforme a segunda tensão de operação do motor: '))

if v1 == line_voltage:
  print('Fechamento em Triangulo, ligação 1-6, 2-4, 3-5 ')
elif v2 == line_voltage:
  print('Fechamento em Estrela, ligar 4-5-6, alimentar as fases nos terminais 1-2-3')
else:
  print('Verifique as informações cedidas')
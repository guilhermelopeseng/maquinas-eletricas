# Programa para o calculo das correntes no estator, de magnetização e no rotor
import numpy as np

voltage = float(input('Informe a tensão de fase em volts: '))
print('\nInformações necessários do circuito equivalente por fase de um motor de indução.')
r1 = float(input('Informe a resistência do estator R1 em ohms: '))
x1 = float(input('Informe a reatância do estator jX1 em ohms: '))
rcxm = float(input('Informe o paralelo  da resistência com a reatância de magnetização em ohms: '))
x2 = float(input('Informe a reatância refletida para o primário do rotor jX2 em ohms: '))
r2 = float(input('Informe a resistência refletida para o primpario do rotor R2 em ohms: '))
s = float(input('Informe o escorregamento: '))

matrix = np.array([[r1+x1*1j, rcxm*1j, 0],
                   [0, -rcxm*1j, r2/s + x2*1j],
                   [-1, 1, 1]])
matrix1 = np.array([[voltage],
                    [0],
                    [0]])
inv = np.linalg.inv(matrix)
result = inv.dot(matrix1)
print(f'\nI1 = {result[0][0]:.3f}\nIm = {result[1][0]:.3f}\nI2 = {result[2][0]:.3f}')
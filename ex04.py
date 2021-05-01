#Para executar o codigo é necessario ter a biblioteca opencv instalada.
import numpy as np
import math

voltage = float(input('Informe a tensão de fase em volts: '))
print('\nInformações necessários do circuito equivalente por fase de um motor de indução.')
r1 = float(input('Informe a resistência do estator R1 em ohms: '))
x1 = float(input('Informe a reatância do estator jX1 em ohms: '))
xm = float(input('Informe o paralelo  da resistência com a reatância de magnetização em ohms: '))
rc = float(input('Informe a resistência Rc em ohms do núcleo: '))
x2 = float(input('Informe a reatância refletida para o primário do rotor jX2 em ohms: '))
r2 = float(input('Informe a resistência refletida para o primpario do rotor R2 em ohms: '))
s = float(input('Informe o escorregamento: '))

matrix = np.array([[r1+x1*1j, xm*1j, 0],
                   [0, -xm*1j, r2/s + x2*1j],
                   [-1, 1, 1]])
matrix1 = np.array([[voltage],
                    [0],
                    [0]])
inv = np.linalg.inv(matrix)
result = inv.dot(matrix1)
print(f'\nI1 = {result[0][0]:.3f}\nIm = {result[1][0]:.3f}\nI2 = {result[2][0]:.3f}')
I1 = np.absolute(result[0][0])
Im = np.absolute(result[1][0])
I2 = np.absolute(result[2][0])

#Calculos das perdas
Pce = 3*(I1**2)*r1 #Perdas no cobre do estator do motor.
Pef = 3*(I2**2)*r2/s #Potencia no entreferro.
Pconv = (1 - s)*Pef #Potencia convertida.
Pcr = Pef - Pconv #Perdas no cobre do rotor.
Pnuc = 3*((I1*rc)**2)*(1/rc)

print(f'\nPerdas no cobre estator: {Pce:.3f}W\nPerdas no cobre do rotor: {Pcr:.3f}W\nPotencia convertida: {Pconv:.2f}W\nPerdas no núcleo: {Pnuc:.2f}W')
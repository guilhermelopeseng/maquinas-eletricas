# Programa para o calculo das correntes no estator, de magnetização e no rotor
import numpy as np
import matplotlib.pyplot as plt
import math

Vo = float(input('Informe a tensão de fase em volts: '))
print('\nInformações necessários do circuito equivalente por fase de um motor de indução.')
r1 = float(input('Informe a resistência do estator R1 em ohms: '))
x1 = float(input('Informe a reatância do estator jX1 em ohms: '))
xm = float(input('Informe o paralelo  da resistência com a reatância de magnetização em ohms: '))
x2 = float(input('Informe a reatância refletida para o primário do rotor jX2 em ohms: '))
r2 = float(input('Informe a resistência refletida para o primpario do rotor R2 em ohms: '))

Vth = Vo*(xm/(x1+xm))
Rth = r1*(xm/(x1+xm))**2
Xth = x1

Nmec = np.linspace(0,1800,6000)
s = np.linspace(1,0,6000) 
Tind = ((3*(Vth**2)*r2/s)/((2*math.pi*Nmec/(60*(1-s)))*((Rth + r2/s)**2 + (Xth + x2)**2)))

plt.plot(Nmec, Tind)
plt.show()



# Programa para determinar os parâmetros do motor a partir dos ensaios
import math

print('Insira as informações requeridas para o Ensaio CC:')
vcc = float(input('Tensão Vcc em volts: '))
icc = float(input('Corrente Icc em Amperes: '))

print('Insira as informações requeridas para o Ensaio a vazio: ')
vt = float(input('Módulo da Tensão aplicada Vt nos terminais em volts: '))
ia = float(input('Módulo da Corrente de linha Ia em Ampéres: '))
ib = float(input('Módulo da Corrente de linha Ib em Ampéres: '))
ic = float(input('Módulo da Corrente de linha Ic em Ampéres: '))
fe = float(input('Frequência da rede elétrica em Hz: '))
Pe = float(input('Potência ativa de entrada em Watts: '))

print('Insira as informações requeridas para o Ensaio de rotor bloqueado: ')
vtb = float(input('Módulo da Tensão aplicada Vt nos terminais em volts: '))
iab = float(input('Módulo da Corrente de linha Ia em Ampéres: '))
ibb = float(input('Módulo da Corrente de linha Ib em Ampéres: '))
icb = float(input('Módulo da Corrente de linha Ic em Ampéres: '))
feb = float(input('Frequência do sinal em Hz: '))
Peb = float(input('Potência ativa de entrada em Watts: '))

#Do ensaio CC
R1 = vcc/(2*icc)

# Do ensaio a vazio
IL = (ia + ib + ic)/3
Vo = 208/math.sqrt(3)
Zvz = Vo/IL

# Do ensaio de rotor bloqueado
ILB = (iab + ibb + icb)/3
Zrb = vtb/(math.sqrt(3)*ILB)
teta = math.acos(Peb/(math.sqrt(3)*vtb*ILB))

R2 = math.fabs(Zrb*math.cos(teta) - R1)
Xrb = (fe/feb)*Zrb*math.sin(teta)
X1 = Xrb/2
X2 = Xrb/2
Xm = Zvz-X1

print(f'\nParâmetros encontrados:\nR1 = {R1:.2f}\nX1 = {X1:.2f}\nXm = {Xm:.2f}\nX2 = {X2:.2f}\nR2 = {R2:.2f}')

polos = float(input('\nInsira a quantidade de polos no motor: '))

#Calculo do equivalente de Thevenin
Vth = Vo*(Xm/(X1+Xm))
Rth = R1*(Xm/(X1+Xm))**2
Xth = X1
smax = R2/(math.sqrt((Rth**2) + (Xth+X2)**2))
wsinc = 2*math.pi*120*fe/(polos*60)
Tmax = (3*Vth**2)/(2*wsinc*(Rth + math.sqrt(Rth**2 + (Xth + X2)**2)))

print(f'\nO escorregamento para o conjugado máximo é: {smax:.2f}\n O conjugado máximo é: {Tmax:.2f} N.m')
input('\nAperte Enter para sair...')
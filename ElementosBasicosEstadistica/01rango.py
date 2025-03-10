import pandas as pd

##Escribir un programa que pregunte al usuario por las ventas y muestre en la pantalla los datos de las ventas indexadas por loaaños antes y despues

inicio=int(input('Introduce el año de inicio ventas inicial: '))
fin=int(input('Introduce el año finalventas inicial: '))

ventas={}

for i in range(inicio,fin+1):
    ventas[i]=float(input('Introduce las ventas del año: '+ str(i) + ': '))

ventas=pd.Series(ventas)
print('Ventas \n' , ventas)
print('Ventas con descuento \n' , ventas*0.9)
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#Mostar las primeras 5 filas
print(df.head())

#Mostar las ultimas
print(df.tail())

print(df.iloc[7])

print(df["ocean_proximity"])

#Media
mediadecuarto = df["total_rooms"].mean()

print('La media de rooms es ', mediadecuarto)

#Mediana
medianadecuarto = df["total_rooms"].median()

print('La media de rooms es ', medianadecuarto)

#Suma
sumadecuarto = df["total_rooms"].sum()

print('La media de rooms es ', sumadecuarto)

#Fltro
vamosahacerunfiltro= df[df["ocean_proximity"]=='ISLAND']

print(vamosahacerunfiltro)

#Grafica

plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
#Para hacer histograma es .hist

#nombarar ejes
plt.xlabel("proximidad")
plt.ylabel("presio")
plt.title("Grafico de dispercion oceano vs precio")
plt.show()
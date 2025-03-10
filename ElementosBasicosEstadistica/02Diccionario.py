import pandas as pd

##Escribir una funcion que reciba un diccioanaria con las notasde los estudiantes del curso y devueklve

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas= pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviacion'])
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>=6].sort_values(ascending=False)

## Corchetes para listas y llaves para lo que define los datos
notas={'Juan': 9, 'Juanita': 7, 'pedro': 6.6, 'Fabian': 8.5, 'Maximiliano': 7.5, 'Sandra': 9.8, 'Rosario':9}

print(estadistica_notas(notas))
print(aprobados(notas))
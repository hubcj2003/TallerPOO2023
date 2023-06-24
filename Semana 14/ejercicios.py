#EJERCICIO 1

import pandas as pd
import matplotlib.pyplot as plt

def graficar(series, titulo):
    series.plot(kind = 'pie', title= titulo)
    plt.savefig(titulo + '.png')
    plt.show()

ventas = {'Enero': 6544, 'Febrero': 1562, 'Marzo': 1234}
series = pd.Series(ventas)
graficar(series, "Ventas del primer trimestre de 2023")

#EJERCICIO 2

import pandas as pd
import matplotlib.pyplot as plt

def graficar(series, tipo):
    series.plot(kind = tipo, title= "Evolucion del numero de ventas")
    plt.show()

series = pd.Series([154, 2156, 147, 123, 456], index=[2018, 2019, 2020, 2021, 2022])
graficar(series, 'line')
graficar(series, 'bar')
graficar(series, 'barh')
graficar(series, 'area')
graficar(series, 'pie')

#EJERCICIO 3

import pandas as pd
import matplotlib.pyplot as plt

def graficar(df):
    df.plot(kind = 'line', title= "Evolucion de ingresos y gastos", ylim= (0, max(df["Ingresos"].max(), df['Gastos'].max()) + 10))
    plt.show()

ventas ={
    'Ingresos': [13, 145, 789, 456, 123],
    'Gastos': [12, 100, 200, 245, 120],
    'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
    }
df = pd.DataFrame(ventas).set_index('Meses')

graficar(df)

#EJERCICIO 4

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# Gráfico de tipo pie con los fallecidos y supervivientes.

print(df['Survived'].value_counts())
df['Survived'].value_counts().plot(kind='pie',ylabel= "", labels = ['Muertos', 'Supervivientes'],  title= 'Fallecido y supervivientes', autopct='%.2f')
plt.show()

# Histograma con las edades.

df['Age'].plot(kind='hist',title= 'Histograma de edades')
plt.show()

# Gráfico de barras con el número de personas en cada clase.

df['Pclass'].value_counts().plot(kind='bar', title ='Personas en cada clase', ylabel = 'Cantidad de personas', xlabel = 'Clases')
plt.show()

# Gráfico de barras con el número de personas fallecidas y 
#supervivientes en cada clase.

fig, ax = plt.subplots()

print(df.groupby(['Pclass', 'Survived']).size().unstack())
df.groupby(['Pclass', 'Survived']).size().unstack().plot(kind= 'bar',ax = ax , title='Supervivientes por clase', xlabel= 'Clases', ylabel= 'Cantidades')
ax.legend(["Muertos", "Vivos"]);
plt.show()

# Gráfico de barras con el número de personas fallecidas y 
#supervivientes acumuladas en cada clase.

df.groupby(['Pclass', 'Survived']).size().unstack().plot(kind= 'bar', stacked=True, title='Supervivientes acumulados por clase', xlabel= 'Clases', ylabel= 'Cantidades')
plt.show()
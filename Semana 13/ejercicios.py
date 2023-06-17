#EJERCICIOS 1 y 2

import pandas as pd

def calcularBalance(df, meses):
    df["Balance"] = df["Ventas"] - df["Gastos"]
    #df["Balance"] = df.Ventas - df.Gastos
    #print(df)
    #print(df["Mes"].isin(meses))
    #print(df[df["Mes"].isin(meses)])
    sumBalance = df[df["Mes"].isin(meses)]["Balance"].sum()
    print(f"El balance para los meses {meses} es {sumBalance}")


ventas = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
    }

df = pd.DataFrame(ventas)
print(df)
calcularBalance(df, ["Enero", "Abril"])

#EJERCICIO 3

import pandas as pd

def analizarDatos(df):
    return pd.DataFrame([df.max(), df.min(), df.median(), df.mean()], index= ["Maximo", "Minimo", "Mediana", "Media"])

df = pd.read_csv("./cotizacion.csv", decimal=".", thousands=",", index_col="Nombre")
#df = pd.read_csv("./cotizacion.csv", delimiter=";") #Usar delimiter si la separacion del csv es con ; y no con ,
#df = pd.read_csv("./cotizacion.csv", encoding="latin-1") #Cambiar idioma a español y permitir ñ y tildes
#df = pd.read_csv("./cotizacion.csv", decimal=",", thousands=".") #para especificar la separacion que tienen los numeros en sus unidades decimales y de mil 
print(df)
print(analizarDatos(df))

#EJERCICIO 4
from audioop import reverse
import pandas as pd

#a) Generar un DataFrame con los datos del archivo.
df = pd.read_csv("./titanic.csv")
print(df)
#b) Mostrar las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus
#columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print("Dimenciones del df: ", df.shape)
print("Numero de datos del df: ", df.size)
print("Nombres de las columnas: ", df.columns.tolist())
print("Nombres de las filas: ", df.index.tolist())
print("Tipos de datos de las columnas: ", df.dtypes)
print("10 primeras filas")
print(df.head(10))
print("10 ultimas filas")
print(df.tail(10))
#c) Mostrar los datos del pasajero con identificador 148.
print(df.loc[148])
print(df.iloc[148])
#d) Mostrar las filas pares del DataFrame.
print(df[::2])
#e) Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(df["Pclass"] == 1) #Retorna una lsita con true false dependiendo si la persona iba o no en primera clase
print(df[df["Pclass"] == 1]) #Con la lista anterior se hace un filtro para que muestre solo las persona sque iban en primera clase
print(df[df["Pclass"] == 1]["Name"]) #Muestra solo los nombres de las persoans de primera clase
print(df[df["Pclass"] == 1]["Name"].sort_values()) #Ordenas normbres de forma asendente
print(df[df["Pclass"] == 1]["Name"].sort_values(ascending=False)) #Ordenas normbres de forma desendente
#f) Mostrar el porcentaje de personas que sobrevivieron y murieron.
print(df["Survived"].value_counts(normalize=True)*100)
#g) Mostrar el porcentaje de personas que sobrevivieron en cada clase.
print(df.groupby("Pclass")["Survived"].mean() *100)
#h) Eliminar del DataFrame los pasajeros con edad desconocida.
print(df.dropna(subset=["Age"]))
#i) Mostrar la edad promedio o media de las mujeres que viajaban en cada clase.
print(df[df["Sex"] == "female"].groupby("Pclass")["Age"].mean())
#j) Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df["MenorEdad"] = df["Age"] < 18
print(df)
#k) Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print("Porcentaje de menores de edad que sobrevivieron por clase: ", df[df["MenorEdad"] == True].groupby("Pclass")["Survived"].mean()*100)
print("Porcentaje de mayores de edad que sobrevivieron por clase: ", df[df["MenorEdad"] == False].groupby("Pclass")["Survived"].mean()*100)
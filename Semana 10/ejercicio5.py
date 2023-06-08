encuestados = list()
medio = ""
while medio != 'X':
    medio = input("Ingrese medio de transporte : ").upper()
    if(medio != 'X'):
        duracion = int(input("Duracion : "))
        momento = int(input("Momento : "))
        ruta = input("Ruta : ").upper()
        persona = { "medio" : medio, "duracion" : duracion , "momento": momento, "ruta": ruta }
        encuestados.append(persona)
#[{}][{}][{}][{}]

#MEDIO
cA = cT = cP = 0
#MOMENTOS
cm1 = cm2 = cm3 = cm4 = 0
#RUTAS
crA = crB = crC = crO = 0
sumrA = sumrB = sumrC = sumrO = 0
print(encuestados)

for x in encuestados:
    if x["momento"] == 1:
        cm1+=1
    elif x["momento"] == 2:
        cm2+=1
    elif x["momento"] == 3:
        cm3+=1
    else:
        cm4+=1
    if(x["medio"] == "A"):
        cA+=1
    elif(x["medio"] == "T"):
        cT+=1
    else:
        cP+=1
    if(x["ruta"] == "A"):
        crA+=1
        sumrA += x["duracion"]
    elif(x["ruta"] == "B"):
        crB+=1
        sumrB += x["duracion"]
    elif(x["ruta"] == "C"):
        crC+=1
        sumrC += x["duracion"]
    else:
        crO+=1
        sumrO += x["duracion"]
    #print(x.keys())
    #print(x.values())
    #print(x)

print("Cantidad de T : ", cT)
print("Cantidad de A : ", cA)
print("Cantidad de P : ", cP)

print("Momento con mayor cantidad de viajes es: " )
if(cm1 >= max(cm2,cm3,cm4)):
    print("1")
if(cm2 >= max(cm1,cm3,cm4)):
    print("2")
if(cm3 >= max(cm2,cm1,cm4)):
    print("3")
if(cm4 >= max(cm2 ,cm3,cm1)):
    print("4")
#USAREMOS OPERADOR TERNARIO 
# [código si se cumple] if [condición] else [código si no se cumple]
print("Tiempo promedio de viaje por ruta son:")
print(f"Av. Arequipa: {(sumrA / crA) if crA > 0 else 0}                      ")
print(f"Av. Brasil: {(sumrB / crB) if crB > 0 else 0}                        ")
print(f"Paseo de la Republica: {(sumrC / crC) if crC > 0 else 0}             ")
print(f"Otra ruta:  {(sumrO / crO) if crO > 0 else 0}                             ")
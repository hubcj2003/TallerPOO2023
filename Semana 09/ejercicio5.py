personasCargo = -1
salario = -1
while salario < 0: 
    salario = float(input("Ingrese salario : "))
while personasCargo < 0:
    personasCargo = int(input("Ingrese personas a cargo "))


if personasCargo  == 1:
    if salario <= 500:
        tipoLinea = "Prepago"
    else:
        tipoLinea = "Pospago"
elif personasCargo >=2 and personasCargo <= 4:
    if salario <= 750:
        tipoLinea = "Prepago"
    else:
        tipoLinea = "Pospago"
else:
    if salario <= 1000:
        tipoLinea = "Prepago"
    else:
        tipoLinea = "Pospago"

print("Tipo de linea al que puede acceder: ", tipoLinea) 
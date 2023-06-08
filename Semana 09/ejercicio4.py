
codigo = int(input("Ingrese codigo : "))
cantidad = int(input("Ingrese cantidad : "))

if codigo == 1:
    precio = 15.75
elif codigo == 2: #else if
    precio = 21
elif  codigo == 3: 
    precio = 8.5
elif  codigo == 4: 
    precio = 25
else:
    precio = 13.25
montoPagar = precio * cantidad

if montoPagar < 100:
    resultado = "Usted no tiene ningun descuento y debe pagar {}".format(montoPagar)
else:
    resultado = "Usted tiene un descuento de {} y debe pagar {}".format(montoPagar*0.11, montoPagar *0.89)
    
print(resultado)



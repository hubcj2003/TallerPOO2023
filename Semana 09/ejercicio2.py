#codigo = int
#while len(str(codigo)) != 10: # codigo < 1000000000 and codigo > 9999999999
#    codigo =  int(input("Ingrese codigo generado: "))
#ss = codigo % 100
#codigo = codigo // 100
#mm = codigo % 100
#codigo = codigo // 100
#hh= codigo % 100
#tttt = codigo // 100

#print("Codigo del trabajador:", tttt)
#print("Hora de entrada:      ", hh)
#print("Minuto de entrada:    ", mm)
#print("Segundos de entrada:  ", ss)

codigo = ""
while len(codigo) != 10: #6668090219
    codigo =  input("Ingrese codigo generado: ") # codigo[indiceInicial:indiceFinal + 1: saltos]
tttt = codigo[:4] #6668
hh= codigo[4:6]
mm = codigo[6:8]
ss = codigo[8:]

print("Codigo del trabajador:", tttt)
print("Hora de entrada:      ", hh)
print("Minuto de entrada:    ", mm)
print("Segundos de entrada:  ", ss)


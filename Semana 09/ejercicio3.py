longitud = -1
while longitud < 0:
    longitud = int(input("Ingrese longitud : "))

r500 = longitud // 500
longitud = longitud % 500
#longitud = longitud - r500 * 500
r300 = longitud // 300
longitud = longitud % 300
r75 = longitud // 75
longitud = longitud % 75

print(r500, " rollos de 500 metros         ")
print(f"{r300} rollo de 300 metros          ")
print(f"{r75} rollo de 75 metros           ")
print("El ultimo rollo tendra ", longitud," metro ")


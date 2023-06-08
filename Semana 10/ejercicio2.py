def graficar(n):
    for i in range(1, n + 1):
        for esp in range( n - i):
            print(" ", end="")
        for j in range(1, i * 2):
            if(j == 1 or j == i * 2 - 1):
                if i % 2 == 0:
                    print("|", end = "")
                else:
                    print("_", end = "")
            else: 
                print("*", end = "")
        print()

n = -1
while not(n >= 4 and n <= 15): 
    n = int(input("Ingrese n : "))

graficar(n)

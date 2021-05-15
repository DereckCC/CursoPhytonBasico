#Ejercicio 1

h= int(input("Ingrese la altura del triángulo (entero positivo): "))
for i in range(h):
    for j in range(i+1):
        print("*", end="")
    print("")
print("")
print("----------------------------------------")


#Ejercicio 2
n = int(input("Ingrese un número entero positivo: "))
for i in range(n,-1,-1):
    print(i,end=",")
print("")
print("----------------------------------------")


#Ejercicio 3
num = int(input("Ingrese un número entero mayor que 2: "))
i=2
while num % i !=0:
    i+=1
if i == num:
    print("El número" , num, "es primo")
else:
    print("El número", num, "no es primo")

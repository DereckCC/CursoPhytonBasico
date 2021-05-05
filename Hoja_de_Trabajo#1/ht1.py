_peso = float(input("Ingrese su peso en kilogramos:  "))
_estatura = float(input("Ingrese estatura en metros:  "))
imc =round(_peso / (_estatura)**2 ,2)
print("Su imc es: ", imc)

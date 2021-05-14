#EJERCICIO 1

_password = input("Ingrese una contraseña: ").lower()
_pass = "contra"
if _password == _pass:
    print("La contraseña", _password, " SI es la misma que", _pass)
else:
    print("La contraseña", _password, " NO es la misma que", _pass)
print()
print("------------------------------------------------")

#EJERCICIO 2

_nombre = input("Ingresa tu nombre: ")
l = ord(_nombre[0])
_sexo = input("Cual es tu sexo? M o F: ")
if _sexo == 'F' and l<=77:
    print(_nombre, "Pertenece al grupo 1")
elif _sexo == 'M' and l>=78:
    print(_nombre, "Pertence al grupo 1")
else: print(_nombre, "Pertence al grupo 2")

# #programa que valida su un numero es par 
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else
    print("El numero es impar")

paridad = "par" if numero % 2 == 0 else "impar"
print(paridad)

# #programa que valida si un numero es positivo o negativo
# numero = int(input("Ingrese un numero: "))
# if numero >= 0:
#     print("El numero es positivo")
# else 
#     print("El numero es negativo")

# #verifica usuario y contraseña
# usuario = input("Ingrese su usuario: ")
# contrasena = input("Ingrese su contraseña: ")
# if usuario == "admin" and contrasena == "1234":
#     print("Acceso concedido")
# else
#     print("Acceso denegado")
    
# #La capital de un país
# capital= input("¿Cual es la capital de mexico ")
# if capital == "Ciudad de mexico":
#     print("Correcto")
# else:
#     print("incorrecto")
# #upper pasa a minuscular y lower a mayuscula, para homologar por ejemplo en caso de que lo escriban CiudAd

# asignar una letra segun la calificacion
# calificacion = int(input("Ingrese su calificacion: "))
# if calificacion >= 90:
#     print("A")
# elif calificacion >= 80: #else if, en caso de que
#     print("B")
# elif calificacion >= 70:
#     print("C") 
# elif calificacipn >= 60:
#     print("D")
# else: 
#     print("F")

# calificacion = int(input("Ingrese su edad: "))
# if calificacion < 0 or calificacion > 120:
#     print("Invalido")
# elif calificacion > 0 and calificacion <= 12:
#     print("Niño")
# elif calificacion > 13 and calificacion <= 17:
#     print("Adolescente")
# elif calificacion > 18 and calificacion <= 59: 
#     print("Adulto")
# elif calificacion > 60:
#     print("Adulto mayor")

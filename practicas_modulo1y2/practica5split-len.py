#EJERCICIO1
#Formateador de Correo Electronico
nombredeusuario= (input("Ingrese su nombre de usuario "))
dominiodeusuario= (input("Ingrese el dominio de usuario "))
print(f"Su correo electronico es {nombredeusuario}@{dominiodeusuario}")

#Contador de palabras 
frase= (input("Ingrese alguna frase "))
palabras= frase.split() 
    #split: se usa para dividir una cadena de texto en una lista de elementos según un separador. Por defecto, divide por espacios en blanco
cantidad_palabras= len(palabras) 
    #len: devuelve la cantidad de elementos de una lista, cadena, tupla u otros objetos iterables
print(f"El numero de palabras de la frase es: {cantidad_palabras}")

#Mensaje de invitacion 
nombredelevento= (input("Ingrese el nombre del evento "))
nombredelinvitado= (input("Nombre del invitado "))
print(f"¡Bienvenido/a a {nombredelevento} {nombredelinvitado}")

#revisar otras funciones de la actividad
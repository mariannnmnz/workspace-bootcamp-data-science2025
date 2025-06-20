# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # se hace una estructura de datos
# even_number = [] #esta es la lista donde se almacenaran los pares
# for i in number: #i es contador que inicia en 0
#     if i % 2 == 0: #aqui pasaria o recorreria el for, y la condicion es que el restante de 0, es decir sea par
#         even_number.append(i) #como len, append es una funcion
# print("Los números pares son: ", even_number) #recordar el while, que tenia condicion, for recorre cosas, es iterativo

# #esto seria como en java u otros programas, en python es mas simple, directo
# for ([expresion-inicial]); [condicion]: [expresion-final]sentencia
# for (var i= 0; i < 9; i++)

# letters = ['a', 'b', 'c', 'd', 'e']
# reversed_letters = []
# for i in range(len(letters)-1, -1, -1): #range es rango de letras, de que numero a numero
#     reversed_letters.append(letters[i])
# print(reversed_letters)

# range_number2= range(11,1,-1)
# for i in range_number2:
#     print(i)
# print(type(range_number2))

# number = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# total= 0
# for i in number:
#     total += i
# print(total)

number2= [1, 2, 7, 4, 5, 7, 7, 8, 9, 10]
unique_numbers = []
for i in number2:
    if i not in unique_numbers:
        unique_numbers.append(i)
print("Los numeros unicos son:", unique_numbers)

suma = sum(number2)
suma_unicos = sum(unique_numbers)
print("La suma de los numeros unicos es:", suma_unicos)
print("La suma de los numeros es:", suma) #snake_case y camelCase
#for y while recorrer, pero se ocupan ambos para recorrer
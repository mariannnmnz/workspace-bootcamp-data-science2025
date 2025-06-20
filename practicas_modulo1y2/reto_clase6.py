#Reto 1 programa
opcion = "" 
lista= [1, 2, 6, 3, 51, 65 7, 38, 9]
while opcion != 5:
    print("MENU INTERACTIVO")
    print("1. Agregar un número a una lista")
    print("2. Ver la lista completa")
    print("3. Ver solo los números pares")
    print("4. Ver solo los numeros impares")
    print("5. Salir del programa")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        lista.append(float(input("Ingrese el numero que sedea agregar: ")))
    elif opcion == "2":
        print(f"La lista completa es {lista}")
    elif opcion == "3":
        par= []
        for i in lista:
            if i%2 == 0:
                par.append(i)
    elif opcion == "4":
        for i in lista:
            if i
    elif opcion == "5":
        print("Saliendo del programa")
    
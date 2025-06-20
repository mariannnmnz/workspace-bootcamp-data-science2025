frutas= {'apple', 'banana', 'cherry', 'date', 'elderberry'}
print(frutas)

#recordar intersecciones
A={5, 10, 15, 20, 25}
B={10, 20, 30, 40, 50}
print("union", A|B) #Union de conjuntos
A.add(35) #Agregar un elemento al conjunto A
print("interseccion", A&B) #Intereccion de conjuntos
B.remove(30)  #Eliminar un elemento del conjunto B
print("diferencia", A-B) #Diferencia de conjuntos
print("diferencia simetrica", A^B) #Diferencia simetrica de conjuntos
print("A es subconjunto de B", A.issubset(B)) #Subconjunto de conjuntos
print("A es superconjunto de B", A.issuperset(B)) #Super
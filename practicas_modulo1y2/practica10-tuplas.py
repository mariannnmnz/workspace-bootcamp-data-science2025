coordenadas = [(122, 467), (56,78), (12, 45), (67, 89), (34,56)]
for punto in coordenadas:
    print(f"Coordenada: {punto[0]}, {punto[1]}")
coordenadas.add((100, 200)) # Esto no funcionara porque las tuplas son inmutables


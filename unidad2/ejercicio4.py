#el mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","x","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#recorriendo la matriz con ciclos anidados
#ciclo externo para manejar filas(i)
for i in range (filas):
    #ciclo externo para manejar columnas(j)
    for j in range(columnas):
        #verificamos si encontramos el tesoro
        if mapa[i][j]=="x":
            print(f"mapa encontrado en la posicion [{i}][{j}]")
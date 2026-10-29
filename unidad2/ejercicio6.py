tabla = [
    ["nombre", "edad", "calificacion"],
    ["ximena", 16, 8.0],
    ["jesus", 16, 7.0],
    ["jorge", 16, 7.0],
    ["sherlyn", 15, 9.0],
    ["mariel", 16, 9.0],
    ["oscar", 16, 8.0],
    ["ulises", 16, 7.0],
    ["dulce", 16, 9.0],
    ["karla", 16, 9.0],
    ["darina", 16, 9.0]
]
filas = len(tabla)
columnas = len(tabla[0])
alumno_que_buscas = input("introduce el nombre del alumno: ")
for i in range(filas):
    for j in range(columnas):
        if str(tabla[i][j]) == alumno_que_buscas:
            print(f"nombre encontrado en la posicion [{i}][{j}]")
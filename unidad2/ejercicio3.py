
letras = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'g'],
    ['h', 'i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p', 'q'],
    ['r', 's', 't', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]
filas = 0
for fila in letras:
    filas += 1
for i in range(filas):
    columnas = 0
    for elemento in letras[i]:
        columnas += 1
    for j in range(columnas):
        print(f"[{i}][{j}] = {letras[i][j]}")
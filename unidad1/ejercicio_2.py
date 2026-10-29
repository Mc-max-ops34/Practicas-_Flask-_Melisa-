
try:
    alumnos=["sherlyn","mariel","jorge","jesus","ximena"]
    calificaciones=[6,7,8,9,5]
    print("lista de alumnos:",alumnos)
    print("lista de calificaciones:",calificaciones)
    print("alumnos con indices impares:")
    print(alumnos[1])
    print(alumnos[5])
except IndexError:
    print("no existe este rango")
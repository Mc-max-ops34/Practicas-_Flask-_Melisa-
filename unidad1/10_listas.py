#declarando una lista
try:
    materias=["programacion","filosofia","matematicas","ingles"]
    print(materias[0]) 
    materias.append("programacion") 
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("matematicas")
    print(materias)
except IndexError:
    print("indice incorrecto:")

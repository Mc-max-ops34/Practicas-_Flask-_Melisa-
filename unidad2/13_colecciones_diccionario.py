#creando un diccionario
persona={
    "nombre":"melisa",
    "edad":16,
    "profesion":"programador",
    "estudiante":True

}
print(persona)
#accediendo a un valor en especifico
print(persona["nombre"])
#se puede usar el metodo get()
#es util porque no marca error si el valor no existe  
print(persona.get("profesion"))
#modificar un valor existente
persona["edad"]=16
print(persona["edad"])
#agregar un par(clave:valor)
persona["ciudad"]="san jose del rincon"
print(persona)
#recorrer un diccionario con un bucle
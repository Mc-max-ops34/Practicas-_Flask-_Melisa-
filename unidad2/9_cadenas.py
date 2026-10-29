#cadenas y concatenacion con (+)
cadena1='hola'
cadena2= 'mundo'
multilinea="""esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)#print(f"(cadena1)")
#cadenas y repeticion
eco='ja'*3
print(eco)
#cambiar una cadena de minuscula  a mayuscula
tu_nombre='melisa'
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#remplazar un texto de una cadena
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de cadenas (F- String)
edad=17
nombre='melisa'
mensaje=f"hola, me llamo {nombre} y tengo\n{edad} años"
print(mensaje)
#contar los caracteres de una cadena
texto="¡felicidades por aun continuar en el cecy!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="aprender python es divertido"
if "java" in oracion:
    print("encontrado")
else:
    print("no esta")
#validar contenido de una cadena
nlista="melisa"
print(nlista.isalpha())
print(nlista.isdigit())
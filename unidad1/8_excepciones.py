#ejemplo 1 sin manejo de excepciones
numero1=float(input("ingresa el primer numero"))
numero2=str(input("ingresa el segundo numero"))
try:
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("error:no se puede dividir con una letra")
except ValueError:
    print("error:no se puede dividir con una letra")
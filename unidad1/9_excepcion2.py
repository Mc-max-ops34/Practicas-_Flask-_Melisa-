try:
    numero1=float(input("ingresa el primer numero"))
    numero2=float(input("ingresa el segundo numero"))
    resultado=numero1/numero2
except ValueError:
    print("solo introduce numeros")
except ZeroDivisionError:
     print("solo introduce cero")
else:
    print("el resultado es",resultado)
finally:
    print("programa finalizado")
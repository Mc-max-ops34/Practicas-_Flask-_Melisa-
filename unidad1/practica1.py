def calcular_venta():
    producto = str(input("Introduce el nombre de tu producto: "))
    precio = float(input("Introduce el precio de tu producto: "))
    cantidad = int(input("Cantidad: "))
    total = precio * cantidad
    print("\n--- lista de venta ---")
    print("Producto:", producto)
    print("Precio: $", precio)
    print("Cantidad:", cantidad)
    print("Total: $", total)
calcular_venta()
def calcularprecio():
    precios = {
        "Pan": 1.40,
        "Huevos": 2.30,
        "Cebolla": 0.85,
        "Aceite": 4.85
    }
    
    producto = input("Ingrese el producto: ").capitalize()
    cantidad = int(input("Ingrese el número de unidades: "))
    
    if producto in precios:
        preciototal = precios[producto] * cantidad
        print(f"El precio de {cantidad} unidades de {producto} es {preciototal:.2f} euros.")
    else:
        print("El producto no está en la lista de precios.")

calcularprecio()
def obtenerinformacionusuario():
    
    usuario = {
        "nombre": input("Escriba su nombre: "),
        "edad": input("Escriba su edad: "),
        "direccion": input("Escriba su dirección: "),
        "telefono": input("Escriba su número de teléfono: ")
    }
    
    print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")

obtenerinformacionusuario()


def recopilarinformacion():
    persona = {}
    
    claves = ["Nombre", "Edad", "Sexo", "Teléfono", "Correo electrónico"]
    
    for clave in claves:
        valor = input(f"Ingrese {clave}: ")
        persona[clave] = valor
        
        print("Información actualizada:", persona)


recopilarinformacion()
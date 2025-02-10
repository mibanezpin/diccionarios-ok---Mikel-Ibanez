def gestionaralumnado():
    alumnado = {}
    
    while True:
        print("\nMenú:")
        print("1. Añadir alumno/a")
        print("2. Eliminar alumno/a")
        print("3. Mostrar alumno/a")
        print("4. Listar todo el alumnado")
        print("5. Listar alumnado aprobado")
        print("6. Terminar")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nif = input("Escribe el NIF del alumno/a: ")
            nombre = input("Escribe el nombre: ")
            apellidos = input("Escribe los apellidos: ")
            telefono = input("Escribe el teléfono: ")
            correo = input("Escribe el correo electrónico: ")
            aprobado = input("¿Ha aprobado? (s/n): ").strip().lower() == "s"
            
            alumnado[nif] = {
                "nombre": nombre,
                "apellidos": apellidos,
                "telefono": telefono,
                "correo": correo,
                "aprobado": aprobado
            }
            print("Alumno/a añadido/a correctamente.")
        
        elif opcion == "2":
            nif = input("Escribe el NIF del alumno/a a eliminar: ")
            if nif in alumnado:
                del alumnado[nif]
                print("Alumno/a eliminado/a correctamente.")
            else:
                print("No se encontró un alumno/a con ese NIF.")
        
        elif opcion == "3":
            nif = input("Escribe el NIF del alumno/a a mostrar: ")
            if nif in alumnado:
                print("Datos del alumno/a:", alumnado[nif])
            else:
                print("No se encontró un alumno/a con ese NIF.")
        
        elif opcion == "4":
            if alumnado:
                print("\nLista de alumnado:")
                for nif, datos in alumnado.items():
                    print(f"NIF: {nif}, Nombre: {datos['nombre']}")
            else:
                print("No hay alumnado registrado.")
        
        elif opcion == "5":
            aprobados = {nif: datos for nif, datos in alumnado.items() if datos["aprobado"]}
            if aprobados:
                print("\nLista de alumnado aprobado:")
                for nif, datos in aprobados.items():
                    print(f"NIF: {nif}, Nombre: {datos['nombre']}")
            else:
                print("No hay alumnado aprobado.")
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

gestionaralumnado()


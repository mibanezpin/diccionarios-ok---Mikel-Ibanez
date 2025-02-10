def creardiccionariotraduccion():
    diccionario = {}
    
    while True:
        entrada = input("Escriba una palabra y su traducción (español:inglés) o 'terminar' para finalizar: ")
        if entrada.lower() == "terminar":
            break
        
        if ":" in entrada:
            palabra, traduccion = entrada.split(":")
            diccionario[palabra.strip()] = traduccion.strip()
        else:
            print("Formato incorrecto. Use 'palabra:traducción'.")
    
    frase = input("Escriba una frase en español para traducir: ")
    palabras = frase.split()
    
    traduccion = " ".join([diccionario.get(palabra, palabra) for palabra in palabras])
    
    print("Frase traducida:", traduccion)

creardiccionariotraduccion()
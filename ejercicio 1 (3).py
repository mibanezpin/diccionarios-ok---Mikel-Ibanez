while True:
    divisas = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    divisaingresada = input("Por favor, ingresa una divisa que sea Euro, Dollar o Yen").capitalize()
    if divisaingresada in divisas:
        print(f"El símbolo de la divisa {divisaingresada} es: {divisas[divisaingresada]}")
    else:
        print("Lo siento, la divisa ingresada no está en el diccionario.")

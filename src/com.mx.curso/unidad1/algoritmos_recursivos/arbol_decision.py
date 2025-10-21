def es_manzana(pregunta):
    respuesta = input(pregunta + " (sí/no): ")

    if pregunta == "¿Es roja?":
        if respuesta.lower().strip() == "sí":
            return es_manzana("¿Es redonda?")
        else: 
            return "Podría ser un plátano 🍌."
    elif pregunta == "¿Es redonda?":
        if respuesta.lower().strip() == "sí":
            return "¡Podría ser una manzana 🍎!"
        else:
            return "Podría ser una fresa 🍓"
        
resultado = es_manzana("¿Es roja?")
print("Resultado: ",resultado)

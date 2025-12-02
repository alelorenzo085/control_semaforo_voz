def procesar_comando(text, canvas, luces, resultado_label, ventana):
    """
    Procesa el comando de voz y actualiza el semáforo tricolor.
    luces: tupla (rojo, amarillo, verde) con los IDs de los óvalos en el canvas
    """
    rojo, amarillo, verde = luces
    text = text.lower()  # Convertimos a minúsculas para evitar errores

    if "enciende" in text and "roja" in text:
        canvas.itemconfig(rojo, fill="red")
        canvas.itemconfig(amarillo, fill="grey20")
        canvas.itemconfig(verde, fill="grey20")
        resultado_label.config(text="🔴 Luz roja encendida")
    elif "enciende" in text and "amarilla" in text:
        canvas.itemconfig(rojo, fill="grey20")
        canvas.itemconfig(amarillo, fill="yellow")
        canvas.itemconfig(verde, fill="grey20")
        resultado_label.config(text="🟡 Luz amarilla encendida")
    elif "enciende" in text and "verde" in text:
        canvas.itemconfig(rojo, fill="grey20")
        canvas.itemconfig(amarillo, fill="grey20")
        canvas.itemconfig(verde, fill="green")
        resultado_label.config(text="🟢 Luz verde encendida")
    elif "apaga" in text or "todas" in text:
        canvas.itemconfig(rojo, fill="grey20")
        canvas.itemconfig(amarillo, fill="grey20")
        canvas.itemconfig(verde, fill="grey20")
        resultado_label.config(text="💤 Todas las luces apagadas")
    elif "salir" in text:
        resultado_label.config(text="👋 Cerrando programa...")
        ventana.after(1000, ventana.destroy)
    else:
        resultado_label.config(text="Comando no reconocido")
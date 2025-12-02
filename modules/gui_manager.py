import tkinter as tk

def crear_ventana():
    """Crea la ventana principal con semáforo y devuelve los widgets principales."""
    ventana = tk.Tk()
    ventana.title("Semáforo controlado por voz 🚦")
    ventana.geometry("400x500")
    ventana.config(bg="#1e1e1e")

    # Título de la ventana
    titulo = tk.Label(ventana, text="CONTROL POR VOZ - SEMÁFORO TRICOLOR",
                      font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00ffcc")
    titulo.pack(pady=10)

    # Canvas donde se dibujarán las luces redondas del semáforo
    canvas = tk.Canvas(ventana, width=150, height=400, bg="#111", highlightthickness=0)
    canvas.pack(pady=20)

    # Crear luces redondas (óvalos) apagadas inicialmente (grey20)
    rojo = canvas.create_oval(25, 30, 125, 130, fill="grey20")
    amarillo = canvas.create_oval(25, 150, 125, 250, fill="grey20")
    verde = canvas.create_oval(25, 270, 125, 370, fill="grey20")

    # Label de instrucciones
    texto_label = tk.Label(ventana, text="Pulsa 'Escuchar' y da un comando. 🎤",
                           font=("Arial", 12), bg="#1e1e1e", fg="white")
    texto_label.pack(pady=10)

    # Label para mostrar resultados de reconocimiento
    resultado_label = tk.Label(ventana, text="...", font=("Arial", 14, "bold"),
                               bg="#1e1e1e", fg="#00ffcc")
    resultado_label.pack(pady=10)

    # Devolvemos todos los widgets necesarios
    return ventana, canvas, rojo, amarillo, verde, texto_label, resultado_label
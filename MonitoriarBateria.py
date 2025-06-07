import psutil
from plyer import notification
import time
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def check_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "conectada"
    else:
        status = "desconectada"

    status_label.config(text=f"Batería {status}, tiene {percent}% de carga.")

    if percent <= 15 and not plugged:
        for _ in range(2):
            notification.notify(
                title="Advertencia de batería baja",
                message="Debe conectar el cargador de la batería.",
                app_icon=None
            )
            time.sleep(1)  # Agregar un retraso de 1 segundo entre las notificaciones
    elif percent >= 95 and plugged:
        for _ in range(2):
            notification.notify(
                title="Advertencia de batería alta",
                message="Debe desconectar la corriente eléctrica para evitar dañar la batería.",
                app_icon=None
            )
            time.sleep(1)  # Agregar un retraso de 1 segundo entre las notificaciones
    elif percent < 18 and not plugged:
        for _ in range(3):
            notification.notify(
                title="Advertencia de batería baja",
                message="La carga de la batería es inferior al 18%. Conéctela a una fuente de alimentación.",
                app_icon=None
            )
            time.sleep(1)  # Agregar un retraso de 1 segundo entre las notificaciones

    # Intervalo de tiempo en segundos (ejemplo: 30 segundos = 30)
    window.after(30000, check_battery)

window = tk.Tk()
window.title("Estado de Carga de la Batería")
window.geometry("300x150")

# Crear un estilo de interfaz gráfica moderno
style = ttk.Style()
style.theme_use("clam")  # Puedes cambiar el tema a otro de tu elección

# Cargar una imagen predeterminada del sistema
image = Image.open("battery_icon.png")  # Ruta de la imagen del icono de la batería o usa otra imagen
image = image.resize((50, 50))  # Ajustar el tamaño de la imagen según sea necesario
icon = ImageTk.PhotoImage(image)
icon_label = ttk.Label(window, image=icon)
icon_label.pack(pady=10)

status_label = ttk.Label(window, text="Batería está desconectada.", font=("Arial", 11))
status_label.pack(pady=10)
status_label.configure(foreground='blue')

check_battery()

window.mainloop()



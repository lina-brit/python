from PIL import ImageTk, Image
import tkinter as tk

ruta_imagen = 'caro2.jpg'

# Crea la ventana principal
ventana = tk.Tk()

# Carga la imagen
img = Image.open(ruta_imagen)
img = img.resize((400, 400), Image.ANTIALIAS)  # Redimensiona la imagen
img_tk = ImageTk.PhotoImage(img)

# Crea el lienzo y agrega la imagen
lienzo = tk.Canvas(ventana, width=400, height=400)
lienzo.pack()
lienzo.create_image(200, 200, image=img_tk)

# Define la función para redimensionar la imagen
def redimensionar_img(event):
    global img_tk
    w, h = event.width, event.height
    img = Image.open(ruta_imagen)
    img = img.resize((w, h), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    lienzo.delete("all")
    lienzo.create_image(w, h, image=img_tk)

# Vincula la redimensión de la ventana a la función
ventana.bind("<Configure>", redimensionar_img)

# Inicia el bucle principal de la ventana
ventana.mainloop()

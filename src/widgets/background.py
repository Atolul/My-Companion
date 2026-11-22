import tkinter as tk 
from PIL import Image, ImageTk

def create_background(room, image_path):

    original_image = Image.open(image_path).convert("RGBA")

    background = tk.Label(room, bg=room.cget("bg"), bd=0)
    background.place(x=0, y=0, relwidth=1, relheight= 1)

    def resize_background(event):
        # Resize image to the window size
        if event.width <= 1 or event.height <=1:
            return
        resized = original_image.resize((event.width, event.height), Image.Resampling.NEAREST
        )

        image = ImageTk.PhotoImage(resized)

        background.config(image=image, bg=room.cget("bg"))
        background.image = image

    room.bind("<Configure>", resize_background)

    background.lower()

    return background


from tkinter import Button

def create_image_button(parent, image, command, bg=None):
    if bg is None:
        bg = parent.cget("bg")

    hover_bg = "#86a6af"
    button = Button(
        parent,
        image=image,
        command=command,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        bg=bg,
        activebackground="#b0c0bf",
        cursor="hand2"
    )

    button.bind("<Enter>", lambda event: button.config(bg=hover_bg))
    button.bind("<Leave>", lambda event: button.config(bg=bg))

    return button


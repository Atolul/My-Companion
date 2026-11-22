import tkinter as tk
from widgets.customizer import bg_color

def create_popup(window, title, width=350, height=320):

    #Create popup
    popup = tk.Frame(window, bg=bg_color, width=width, height=height, bd=2, relief="solid")

    # Prevent popup from shrinking to fit its contents
    popup.pack_propagate(False)

    tk.Label(popup, text=title, bg=bg_color).pack(pady=20)

    # Close button
    close_button = tk.Button(
        popup, text="✖",
        command=popup.place_forget,
        bg=bg_color,
        fg="black",
        borderwidth=1,
        activebackground= bg_color,
        relief="solid"
    )

    close_button.place(relx=1.0, x=-10, y=10, anchor="ne")

    # Function to show popup
    def show():
        popup.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        popup.lift()

    return popup, show




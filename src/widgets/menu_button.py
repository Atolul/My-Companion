from tkinter import *
from widgets.customizer import bg_color

def create_menu(room):

    menu_image = PhotoImage(file="assets/menu.png")

    #Dropdown menu
    menu_frame = Frame(room, bg=bg_color, bd=0)

    #Show/hide menu
    def toggle_menu():
        if menu_frame.winfo_ismapped():
            menu_frame.place_forget()
        else:
            menu_frame.place(relx=0.0, x=10, y=50, anchor="nw")

# Create a menu option
    def menu_option(text, command=None):
        button = Button(
            menu_frame,
            text=text,
            command=command,
            bg=bg_color,
            fg="black",
            activebackground=bg_color,
            activeforeground= "black",
            relief="solid",
            borderwidth=1,
            width=15,
            anchor="center",
            padx=10
        )

        button.pack(fill="x", padx=5, pady=5)

# Menu button
    menu_button = Button(
        room, image=menu_image, command=toggle_menu, borderwidth=0, highlightthickness=0, bg=bg_color, activebackground=bg_color
    )

# Put menu at top right
    menu_button.place(relx=0.0, x=10, y=10, anchor="nw")

# Keep image alive
    room.menu_image = menu_image

    return menu_option

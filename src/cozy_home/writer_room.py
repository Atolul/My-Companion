from tkinter import *
import tkinter as tk
from widgets.button import create_image_button
from widgets.menu_button import create_menu
from widgets.popup_window import create_popup
from widgets.customizer import bg_color
from data.data import load_data, save_data

def create_writer_room(window, go_library, go_writer, go_study, go_farm, go_bed):


    writer_image= PhotoImage(file="assets/writer.png")
    study_image= PhotoImage(file="assets/study.png")
    bed_image= PhotoImage(file="assets/bed.png")
    farm_image= PhotoImage(file="assets/farm.png")
    library_image= PhotoImage(file="assets/library.png")
    bg_image = PhotoImage(file="assets/writer_room.png")

    room = Frame(window, bg="#b0c0bf")

    menu_option = create_menu(room)

    #------Popup Window---------
    new_project_window, show_newProject = create_popup(room, "SELECT WORK TYPE")

    # new project
    project_type=None

    def choose_type(type_name):
        nonlocal project_type

        project_type = type_name

        #Remove the current popup content
        for widget in new_project_window.winfo_children():
            widget.destroy()

        #Project name title
        tk.Lable(
            new_project_window,
            text={type_name},
            bg=bg_color
        ).pack(pady=20)

        # Name input
        name_entry = tk.Entry(new_project_window)
        name_entry.pack(pady=10)

        def create_project():
            project_name = name_entry.get().strip()

            if project_name == "":
                return

            data = load_data()

            data["projects"].append({
                "name": project_name,
                "type": project_type
            })

            save_data(data)

            new_project_window.place_forget()

        tk.Button(
            new_project_window,
            text="Fan-fiction",
            command=lambda: choose_type("Fanfic"),
            bg=bg_color
        ).pack(fill="x", padx=30, pady=5)

        tk.Button(
                new_project_window,
                text="Fiction",
                command=lambda: choose_type("Fic"),
                bg=bg_color
            ).pack(fill="x", padx=30, pady=5)

        tk.Button(
                new_project_window,
                text="Non-fiction",
                command=lambda: choose_type("Non-Fic"),
                bg=bg_color
            ).pack(fill="x", padx=30, pady=5)


    
    menu_option("New Work", show_newProject)


    button_frame = Frame(room, bg="#b0c0bf")
    button_frame.pack(anchor="ne", padx=10, pady=10)
    
    writer_button = create_image_button(button_frame, writer_image, go_writer, bg="#86a6af")
    writer_button.pack(side="left", padx=5)

    study_button = create_image_button(button_frame, study_image, go_study)
    study_button.pack(side="left", padx=5)

    library_button = create_image_button(button_frame, library_image, go_library)
    library_button.pack(side="left", padx=5)

    farm_button = create_image_button(button_frame, farm_image, go_farm)
    farm_button.pack(side="left", padx=5)

    bed_button = create_image_button(button_frame, bed_image, go_bed)
    bed_button.pack(side="left", padx=5)
    
    

    room.writer_image = writer_image
    room.study_image = study_image
    room.bed_image = bed_image
    room.farm_image = farm_image
    room.library_image = library_image




    return room


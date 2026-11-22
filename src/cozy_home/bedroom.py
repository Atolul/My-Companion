from tkinter import *
import tkinter as tk
from widgets.button import create_image_button
from widgets.animation import create_animation
from widgets.background import create_background



def create_bedroom(window, go_library, go_writer, go_study, go_farm, go_bed):
    writer_image= PhotoImage(file="assets/writer.png")
    study_image= PhotoImage(file="assets/study.png")
    bed_image= PhotoImage(file="assets/bed.png")
    farm_image= PhotoImage(file="assets/farm.png")
    library_image= PhotoImage(file="assets/library.png")

    room = tk.Frame(window)
  
    create_background(room, "assets/bedroom.png")

    button_frame = Frame(room, bg="#b0c0bf")
    button_frame.pack(anchor="ne", padx=10, pady=10)
    
    writer_button1 = create_image_button(button_frame, writer_image, go_writer)
    writer_button1.pack(side="left", padx=5)

    study_button = create_image_button(button_frame, study_image, go_study)
    study_button.pack(side="left", padx=5)

    library_button = create_image_button(button_frame, library_image, go_library)
    library_button.pack(side="left", padx=5)

    farm_button = create_image_button(button_frame, farm_image, go_farm)
    farm_button.pack(side="left", padx=5)

    bed_button = create_image_button(button_frame, bed_image, go_bed, bg="#86a6af")
    bed_button.pack(side="left", padx=5)
    
    

    room.writer_image = writer_image
    room.study_image = study_image
    room.bed_image = bed_image
    room.farm_image = farm_image
    room.library_image = library_image

    run_frames = [
        PhotoImage(file="assets/sleeping1.png").zoom(4, 4),
        PhotoImage(file="assets/sleeping2.png").zoom(4, 4),
        PhotoImage(file="assets/sleeping3.png").zoom(4, 4),
        PhotoImage(file="assets/sleeping4.png").zoom(4, 4),
        PhotoImage(file="assets/sleeping1.png").zoom(4, 4),
        ]

    wakeup_frames = [
        PhotoImage(file="assets/wake2.png").zoom(4, 4),
        PhotoImage(file="assets/wake2.png").zoom(4, 4),
        PhotoImage(file="assets/wake2.png").zoom(4, 4),
        PhotoImage(file="assets/wake1.png").zoom(4, 4),
        PhotoImage(file="assets/wake1.png").zoom(4, 4),
    ]

    def clicked(event):
        change_animation(wakeup_frames, new_loop=False, new_speed=700, return_to_original=True)

    sprite, play_run, change_animation, bind_animation = create_animation(room, run_frames, x=300, y=300, speed=250, loop=True, on_click=clicked)

    play_run()


    return room
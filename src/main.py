from tkinter import *

from cozy_home.bedroom import create_bedroom
from cozy_home.writer_room import create_writer_room
from cozy_home.study_room import create_study_room
from cozy_home.library import create_library
from cozy_home.farm import create_farm

window = Tk() #instantiate an instance of a window
window.geometry("400x400")
window.title("My Companion")
window.resizable(False,False)
window.config(background="#b0c0bf")

current_room = None

def show_room(room):
    global current_room

# Hide the current room
    if current_room is not None:
        current_room.pack_forget()

# Show the new room
    current_room = room
    current_room.pack(fill="both", expand=True)

# Navigation functions
def go_to_writerRoom():
    show_room(writer_room)

def go_to_studyRoom():
    show_room(study_room)

def go_to_library():
    show_room(library)

def go_to_farm():
    show_room(farm)

def go_to_bedRoom():
    show_room(bedroom)

# # Create rooms
bedroom = create_bedroom(
    window, go_to_library, go_to_writerRoom, go_to_studyRoom, go_to_farm, go_to_bedRoom
)

library = create_library(
    window, go_to_library, go_to_writerRoom, go_to_studyRoom, go_to_farm, go_to_bedRoom
)

writer_room = create_writer_room(
    window, go_to_library, go_to_writerRoom, go_to_studyRoom, go_to_farm, go_to_bedRoom
)

study_room = create_study_room(
    window, go_to_library, go_to_writerRoom, go_to_studyRoom, go_to_farm, go_to_bedRoom
)

farm = create_farm(
    window, go_to_library, go_to_writerRoom, go_to_studyRoom, go_to_farm, go_to_bedRoom
)

# Start at writer room (for now)
show_room(bedroom)

window.mainloop() #place window on computer screen. Listen for events
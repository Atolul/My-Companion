import tkinter as tk

def create_animation(parent, frames, x=0, y=0, speed=100, loop=True, on_click=None):

    sprite= tk.Label(
        parent, 
        image=frames[0],
        bg=parent.cget("bg")
    )

    sprite.place(relx=0.5, rely=0.5, anchor="center")

    #Original animation
    original_frames = frames
    original_loop = loop    

    current_frames = frames
    current_loop = loop

  

    #What animation should play after a temporary animation?
    return_frames = None
    next_loop = True

    after_id = None



    def play(index=0):
            nonlocal after_id
            nonlocal current_frames
            nonlocal current_loop
            nonlocal return_frames
            nonlocal next_loop

            # Show current frame
            sprite.config(image=current_frames[index])

            # Animation finished
            if not current_loop and index == len(current_frames) - 1:
                  after_id = None

                  # Return somewhere if requested
                  if return_frames is not None:
                        current_frames = return_frames
                        current_loop = next_loop

                        return_frames = None

                        play(0)

                  return

            # Calculate next frame
            next_index = (index + 1) % len(current_frames)

            after_id = parent.after(
                  speed, lambda: play(next_index)
            )

    def stop():
        nonlocal after_id

        if after_id is not None:
            parent.after_cancel(after_id)
            after_id = None

    def change_animation(new_frames, new_loop=True, return_to=None, return_loop=True, return_to_original=False):
          nonlocal current_frames
          nonlocal current_loop
          nonlocal return_frames
          nonlocal next_loop

          stop()

          current_frames = new_frames
          current_loop = new_loop

          # Decide where to return
          if return_to_original:
                return_frames = original_frames
                next_loop = original_loop

          elif return_to is not None:
                return_frames = return_to
                next_loop = return_loop

          else:
                return_frames = None

          play(0)


    # When this animation is clicked, trigger another animation
    def bind_animation(other_animation):
          other_sprite, other_play, other_change, other_bind = other_animation
          
          
          sprite.bind("<Button-1>", lambda event: other_play())

          sprite.config(cursor="hand2")


    # Only make it clickable if on_click was provided
    if on_click is not None:
          sprite.bind("<Button-1>", on_click)
          sprite.config(cursor="hand2")

    # Store frames on the sprite so other animations can access them
    sprite.frames = current_frames

    return sprite, play, change_animation, bind_animation

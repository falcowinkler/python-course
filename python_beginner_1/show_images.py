from tkinter import *
from typing import List, Any

root = Tk()
# Silence thonny warning
def init_frames() -> List[Any]:
    return list()
frames = init_frames()

label = Label(root)
should_run = True

def add_frame(i):
    if len(frames) > 1000:
        raise(Exception("Please don't add more than 1000 images to your animation :)"))
    frames.append(PhotoImage(file='images/mygif.gif',format = 'gif -index %i' % (i)))

def update(repeat, ind):
    global should_run
    if ind >= len(frames):
        if repeat:
            ind = 0
        else:
            return
        
    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    if should_run:
        root.after(50, update, repeat, ind)
    
def on_close():
    global root
    global should_run
    should_run=False
    root.quit()
    
def start(repeat=False):
    label.pack()
    root.after(0, update, repeat, 0)
    button = Button(root, text="Stop", command = on_close )
    button.pack()
    root.mainloop()

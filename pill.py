
from tkinter import *
from options import *

def give_pill():
    #pill count
    #add pills
    #pill information
    small_font = ("Arial", 10)
    medium_font = ("Arial", 15)
    large_font = ("Arial", 20)
    
    root = Tk()
    root.running = True
    root.configure(bg="white")

    title_label = Label(root, text="Please wait, medicine dispensing", bg="white", font=large_font)
    title_label.grid(row=0, column=0)

    def on_exit():
        root.running = False


    root.protocol("WM_DELETE_WINDOW", on_exit)

    cancel_button = Button(root, text= "Cancel", command= on_exit)
    cancel_button.grid(row=2, column= 1)

    while root.running:
        root.update()
    root.destroy()

    #mechanical processes
    #update pill count


if __name__ == "__main__":
    give_pill()
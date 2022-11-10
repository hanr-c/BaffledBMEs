#main for BB

from options import show_options
from tkinter import *
from pill import give_pill

def show_app():

    small_font = ("Arial", 10)
    medium_font = ("Arial", 15)
    large_font = ("Arial", 20)

    root = Tk()
    root.running = True
    root.configure(bg="white")

    frame = None
    frame = Frame(root, bg="gray", relief=RAISED, borderwidth=1)
    frame.grid(row=1, column=1, rowspan=3, columnspan=3)
    frame_label = Label(root, text = "Baffled BMEs Pill Dispenser",font = medium_font)
    frame_label.grid(row=0, column=0)



    def on_exit():
        root.running = False
        # save data
    root.protocol("WM_DELETE_WINDOW", on_exit)


    def on_pill():
        #checklist variables go into paranthesis
        # activate motors to give neccessary pills from the checklist
        give_pill()


    def give_options():
        show_options()



    options_button = Button(root, text="Options", command=give_options, bg="white", font= medium_font)
    options_button.grid(row=3, column=0, padx = 10, pady =10)

    pill_button = Button(root, text="Give Pill", command=on_pill, bg="white", font= medium_font)
    pill_button.grid(row=3, column=3, padx = 10, pady =10)


    while root.running:
        root.update()
    root.destroy()
     


if __name__ == "__main__":
    show_app()



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
    print("here")

    # frame = None

    def closing():
        root.running = False
        app_frame.exit()
        print("closing")
    root.protocol("WM_DELETE_WINDOW", closing)


    def give_pill(symptoms = None):
        #checklist variables go into paranthesis
        # activate motors to give neccessary pills from the checklist
        print("here")


    def give_options():
        show_options()

    def on_exit():
        #save all data
        print("closing 2")
        root.running = False

    app_frame = Frame(root, bg="gray")

    options_button = Button(root, text="Options", command=give_options, bg="white", font= medium_font)
    options_button.grid(row=3, column=0)

    pill_button = Button(root, text="Give Pill", command=give_pill, bg="white", font= medium_font)
    pill_button.grid(row=3, column=3)

    root.mainloop()

    print("here 2")
    


if __name__ == "__main__":
    show_app()


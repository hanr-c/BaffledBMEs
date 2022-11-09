from tkinter import *

def show_options():
    #pill count
    #add pills
    #pill information

    small_font = ("Arial", 10)
    medium_font = ("Arial", 15)
    large_font = ("Arial", 20)

    root = Tk()
    root.running = True
    root.configure(bg="white")

    title_label = Label(root, text="Options", bg="white", font=large_font)
    title_label.grid(row=0, column=0)

    def on_exit():
        root.running = False

    def on_ok():
        # save all info

        on_exit()

    root.protocol("WM_DELETE_WINDOW", on_exit)

    ok_button = Button(root, text="Ok", command= on_ok)
    ok_button.grid(row=3, column=3)

    cancel_button = Button(root, text= "Cancel", command= on_exit)
    cancel_button.grid(row=3, column= 1)

    while root.running:
        root.update()
    root.destroy()


if __name__ == "__main__":
    show_options()
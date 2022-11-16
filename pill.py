
from tkinter import *
from options import *
#from main import recall

def give_pill(sym1,sym2,sym3):
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

    def diagnose(sym1,sym2,sym3):
        print(sym1,sym2,sym3)

        if sym1 == 1:
            print("a pill")
        elif sym2 ==1:
            print("b pill")
        elif sym3 ==1:
            print("b pill")
        else:
            print("check prescription")    




    def on_exit():
        root.running = False


    root.protocol("WM_DELETE_WINDOW", on_exit)

    cancel_button = Button(root, text= "Cancel", command= on_exit)
    cancel_button.grid(row=2, column= 1)
    diagnose(sym1,sym2,sym3)

    while root.running:
        root.update()
    root.destroy()

    #mechanical processes
    #update pill count


if __name__ == "__main__":
    give_pill()
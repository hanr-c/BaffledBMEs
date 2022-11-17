#main for BB

from options import show_options
from tkinter import *
from tkinter import IntVar
# :(
from pill import give_pill
import time

def show_app():

    #fonts (changable)
    small_font = ("Arial", 10)
    medium_font = ("Arial", 15)
    large_font = ("Arial", 20)
    
    # calling the gui
    root = Tk()
    root.running = True
    root.configure(bg="white")
    frame = None
    frame = Frame(root, bg="white", relief=RAISED, borderwidth=1)
    frame.grid(row=1, column=1, rowspan=3, columnspan=3)
    info_text.grid(row=1, column=0, padx = 5)
    text = Text(root)

    #team name
    frame_label = Label(root, text = "Baffled BMEs Pill Dispenser",font = small_font, bg="white")
    frame_label.grid(row=0, column=0)

    #closing the window
    def on_exit():
        root.running = False     
    root.protocol("WM_DELETE_WINDOW", on_exit)


    #sends symptom info to pill.py
    def on_pill():
        #clear checklist?
        give_pill(s1,s2,s3)

    # options window
    def give_options():
        #prescription pills
        #insert pill numbers 
        #insert dosage time

        #pain pills
        #insert numbers
        #insert dosage time

        #sick pills
        #insert numbers
        #insert dosage time

        show_options()

    #getting symptoms
    def store_syms():
        global s1
        global s2
        global s3
        s1= sym_1.get()
        s2 =sym_2.get()
        s3 =sym_3.get()


    #recalling time since dosage
    def recall():
        #if symptom pill taken
        #print symptom
        #print time since symptom
        #timesym = [pill, ": ", pill_time]
        timesym = "Benadryl: 08:30 ago"
        print(timesym)

    # warning to replace pill
    def warning():
        #edit to include pill that is low
        warning_text =Label(root, text= "Warning Replace: Pill", font= medium_font, bg="white", fg= "red")
        warning_text.grid(row=4, column=0)


    sym_1 = IntVar()
    sym_2 = IntVar()
    sym_3= IntVar()

    #place holders
    timesym = StringVar()
    
    timepres = StringVar()
    timepres = "NEED TO TAKE"
    
    # ye old checklist for symptoms
    sym_label = Label(root, text = "Symptoms:",font = medium_font, bg="white")
    sym_label.grid(row=0, column=3)
    sym1 = Checkbutton(root, text = "Headache", variable =sym_1, onvalue= 1, offvalue= 0, command=store_syms(), bg="white" )
    sym1.grid(row= 1, column = 3, padx = 5, pady =5)
    sym2 = Checkbutton(root, text = "Sickness", variable =sym_2, onvalue= 1, offvalue= 0,  command=store_syms(), bg="white" )
    sym2.grid(row = 2, column = 3, padx = 5, pady =5)
    sym3 = Checkbutton(root, text = "Pain", variable =sym_3, onvalue= 1, offvalue= 0,  command=store_syms(),bg="white" )
    sym3.grid(row = 3, column = 3, padx = 5, pady =5)


    # pills last taken
    info_text =Label(root, text= "Pills last taken:", font= medium_font, bg="white")
    recall_text = Label(root, text= timesym, font= small_font, bg="white")
    recall_text.grid(row =2, column=0, padx = 5)

    prescription_text =Label(root, text= "Prescription:", font= medium_font, bg="white")
    prescription_text.grid(row=3, column=0)
    pre_recall_text = Label(root, text= timepres, font= medium_font, bg="white")
    pre_recall_text.grid(row =3, column=1,)

    options_button = Button(root, text="Options", command=give_options, bg="white", font= medium_font)
    options_button.grid(row=5, column=0, padx = 10, pady =10)

    pill_button = Button(root, text="Give Pill", bg="white",command=on_pill, font= medium_font)
    pill_button.grid(row=5, column=3, padx = 10, pady =10)

    while root.running:
        root.update()
        warning()
    root.destroy()
     


if __name__ == "__main__":
    show_app()



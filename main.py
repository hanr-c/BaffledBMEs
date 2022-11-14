#main for BB

from options import show_options
from tkinter import *
from tkinter import IntVar
# :(
from pill import give_pill

def show_app():

    small_font = ("Arial", 10)
    medium_font = ("Arial", 15)
    large_font = ("Arial", 20)
    

    root = Tk()
    root.running = True
    root.configure(bg="white")

    frame = None
    frame = Frame(root, bg="white", relief=RAISED, borderwidth=1)
    frame.grid(row=1, column=1, rowspan=3, columnspan=3)
    frame_label = Label(root, text = "Baffled BMEs Pill Dispenser",font = small_font, bg="white")
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

    def store_syms():
        
        symptoms = [
         sym_1.get(), 
         sym_2.get(),
         sym_3.get(),
         sym_4.get()
         ]
        print(symptoms)
         #somehow through that to give_pill

    def recall():
        #if symptom pill taken
        #print symptom
        #print time since symptom
        timesym = [pill, ": ", pill_time]
        print(timesym)

    def warning():
        #enter pill count
        warning_text =Label(root, text= "Warning Replace: Pill", font= medium_font, bg="white")
        warning_text.grid(row=4, column=0)



    options_button = Button(root, text="Options", command=give_options, bg="white", font= medium_font)
    options_button.grid(row=5, column=0, padx = 10, pady =10)

    pill_button = Button(root, text="Give Pill", command=on_pill, bg="white", font= medium_font)
    pill_button.grid(row=5, column=3, padx = 10, pady =10)

    sym_1 = IntVar()
    sym_2 = IntVar()
    sym_3= IntVar()
    sym_4 = IntVar()
    timesym = StringVar()
    timesym = "Benadryl: 08:30 ago"
    timepres = StringVar()
    timepres = "NEED TO TAKE"
    
    sym_label = Label(root, text = "Symptoms:",font = medium_font, bg="white")
    sym_label.grid(row=0, column=3)
    sym1 = Checkbutton(root, text = "Headache", variable =sym_1, onvalue= 1, offvalue= 0, command=store_syms, bg="white" )
    sym1.grid(row= 1, column = 3, padx = 5, pady =5)
    sym2 = Checkbutton(root, text = "Sickness", variable =sym_2, onvalue= 1, offvalue= 0, command=store_syms, bg="white" )
    sym2.grid(row = 2, column = 3, padx = 5, pady =5)
    sym3 = Checkbutton(root, text = "Pain", variable =sym_3, onvalue= 1, offvalue= 0, command=store_syms, bg="white" )
    sym3.grid(row = 3, column = 3, padx = 5, pady =5)
    sym4 = Checkbutton(root, text = "Other", variable =sym_4, onvalue= 1, offvalue= 0, command=store_syms, bg="white" )
    sym4.grid(row = 4, column = 3, padx = 5, pady =5)

    text = Text(root)

    info_text =Label(root, text= "Pills last taken:", font= medium_font, bg="white")
    info_text.grid(row=1, column=0, padx = 5)
    recall_text = Label(root, text= timesym, font= small_font, bg="white")
    recall_text.grid(row =2, column=0, padx = 5)

    prescription_text =Label(root, text= "Prescription:", font= medium_font, bg="white")
    prescription_text.grid(row=3, column=0)
    pre_recall_text = Label(root, text= timepres, font= medium_font, bg="white")
    pre_recall_text.grid(row =3, column=1,)



    while root.running:
        root.update()
        warning()
    root.destroy()
     


if __name__ == "__main__":
    show_app()



import tkinter

window = tkinter.Tk()
window.title("Second")
window.config(padx=100,pady=100)
window.minsize(width=500,height=500)

label_1 = tkinter.Label(text="Abo")
label_1.config(bg="black")
label_1.config(fg="white")
label_1.config(padx=100,pady=100)
label_1.pack()


def mia():
    print("Clicked")

button_1 = tkinter.Button(text="Click",command=mia)
button_1.pack()

# text birden fazla cümle almak için entry yerine text kullanıcaz
text_1 = tkinter.Text()


def scale_sec(value):
    print(value)

#scale
scale_1 = tkinter.Scale(from_=0,to=100,command=scale_sec)
scale_1.pack()

def spinme():
    print(spinbox_1.get())
#spinbox
spinbox_1 = tkinter.Spinbox(from_=0,to=100,command=spinme)
spinbox_1.pack()

#checkbutton
def checkbut():
    print(check_state.get())
check_state = tkinter.IntVar()
checkbut_1 = tkinter.Checkbutton(text="checkbut",variable=check_state,command=checkbut)
checkbut_1.pack()


#radio_button matığı birden fazla kullanım
def radiokilletheradiostar():
    print(radio_01_state.get())
radio_01_state = tkinter.IntVar()
radio_button_1 = tkinter.Radiobutton(text="radbut_01",value=5, variable=radio_01_state,command=radiokilletheradiostar)
radio_button_2 = tkinter.Radiobutton(text="radbut",value=10,variable=radio_01_state,command=radiokilletheradiostar)
radio_button_1.pack()
radio_button_2.pack()

#listbox
def selectionoglist(event):
    print(listbox_1.get(listbox_1.curselection()))
listbox_1 = tkinter.Listbox()
list_1 = ["Barkın","Demirci","abc","ABC"]
listbox_1.bind('<<ListboxSelect>>',func=selectionoglist)

for i in range(len(list_1)):
    listbox_1.insert(i,list_1[i])
listbox_1.pack()





#güncelledikçe push larım

window.mainloop()

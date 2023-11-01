import tkinter

window = tkinter.Tk()
window.title("İlk Deneme")
window.minsize(width=500,height=500)
#label kullanıcıya metin göstrmek için kullandığımız fonkisiyonlarlar

def button_click():
    mama = ma_entry.get()

    print(mama)


ma_label = tkinter.Label(text="Deneme1-2-3")
ma_label.config(bg="black",fg="white")
#ma_label.pack(side="left")
#ma_label.place()

#button
ma_button = tkinter.Button(text="button",command=button_click)
# ma_button.pack()

#entry
ma_entry = tkinter.Entry(width=20,)

ma_entry.grid()

#entry ye girenleri almak için .get demen yeter mesela    ma_entry.get desem çıktıyı alabiliyorum





window.mainloop()
